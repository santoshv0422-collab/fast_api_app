import os
from dotenv import load_dotenv
from groq import AuthenticationError
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

llm_api_key = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY") or os.getenv("GEMINIAPIKEY")
if not llm_api_key:
    raise ValueError("Missing Groq API key. Set GROQ_API_KEY or API_KEY in the backend .env file.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=llm_api_key,
    temperature=0.7,
)

prompt_with_memory = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant"),
    ("placeholder", "{chat_history}"),
    ("human", "{user_query}")
])

chain_with_memory = prompt_with_memory | llm

store={}

def get_history(session_id: str):
    if session_id not in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]

chat_with_memory=RunnableWithMessageHistory(
    runnable=chain_with_memory,
    get_session_history=get_history,
    input_messages_key="user_query",
    message_history="chat_history"
)
def ask_career_advice(session_id: str, user_query: str):
    try:
        response = chat_with_memory.invoke(
            {"user_query": user_query},
            {"configurable": {"session_id": session_id}}
        )
        return response.content
    except AuthenticationError:
        return "LLM authentication failed: invalid Groq API key. Update GROQ_API_KEY in backend/.env."
    except Exception as e:
        return f"LLM service error: {e}"