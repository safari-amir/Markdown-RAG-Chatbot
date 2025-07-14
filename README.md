
# 📚 AI-Powered Document Chatbot
<img width="1863" height="734" alt="image" src="https://github.com/user-attachments/assets/23fa8107-169c-4dc5-8bc8-25cc44be6a97" />

## Overview

This project provides an intelligent chatbot capable of answering questions directly from your Markdown documentation using **Retrieval Augmented Generation (RAG)**. It's designed to make information retrieval from technical documents, personal notes, or any text-heavy Markdown content quick and efficient, enhancing accessibility and user experience.

Leveraging state-of-the-art Natural Language Processing and Large Language Models, this bot transforms static documentation into an interactive knowledge base.

## Features

* **Intelligent Q&A:** Ask natural language questions and get concise, accurate answers from your provided Markdown files.
* **Retrieval Augmented Generation (RAG):** Combines information retrieval with generative AI to ensure answers are grounded in your specific documentation.
* **Modular Architecture:** Clean, organized codebase for easy maintenance and extension.
* **User-Friendly Interface:** Built with Streamlit for an interactive web application experience.
* **Flexible Document Handling:** Easily adaptable to different Markdown file structures.
* **Local LLM Support (Ollama):** Supports local large language models (e.g., Code Llama) via Ollama, ensuring data privacy and reducing API costs. (Note: Can be configured for OpenAI or other APIs).

## Technologies Used

* **Python:** The core programming language.
* **LangChain:** For orchestrating LLM interactions, document loading, splitting, and vector store management.
* **Streamlit:** For creating the interactive web user interface.
* **ChromaDB:** A lightweight, in-memory vector database used for storing and retrieving document embeddings.
* **HuggingFace Embeddings (BAAI/bge-large-en-v1.5):** For generating high-quality document embeddings.
* **Ollama / OpenAI:** For running the Large Language Models (LLMs).
* **`python-dotenv`:** For secure management of environment variables (e.g., API keys).

## Project Structure

The project is structured for clarity and modularity:

```

.
├── src/
│   ├── data/                 \# Placeholder for your Markdown document(s)
│   │   └── FINAL.md          \# Example Markdown file
│   ├── config.py             \# Global configuration settings
│   ├── llm_model.py          \# LLM initialization and prompt handling
│   ├── processing.py         \# Document loading, splitting, and chunking
│   ├── vector_db.py          \# ChromaDB initialization and interaction
│   └── **init**.py           \# Makes 'src' a Python package
├── app.py                    \# The main Streamlit application entry point
├── .env.example              \# Example environment variables file
├── .gitignore                \# Specifies intentionally untracked files to ignore
├── LICENSE                   \# Project license (e.g., MIT, Apache 2.0)
└── README.md                 \# This README file

````

## Getting Started

Follow these steps to set up and run the chatbot locally.

### Prerequisites

* Python 3.8+
* Git (for cloning the repository)
* **Ollama (Optional, for local LLM):** Download and install Ollama from [ollama.ai](https://ollama.ai/). Then, pull the desired model (e.g., `codellama:7b`).
    ```bash
    ollama pull codellama:7b
    ```

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd your-repo-name
    ```
    (Replace `YourUsername` and `your-repo-name` with your actual GitHub details)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *If you don't have `requirements.txt`, create one first by running:*
    ```bash
    pip freeze > requirements.txt
    # Then install:
    # pip install -r requirements.txt
    ```

### Configuration

1.  **Place your Markdown file(s):**
    Put your `FINAL.md` (or any other Markdown file you wish to use) inside the `src/data/` directory. Update `src/config.py` if your file path or name changes.

2.  **Set up environment variables:**
    Create a file named `.env` in the root directory of your project (same level as `app.py`). This file will store sensitive information like API keys.

    ```bash
    # .env
    # Example for OpenAI API key (if you use OpenAI instead of Ollama)
    # OPENAI_API_KEY="sk-your-openai-api-key-here"

    # You can add other variables here if needed
    ```
    **Remember to add `.env` to your `.gitignore` file to prevent it from being committed to version control!**

### Running the Application

1.  **Ensure Ollama is running (if using local LLM):**
    Open a terminal and start Ollama (it usually runs in the background after installation) or ensure your chosen model is pulled.

2.  **Run the Streamlit application:**
    From the project's root directory, execute:
    ```bash
    streamlit run app.py
    ```

    This will open the application in your default web browser (usually at `http://localhost:8501`).

## How it Works (Brief Technical Overview)

1.  **Document Loading:** Your Markdown file is loaded.
2.  **Document Splitting:** The Markdown content is first split by headers (e.g., #, ##) to preserve semantic structure, and then further broken down into smaller, overlapping chunks suitable for embedding.
3.  **Embedding Generation:** Each text chunk is converted into a numerical vector (embedding) using a pre-trained embedding model.
4.  **Vector Store (ChromaDB):** These embeddings are stored in a local ChromaDB instance, allowing for efficient similarity search.
5.  **Query Processing:** When a user asks a question, the query is also embedded.
6.  **Context Retrieval:** The most similar document chunks from the vector store are retrieved based on the query's embedding.
7.  **Answer Generation:** The retrieved context, along with the user's question, is sent to a Large Language Model (LLM). The LLM then generates a concise and accurate answer, grounded in the provided context.

## Contribution

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

