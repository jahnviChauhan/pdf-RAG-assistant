PDF RAG Assistant

This is my first Retrieval-Augmented Generation (RAG) project built using Python, LangChain, FAISS, and Google Gemini.

The project reads a PDF document, converts it into searchable chunks using embeddings, stores them in a FAISS vector database, and answers user questions based on the document content.

I built this project to understand how modern AI systems retrieve information from documents instead of relying only on general model knowledge.

Features
Load and process PDF files
Split large documents into chunks
Generate embeddings using Gemini Embeddings
Store vectors using FAISS
Retrieve relevant chunks using semantic similarity
Generate answers using Gemini
Tech Stack
Python
LangChain
FAISS
Google Gemini API
PyPDF
dotenv
Project Structure
pdf-RAG-assistant/
│
├── app.py
├── data.pdf
├── .env
├── .gitignore
├── requirements.txt
└── README.md
Setup
1. Clone the repository
git clone https://github.com/jahnviChauhan/pdf-RAG-assistant.git
cd pdf-RAG-assistant
2. Create virtual environment
Linux / Mac
python3 -m venv venv
source venv/bin/activate
Windows
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
API Key Setup

Create a .env file and add your Gemini API key:

GOOGLE_API_KEY=your_api_key

Get API key from:

Google AI Studio

Run the project
python3 app.py
Example Questions
What is DBMS?

Explain normalization.

What are the advantages of DBMS?

What is functional dependency?
How the Pipeline Works
PDF
↓
Chunking
↓
Embeddings
↓
FAISS Vector Store
↓
Semantic Retrieval
↓
Gemini Response
What I Learned

While building this project, I learned:

how the RAG pipeline works
document chunking
embeddings and vector databases
semantic retrieval
LangChain basics
debugging APIs and Python environments

This project also helped me understand how AI assistants can answer questions using external knowledge sources like PDFs.

Future Improvements
Streamlit UI
Multiple PDF support
Chat interface
Better prompt engineering
Deployment