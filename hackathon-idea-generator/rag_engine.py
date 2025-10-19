"""
Simple RAG Engine for Hackathon Idea Generator using Google Gemini.
Uses keyword matching instead of embeddings to avoid quota issues.
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from knowledge_base import get_all_ideas
import google.generativeai as genai

# Load environment variables
load_dotenv()


class HackathonRAGEngine:
    """RAG Engine for generating hackathon ideas with context retrieval."""
    
    def __init__(self, gemini_api_key: Optional[str] = None):
        """Initialize the RAG engine with Google Gemini."""
        self.api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY in .env file.")
        
        # Configure Gemini API
        genai.configure(api_key=self.api_key)
        
        # Initialize the model with correct name
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Load knowledge base
        self.ideas = get_all_ideas()
        
    def initialize_knowledge_base(self):
        """Initialize the knowledge base (just loads ideas)."""
        return len(self.ideas)
    
    def retrieve_similar_ideas(self, query: str, k: int = 3) -> List[Dict]:
        """Retrieve similar ideas using keyword matching."""
        query_lower = query.lower()
        
        # Score ideas based on keyword matches
        scored_ideas = []
        for idea in self.ideas:
            score = 0
            searchable_text = f"{idea['title']} {idea['description']} {idea['theme']} {' '.join(idea['tech_stack'])}".lower()
            
            # Simple keyword scoring
            for word in query_lower.split():
                if len(word) > 3:  # Only consider words longer than 3 characters
                    score += searchable_text.count(word)
            
            if score > 0:
                scored_ideas.append((score, idea))
        
        # Sort by score and get top k
        scored_ideas.sort(reverse=True, key=lambda x: x[0])
        
        similar_ideas = []
        for i, (score, idea) in enumerate(scored_ideas[:k]):
            similar_ideas.append({
                "content": f"""Title: {idea['title']}
Description: {idea['description']}
Theme: {idea['theme']}
Difficulty: {idea['difficulty']}
Tech Stack: {', '.join(idea['tech_stack'])}
Team Size: {idea['team_size']}""",
                "metadata": idea,
                "similarity_score": score / 10.0  # Normalize score
            })
        
        # If no matches, return random ideas
        if not similar_ideas:
            import random
            for idea in random.sample(self.ideas, min(k, len(self.ideas))):
                similar_ideas.append({
                    "content": f"""Title: {idea['title']}
Description: {idea['description']}
Theme: {idea['theme']}
Difficulty: {idea['difficulty']}
Tech Stack: {', '.join(idea['tech_stack'])}
Team Size: {idea['team_size']}""",
                    "metadata": idea,
                    "similarity_score": 0.5
                })
        
        return similar_ideas
    
    def generate_idea(
        self,
        topic: Optional[str] = None,
        theme: Optional[str] = None,
        difficulty: Optional[str] = None,
        tech_stack: Optional[List[str]] = None,
        team_size: Optional[str] = None,
        custom_requirements: Optional[str] = None
    ) -> Dict:
        """
        Generate a new hackathon idea using RAG.
        
        Args:
            topic: Main topic for the hackathon idea
            theme: Project theme (e.g., "Healthcare", "Sustainability")
            difficulty: Difficulty level ("Beginner", "Intermediate", "Advanced")
            tech_stack: Preferred technologies
            team_size: Team size (e.g., "2-3", "4-5")
            custom_requirements: Any additional custom requirements
        
        Returns:
            Dictionary containing the generated idea
        """
        # Build the query for retrieval
        query_parts = []
        if topic:
            query_parts.append(topic)
        if theme:
            query_parts.append(f"Theme: {theme}")
        if difficulty:
            query_parts.append(f"Difficulty: {difficulty}")
        if tech_stack:
            query_parts.append(f"Technologies: {', '.join(tech_stack)}")
        if custom_requirements:
            query_parts.append(custom_requirements)
        
        query = " ".join(query_parts) if query_parts else "innovative hackathon project"
        
        # Retrieve similar ideas for context
        similar_ideas = self.retrieve_similar_ideas(query, k=3)
        
        # Build context from retrieved ideas
        context = "Here are some similar hackathon ideas for inspiration:\n\n"
        for i, idea in enumerate(similar_ideas, 1):
            context += f"{i}. {idea['content']}\n\n"
        
        # Build the generation prompt
        prompt = f"""You are a creative hackathon idea generator. Based on the context provided and the user's requirements, generate a unique and innovative hackathon project idea.

Context (Similar Ideas for Inspiration):
{context}

Requirements:
"""
        if topic:
            prompt += f"- Main Topic: {topic}\n"
        if theme:
            prompt += f"- Theme: {theme}\n"
        if difficulty:
            prompt += f"- Difficulty Level: {difficulty}\n"
        if tech_stack:
            prompt += f"- Preferred Technologies: {', '.join(tech_stack)}\n"
        if team_size:
            prompt += f"- Team Size: {team_size}\n"
        if custom_requirements:
            prompt += f"- Additional Requirements: {custom_requirements}\n"
        
        prompt += """
Generate a UNIQUE hackathon idea (don't copy the examples) with the following structure:

1. **Title**: A catchy, memorable name for the project

2. **Description**: A detailed description (2-3 paragraphs) explaining what the project does, its key features, and its impact

3. **Target Audience**: Who would benefit from this project

4. **Key Features**: List 4-6 main features

5. **Technical Approach**: How would you build this (architecture overview)

6. **Innovation Factor**: What makes this idea unique and innovative

7. **Potential Challenges**: 2-3 challenges the team might face

8. **Success Metrics**: How to measure if the project is successful

Make sure the idea is creative, feasible within a hackathon timeframe, and addresses a real problem or need.
"""
        
        # Generate the idea using Gemini
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            generated_text = response.text
        except Exception as e:
            # If gemini-pro fails, try with models/gemini-pro
            try:
                model = genai.GenerativeModel('models/gemini-pro')
                response = model.generate_content(prompt)
                generated_text = response.text
            except Exception as e2:
                raise Exception(f"Error generating idea: {str(e2)}")
        
        return {
            "generated_idea": generated_text,
            "similar_ideas": similar_ideas,
            "parameters": {
                "topic": topic,
                "theme": theme,
                "difficulty": difficulty,
                "tech_stack": tech_stack,
                "team_size": team_size,
                "custom_requirements": custom_requirements
            }
        }
    
    def get_random_inspiration(self) -> str:
        """Get a random idea from the knowledge base for inspiration."""
        import random
        ideas = get_all_ideas()
        if ideas:
            idea = random.choice(ideas)
            return f"""**{idea['title']}**

{idea['description']}

**Theme**: {idea['theme']}
**Difficulty**: {idea['difficulty']}
**Tech Stack**: {', '.join(idea['tech_stack'])}
**Team Size**: {idea['team_size']}
"""
        return "No ideas available in the knowledge base."
