from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from src.config import PERSIST_DIRECTORY, EMBEDDING_MODEL_NAME

def get_embedding_function():
    """Returns the HuggingFaceEmbeddings function."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

def initialize_vector_db(documents):
    """Initializes and persists the Chroma vector database."""
    embedding_function = get_embedding_function()
    db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=PERSIST_DIRECTORY
    )
    db.persist()
    return db

def get_db_connection():
    """Establishes a connection to an existing Chroma database."""
    embedding_function = get_embedding_function()
    db_connection = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_function
    )
    return db_connection

def retrieve_documents(query, db_connection, k):
    """Performs a similarity search in the vector database."""
    return db_connection.similarity_search(query=query, k=k)