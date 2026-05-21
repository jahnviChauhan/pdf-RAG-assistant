from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI


# STEP 1 — LOAD PDF
loader = PyPDFLoader("data.pdf")
documents = loader.load()

print("PDF Loaded Successfully")

# STEP 2 — SPLIT INTO CHUNK
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

# STEP 3 — CREATE EMBEDDINGS
embeddings = OpenAIEmbeddings()

# STEP 4 — STORE IN VECTOR DATABASE
db = FAISS.from_documents(chunks, embeddings)

print("Vector Database Created")

# STEP 5 — USER QUESTION
query = input("Ask a question: ")

# STEP 6 — RETRIEVE RELEVANT CHUNKS
results = db.similarity_search(query)

print("\nRetrieved Chunks:\n")

for r in results:
    print(r.page_content)
    print("\n" + "="*50 + "\n")

# STEP 7 — CREATE CONTEXT
context = "\n".join([r.page_content for r in results])

# STEP 8 — LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

print("\nFINAL ANSWER:\n")
print(response.content)

