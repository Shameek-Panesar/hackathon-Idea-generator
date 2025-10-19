"""
Test script for the Hackathon Idea Generator.
Run this to test the RAG engine without the UI.
"""

import os
from dotenv import load_dotenv
from rag_engine import HackathonRAGEngine
from knowledge_base import get_all_ideas

def print_separator():
    print("\n" + "="*80 + "\n")

def test_knowledge_base():
    """Test the knowledge base."""
    print_separator()
    print("📚 Testing Knowledge Base...")
    print_separator()
    
    ideas = get_all_ideas()
    print(f"✅ Found {len(ideas)} ideas in the knowledge base")
    
    print("\nSample idea:")
    sample = ideas[0]
    print(f"  Title: {sample['title']}")
    print(f"  Theme: {sample['theme']}")
    print(f"  Difficulty: {sample['difficulty']}")
    print(f"  Tech Stack: {', '.join(sample['tech_stack'])}")
    
    return True

def test_rag_engine():
    """Test the RAG engine initialization."""
    print_separator()
    print("🤖 Testing RAG Engine Initialization...")
    print_separator()
    
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "your_openai_api_key_here":
        print("❌ ERROR: OpenAI API key not set in .env file")
        print("\nPlease:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key")
        print("3. Run this test again")
        return False
    
    try:
        print("Initializing RAG engine...")
        engine = HackathonRAGEngine(openai_api_key=api_key)
        print("✅ RAG engine created successfully")
        
        print("\nInitializing knowledge base...")
        num_docs = engine.initialize_knowledge_base()
        print(f"✅ Knowledge base initialized with {num_docs} documents")
        
        return engine
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return None

def test_similarity_search(engine):
    """Test similarity search."""
    print_separator()
    print("🔍 Testing Similarity Search...")
    print_separator()
    
    query = "healthcare AI project"
    print(f"Query: '{query}'")
    
    try:
        results = engine.retrieve_similar_ideas(query, k=3)
        print(f"\n✅ Found {len(results)} similar ideas:\n")
        
        for i, result in enumerate(results, 1):
            print(f"{i}. Similarity Score: {result['similarity_score']:.4f}")
            print(f"   Metadata: {result['metadata']['title']}")
            print(f"   Theme: {result['metadata']['theme']}\n")
        
        return True
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def test_idea_generation(engine):
    """Test idea generation."""
    print_separator()
    print("✨ Testing Idea Generation...")
    print_separator()
    
    print("Generating idea with parameters:")
    print("  Theme: Healthcare")
    print("  Difficulty: Intermediate")
    print("  Tech Stack: Python, React")
    print("\nThis may take 10-20 seconds...\n")
    
    try:
        result = engine.generate_idea(
            theme="Healthcare",
            difficulty="Intermediate",
            tech_stack=["Python", "React"],
            custom_requirements="Focus on accessibility"
        )
        
        print("✅ Idea generated successfully!\n")
        print("="*80)
        print(result['generated_idea'])
        print("="*80)
        
        print("\n📊 Similar ideas used for context:")
        for i, idea in enumerate(result['similar_ideas'], 1):
            print(f"{i}. {idea['metadata']['title']} (score: {idea['similarity_score']:.4f})")
        
        return True
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("  🧪 Hackathon Idea Generator - Test Suite")
    print("="*80)
    
    # Test 1: Knowledge Base
    if not test_knowledge_base():
        return
    
    # Test 2: RAG Engine
    engine = test_rag_engine()
    if not engine:
        return
    
    # Test 3: Similarity Search
    if not test_similarity_search(engine):
        return
    
    # Test 4: Idea Generation
    test_idea_generation(engine)
    
    print_separator()
    print("✅ All tests completed!")
    print("\nYour Hackathon Idea Generator is working correctly!")
    print("Run 'streamlit run app.py' to start the web interface.")
    print_separator()

if __name__ == "__main__":
    main()
