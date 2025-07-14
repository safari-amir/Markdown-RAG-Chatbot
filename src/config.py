MARKDOWN_PATH = "/home/amir/Work/agent/My-Project/Markdown-RAG-Chatbot/src/data/FINAL.md"
EMBEDDING_MODEL_NAME = "BAAI/bge-large-en-v1.5"
PERSIST_DIRECTORY = "./Markdown_embedding_db"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
K_SIMILARITY_SEARCH = 5
TEMPERATURE = 0.1
MAX_TOKENS = 200

HEADERS_TO_SPLIT_ON = [
    ("#", "Section"),
    ("##", "Subsection"),
    ("###", "Subsubsection"),
]