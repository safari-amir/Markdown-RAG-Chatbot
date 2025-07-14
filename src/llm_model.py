from langchain_openai import ChatOpenAI  
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from src.config import TEMPERATURE, MAX_TOKENS
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.environ.get("BASE_URL")
MODEL_NAME = os.environ.get("MODEL_NAME")
API_KEY =  os.environ.get("API_KEY")

def get_ollama_llm():
    """Initializes and returns the Ollama LLM."""
    llm = ChatOpenAI(
        base_url=BASE_URL,
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        api_key=API_KEY
    )
    return llm

def create_rag_prompt():
    """Creates and returns the RAG prompt template."""
    prompt_template = """
    You are a highly knowledgeable and concise assistant, specializing exclusively in K3Core documentation.
    Your goal is to provide accurate, brief, and direct answers to user questions based *only* on the provided context.

    Follow these instructions strictly:
    1.  **Focus on K3Core:** Ensure your answer is directly related to K3Core and its functionalities.
    2.  **Conciseness:** Provide the shortest possible answer that is still complete and addresses the user's question fully. Avoid conversational filler or unnecessary introductory/concluding remarks.
    3.  **Accuracy:** Base your answer *strictly* on the information found in the `Context` section. Do not use outside knowledge.
    4.  **Completeness:** Even if concise, the answer must fully address the question.
    5.  **No Hallucinations:** If the `Context` does not contain enough information to answer the question, state clearly that you cannot provide an answer based on the given context. Do not invent information.
    6.  **Formatting (if applicable):** Use bullet points or numbered lists if the answer involves steps or multiple distinct points, to improve readability.

    # Question:
    {query}

    # Context:
    {context}

    # Answer:
    """
    human_prompt = HumanMessagePromptTemplate.from_template(prompt_template)
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
    return chat_prompt

def get_answer_from_llm(llm, prompt, query, context):
    """Invokes the LLM with the given prompt and context."""
    # This prepares the prompt with the actual query and context
    formatted_prompt = prompt.format_messages(query=query, context=context)
    # This sends the formatted messages to the LLM and gets a response
    response = llm.invoke(formatted_prompt)
    return response.content