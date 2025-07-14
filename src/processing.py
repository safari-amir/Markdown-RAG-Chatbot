from langchain.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from src.config import MARKDOWN_PATH, HEADERS_TO_SPLIT_ON, CHUNK_SIZE, CHUNK_OVERLAP

def load_document(path=MARKDOWN_PATH):
    """Loads a text document from the specified path."""
    loader = TextLoader(path)
    docs = loader.load()
    return docs[0].page_content

def split_markdown_document(markdown_content):
    """Splits markdown content based on headers."""
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON, strip_headers=False
    )
    return markdown_splitter.split_text(markdown_content)

def split_documents_into_chunks(md_header_splits):
    """Further splits documents into smaller, recursive chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return text_splitter.split_documents(md_header_splits)

def get_processed_documents():
    """Combines all processing steps to get the final document splits."""
    markdown_document = load_document()
    md_header_splits = split_markdown_document(markdown_document)
    splits = split_documents_into_chunks(md_header_splits)
    return splits