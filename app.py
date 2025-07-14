import streamlit as st
from src.processing import get_processed_documents
from src.vector_db import initialize_vector_db, get_db_connection, retrieve_documents
from src.llm_model import get_ollama_llm, create_rag_prompt, get_answer_from_llm
from src.config import PERSIST_DIRECTORY, K_SIMILARITY_SEARCH
import os

st.set_page_config(page_title="Markdown Doc Chatbot", layout="wide")
st.title("📚 Markdown Documentation Chatbot")

# --- Initialize or connect to the Vector DB ---
@st.cache_resource
def setup_vector_db():
    """
    Sets up the vector database. It checks if the DB exists,
    otherwise, it processes documents and initializes a new one.
    """
    if not os.path.exists(PERSIST_DIRECTORY):
        with st.spinner("Initializing document embeddings... This might take a moment."):
            splits = get_processed_documents()
            db = initialize_vector_db(splits)
        st.success("Document embeddings initialized and saved!")
    else:
        st.info("Connecting to existing document embeddings.")
        db = get_db_connection()
    return db

db_connection = setup_vector_db()

# --- Initialize LLM and Prompt ---
@st.cache_resource
def setup_llm():
    """Initializes the Ollama LLM."""
    return get_ollama_llm()

llm = setup_llm()
rag_prompt = create_rag_prompt()

# --- Chat Interface ---
st.write("---")
st.header("Ask a Question about Markdown Docs")

# Initialize chat history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_query := st.chat_input("How can I install K3?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Searching for relevant information and generating response..."):
            # 1. Retrieve relevant documents
            docs_sim = retrieve_documents(user_query, db_connection, K_SIMILARITY_SEARCH)
            
            context = ""
            for doc in docs_sim:
                context += doc.page_content + "\n\n" # Add newlines for better separation

            # You can optionally show the retrieved context for debugging/transparency
            # with st.expander("See retrieved context"):
            #     st.markdown(context)

            # 2. Get answer from LLM
            try:
                ai_response = get_answer_from_llm(llm, rag_prompt, user_query, context)
                st.markdown(ai_response)
                # Add assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                st.error(f"An error occurred while communicating with the LLM: {e}")
                st.session_state.messages.append({"role": "assistant", "content": "Sorry, I couldn't process that request. Please try again."})