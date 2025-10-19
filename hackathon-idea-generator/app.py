"""
Streamlit web application for the Hackathon Idea Generator.
Features an interactive UI for generating AI-powered hackathon ideas.
"""

import streamlit as st
import os
from dotenv import load_dotenv
from rag_engine import HackathonRAGEngine
from knowledge_base import get_all_ideas

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Hackathon Idea Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .idea-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'rag_engine' not in st.session_state:
    st.session_state.rag_engine = None
if 'generated_idea' not in st.session_state:
    st.session_state.generated_idea = None
if 'api_key_set' not in st.session_state:
    st.session_state.api_key_set = False

def initialize_rag_engine(api_key):
    """Initialize the RAG engine with the provided API key."""
    try:
        engine = HackathonRAGEngine(gemini_api_key=api_key)
        with st.spinner("Initializing knowledge base..."):
            num_docs = engine.initialize_knowledge_base()
        st.session_state.rag_engine = engine
        st.session_state.api_key_set = True
        st.success(f"✅ RAG engine initialized with {num_docs} sample ideas!")
        return True
    except Exception as e:
        st.error(f"❌ Error initializing RAG engine: {str(e)}")
        return False

def main():
    """Main application function."""
    
    # Header
    st.markdown('<h1 class="main-header">🚀 Hackathon Idea Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Generate innovative hackathon ideas powered by AI and RAG</p>', unsafe_allow_html=True)
    
    # Sidebar for API key and settings
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Auto-load API key from .env (hidden from user)
        api_key = os.getenv("GEMINI_API_KEY", "")
        
        if api_key and not st.session_state.api_key_set:
            if st.button("Initialize RAG Engine"):
                initialize_rag_engine(api_key)
        
        if st.session_state.api_key_set:
            st.success("✅ RAG Engine Ready!")
        
        st.divider()
        
        st.header("📚 About")
        st.markdown("""
        This tool uses:
        - **Google Gemini** for idea generation
        - **RAG** for context-aware suggestions
        - **ChromaDB** for vector storage
        - **LangChain** for orchestration
        
        The system retrieves similar ideas from a knowledge base and uses them as context to generate unique, innovative hackathon projects.
        """)
        
        st.divider()
        
        # View knowledge base
        if st.button("📖 View Sample Ideas"):
            st.session_state.show_samples = True
    
    # Main content
    if not st.session_state.api_key_set:
        st.warning("⚠️ Please click 'Initialize RAG Engine' in the sidebar to get started.")
        
        st.info("💡 **Using Google Gemini API** for AI-powered idea generation")
        
        # Show sample ideas from knowledge base
        st.header("📚 Sample Ideas in Knowledge Base")
        ideas = get_all_ideas()[:5]  # Show first 5
        for idea in ideas:
            with st.expander(f"🎯 {idea['title']}"):
                st.write(f"**Theme:** {idea['theme']}")
                st.write(f"**Difficulty:** {idea['difficulty']}")
                st.write(f"**Description:** {idea['description']}")
                st.write(f"**Tech Stack:** {', '.join(idea['tech_stack'])}")
                st.write(f"**Team Size:** {idea['team_size']}")
        
        return
    
    # Tabs for different functionalities
    tab1, tab2, tab3 = st.tabs(["🎨 Generate Idea", "💡 Random Inspiration", "📊 Browse Knowledge Base"])
    
    with tab1:
        st.header("Generate Custom Hackathon Idea")
        
        # Topic input - Main feature
        topic = st.text_input(
            "🎯 Enter Your Topic",
            placeholder="E.g., 'AI for climate change', 'Blockchain voting', 'Mental health app'",
            help="Enter the main topic or idea for your hackathon project"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            theme = st.selectbox(
                "Theme",
                ["Any", "Healthcare", "Sustainability", "Education", "Blockchain", 
                 "Social Impact", "AR/VR", "IoT", "Developer Tools", "Accessibility"],
                help="Choose a theme for your hackathon project"
            )
            
            difficulty = st.selectbox(
                "Difficulty Level",
                ["Any", "Beginner", "Intermediate", "Advanced"],
                help="Select the complexity level"
            )
        
        with col2:
            team_size = st.selectbox(
                "Team Size",
                ["Any", "1-2", "2-3", "3-4", "4-5", "5+"],
                help="How many people will work on this project?"
            )
            
            tech_options = st.multiselect(
                "Preferred Technologies (optional)",
                ["Python", "JavaScript", "React", "Node.js", "TensorFlow", 
                 "PyTorch", "MongoDB", "PostgreSQL", "Firebase", "AWS",
                 "Docker", "Kubernetes", "Blockchain", "Unity", "Flutter"],
                help="Select technologies you'd like to use"
            )
        
        custom_requirements = st.text_area(
            "Additional Requirements (optional)",
            placeholder="E.g., 'Must use computer vision', 'Should help elderly people', 'Focus on mobile-first design'",
            help="Add any specific requirements or constraints"
        )
        
        if st.button("🚀 Generate Hackathon Idea", type="primary"):
            # Prepare parameters
            params = {
                "topic": topic if topic else None,
                "theme": None if theme == "Any" else theme,
                "difficulty": None if difficulty == "Any" else difficulty,
                "tech_stack": tech_options if tech_options else None,
                "team_size": None if team_size == "Any" else team_size,
                "custom_requirements": custom_requirements if custom_requirements else None
            }
            
            # Generate idea
            with st.spinner("🤖 AI is generating your hackathon idea..."):
                try:
                    result = st.session_state.rag_engine.generate_idea(**params)
                    st.session_state.generated_idea = result
                except Exception as e:
                    st.error(f"❌ Error generating idea: {str(e)}")
                    return
        
        # Display generated idea
        if st.session_state.generated_idea:
            st.divider()
            st.subheader("✨ Your Generated Hackathon Idea")
            
            # Main idea
            st.markdown(st.session_state.generated_idea['generated_idea'])
            
            # Similar ideas used for context
            with st.expander("🔍 Similar Ideas Used for Context (RAG)"):
                for i, idea in enumerate(st.session_state.generated_idea['similar_ideas'], 1):
                    st.markdown(f"**{i}. Reference Idea**")
                    st.text(idea['content'])
                    st.caption(f"Similarity Score: {idea['similarity_score']:.4f}")
                    st.divider()
            
            # Download button
            idea_text = st.session_state.generated_idea['generated_idea']
            st.download_button(
                label="📥 Download Idea as Text",
                data=idea_text,
                file_name="hackathon_idea.txt",
                mime="text/plain"
            )
    
    with tab2:
        st.header("Get Random Inspiration")
        st.write("Not sure where to start? Get a random idea from our knowledge base!")
        
        if st.button("🎲 Get Random Idea"):
            inspiration = st.session_state.rag_engine.get_random_inspiration()
            st.markdown('<div class="idea-box">', unsafe_allow_html=True)
            st.markdown(inspiration)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.header("Browse Knowledge Base")
        st.write("Explore all the sample ideas in our knowledge base:")
        
        ideas = get_all_ideas()
        
        # Filters
        col1, col2 = st.columns(2)
        with col1:
            filter_theme = st.selectbox("Filter by Theme", ["All"] + list(set(idea['theme'] for idea in ideas)))
        with col2:
            filter_difficulty = st.selectbox("Filter by Difficulty", ["All"] + list(set(idea['difficulty'] for idea in ideas)))
        
        # Apply filters
        filtered_ideas = ideas
        if filter_theme != "All":
            filtered_ideas = [idea for idea in filtered_ideas if idea['theme'] == filter_theme]
        if filter_difficulty != "All":
            filtered_ideas = [idea for idea in filtered_ideas if idea['difficulty'] == filter_difficulty]
        
        st.write(f"**Showing {len(filtered_ideas)} ideas**")
        
        # Display ideas in a grid
        for i in range(0, len(filtered_ideas), 2):
            col1, col2 = st.columns(2)
            
            with col1:
                if i < len(filtered_ideas):
                    idea = filtered_ideas[i]
                    with st.container():
                        st.markdown(f"### {idea['title']}")
                        st.write(f"**Theme:** {idea['theme']} | **Difficulty:** {idea['difficulty']}")
                        st.write(idea['description'])
                        st.write(f"**Tech:** {', '.join(idea['tech_stack'][:3])}{'...' if len(idea['tech_stack']) > 3 else ''}")
                        st.write(f"**Team Size:** {idea['team_size']}")
            
            with col2:
                if i + 1 < len(filtered_ideas):
                    idea = filtered_ideas[i + 1]
                    with st.container():
                        st.markdown(f"### {idea['title']}")
                        st.write(f"**Theme:** {idea['theme']} | **Difficulty:** {idea['difficulty']}")
                        st.write(idea['description'])
                        st.write(f"**Tech:** {', '.join(idea['tech_stack'][:3])}{'...' if len(idea['tech_stack']) > 3 else ''}")
                        st.write(f"**Team Size:** {idea['team_size']}")
            
            st.divider()

if __name__ == "__main__":
    main()
