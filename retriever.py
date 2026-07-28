import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


DATA_PATH = "data"
FAISS_PATH = "faiss_index"


# Load embedding model only one time
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store():

    documents = []

    # Read all PDFs
    for file in os.listdir(DATA_PATH):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(DATA_PATH, file)

            loader = PyPDFLoader(pdf_path)

            documents.extend(loader.load())


    print(f"Loaded {len(documents)} pages")


    # Split documents into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )


    chunks = splitter.split_documents(documents)


    print(f"Created {len(chunks)} chunks")


    # Create FAISS vector database
    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )


    # Save FAISS database
    vectorstore.save_local(FAISS_PATH)


    print("FAISS database created successfully")



def retriever_agent(question):

    # Load existing FAISS database
    vectorstore = FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


    # Search similar documents
    docs = vectorstore.similarity_search(
        question,
        k=3
    )


    # Combine retrieved text
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )


    return context, docs