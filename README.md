# PDF RAG Assistant 🚀

A Retrieval-Augmented Generation (RAG) based PDF Question Answering system built using Python, LangChain, FAISS, and Google Gemini.

This project allows users to query a PDF document in natural language.  
The system retrieves the most relevant chunks from the document using semantic similarity search and generates grounded responses using Gemini.

---

## Features

- PDF document ingestion
- Text chunking using LangChain
- Semantic embeddings with Gemini
- FAISS vector database integration
- Context-aware question answering
- Retrieval-Augmented Generation (RAG) pipeline

---

## Tech Stack

- Python
- LangChain
- FAISS
- Google Gemini API
- PyPDF
- dotenv

---

## Project Structure

```bash
pdf-RAG-assistant/
│
├── app.py
├── data.pdf
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jahnviChauhan/pdf-RAG-assistant.git
cd pdf-RAG-assistant
```

---

### 2. Create Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

Generate API key from:

https://aistudio.google.com/app/apikey

---

## About the PDF

I used a random DBMS PDF from the internet just for testing the pipeline and retrieval system.

You can replace it with any PDF of your choice.

To use your own PDF:

1. Add your PDF file to the project folder
2. Rename it to:

```bash
data.pdf
```

OR change the filename inside `app.py`:

```python
loader = PyPDFLoader("your_file_name.pdf")
```

You can try it with:
- study notes
- research papers
- ebooks
- resumes
- technical documentation
- reports

---

## Run the Application

```bash
python3 app.py
```

---

## Example Queries

```text
What is DBMS?

Explain normalization.

What are the advantages of DBMS?

What is functional dependency?

Explain 3NF.
```

---

## RAG Pipeline

```text
PDF
 ↓
Text Extraction
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
```

---

## What I Learned

- Fundamentals of Retrieval-Augmented Generation (RAG)
- Vector embeddings and semantic search
- FAISS vector database
- LangChain workflow
- Prompt grounding using retrieved context
- Handling real-world API and dependency issues

---

## Future Improvements

- Streamlit-based UI
- Multi-PDF support
- Persistent vector storage
- Conversational memory
- Web deployment

---

## License

MIT License