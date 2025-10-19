"""
Example usage of the Hackathon Idea Generator RAG Engine.
This script demonstrates how to use the RAG engine programmatically.
"""

import os
from dotenv import load_dotenv
from rag_engine import HackathonRAGEngine

# Load environment variables
load_dotenv()

def example_basic_generation():
    """Example: Basic idea generation."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Idea Generation")
    print("="*80 + "\n")
    
    # Initialize engine
    engine = HackathonRAGEngine()
    engine.initialize_knowledge_base()
    
    # Generate a simple idea
    result = engine.generate_idea(
        theme="Education",
        difficulty="Beginner"
    )
    
    print(result['generated_idea'])
    print("\n")

def example_custom_requirements():
    """Example: Idea generation with custom requirements."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Idea with Custom Requirements")
    print("="*80 + "\n")
    
    engine = HackathonRAGEngine()
    engine.initialize_knowledge_base()
    
    # Generate idea with specific requirements
    result = engine.generate_idea(
        theme="Social Impact",
        difficulty="Intermediate",
        tech_stack=["React Native", "Firebase", "Python"],
        team_size="3-4",
        custom_requirements="Must help underprivileged communities and work offline"
    )
    
    print(result['generated_idea'])
    print("\n")

def example_similarity_search():
    """Example: Finding similar ideas."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Similarity Search")
    print("="*80 + "\n")
    
    engine = HackathonRAGEngine()
    engine.initialize_knowledge_base()
    
    # Search for similar ideas
    query = "blockchain healthcare privacy"
    results = engine.retrieve_similar_ideas(query, k=3)
    
    print(f"Query: '{query}'\n")
    print(f"Found {len(results)} similar ideas:\n")
    
    for i, result in enumerate(results, 1):
        print(f"{i}. Score: {result['similarity_score']:.4f}")
        print(f"   Title: {result['metadata']['title']}")
        print(f"   Theme: {result['metadata']['theme']}")
        print(f"   Description: {result['metadata']['description'][:100]}...")
        print()

def example_random_inspiration():
    """Example: Get random inspiration."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Random Inspiration")
    print("="*80 + "\n")
    
    engine = HackathonRAGEngine()
    engine.initialize_knowledge_base()
    
    # Get random idea
    inspiration = engine.get_random_inspiration()
    print(inspiration)
    print("\n")

def example_advanced_generation():
    """Example: Advanced idea generation with all parameters."""
    print("\n" + "="*80)
    print("EXAMPLE 5: Advanced Generation")
    print("="*80 + "\n")
    
    engine = HackathonRAGEngine()
    engine.initialize_knowledge_base()
    
    # Generate advanced idea
    result = engine.generate_idea(
        theme="Sustainability",
        difficulty="Advanced",
        tech_stack=["Python", "TensorFlow", "IoT", "React", "AWS"],
        team_size="4-5",
        custom_requirements="Use machine learning and IoT sensors to solve climate change problems. Must be scalable and cost-effective."
    )
    
    print(result['generated_idea'])
    
    print("\n" + "-"*80)
    print("Similar ideas used for context:")
    print("-"*80 + "\n")
    
    for i, idea in enumerate(result['similar_ideas'], 1):
        print(f"{i}. {idea['metadata']['title']}")
        print(f"   Similarity: {idea['similarity_score']:.4f}")
        print(f"   Theme: {idea['metadata']['theme']}\n")

if __name__ == "__main__":
    print("\n" + "="*80)
    print("  Hackathon Idea Generator - Usage Examples")
    print("="*80)
    
    print("\nNOTE: Make sure you have set your OPENAI_API_KEY in the .env file!")
    print("These examples will call the OpenAI API and may incur costs.")
    
    input("\nPress Enter to continue with the examples...")
    
    # Run examples (comment out the ones you don't want to run)
    try:
        # Example 1: Basic generation
        # example_basic_generation()
        
        # Example 2: Custom requirements
        # example_custom_requirements()
        
        # Example 3: Similarity search
        example_similarity_search()
        
        # Example 4: Random inspiration
        example_random_inspiration()
        
        # Example 5: Advanced generation
        # example_advanced_generation()
        
        print("\n" + "="*80)
        print("  Examples completed successfully!")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure:")
        print("1. You have installed all requirements: pip install -r requirements.txt")
        print("2. Your OpenAI API key is set in the .env file")
        print("3. You have an active internet connection")
