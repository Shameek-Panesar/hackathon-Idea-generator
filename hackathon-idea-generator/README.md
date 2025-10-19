# 🚀 Hackathon Idea Generator

An AI-powered hackathon idea generator that uses OpenAI's GPT models and RAG (Retrieval-Augmented Generation) to create innovative and creative hackathon project ideas.

## Features

- 🤖 **AI-Powered Generation**: Uses OpenAI GPT models to generate creative hackathon ideas
- 🔍 **RAG Implementation**: Retrieval-Augmented Generation for context-aware suggestions
- 💾 **Vector Database**: ChromaDB for semantic search of similar ideas
- 🎨 **Interactive UI**: Beautiful Streamlit web interface
- ⚙️ **Customizable**: Filter by theme, difficulty, tech stack, and team size
- 📚 **Knowledge Base**: Pre-loaded with example hackathon ideas

## Installation

1. Clone this repository or download the files

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## How It Works

1. **Knowledge Base**: The app uses a vector database (ChromaDB) to store and retrieve similar hackathon ideas
2. **RAG Pipeline**: When you request an idea, the system:
   - Retrieves relevant context from the knowledge base
   - Sends the context + your parameters to OpenAI's GPT model
   - Generates a unique, contextualized hackathon idea
3. **Customization**: You can specify themes, difficulty levels, tech stacks, and team sizes

## Project Structure

```
hackaton idea generator/
├── app.py                  # Main Streamlit application
├── rag_engine.py          # RAG implementation
├── knowledge_base.py      # Sample hackathon ideas database
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Technologies Used

- **OpenAI GPT**: For idea generation
- **LangChain**: For RAG implementation
- **ChromaDB**: Vector database for semantic search
- **Streamlit**: Web interface
- **Python**: Core programming language

## Example Ideas Generated

The generator can create ideas like:
- AI-powered sustainability solutions
- Blockchain voting systems
- AR/VR educational platforms
- Healthcare accessibility apps
- And much more!

## License

MIT License - feel free to use this project for your hackathons!

## Contributing

Pull requests are welcome! Feel free to improve the knowledge base or add new features.
