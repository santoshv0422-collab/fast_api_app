import os
from dotenv import load_dotenv
from groq import AuthenticationError
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm_api_key = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY") or os.getenv("GEMINIAPIKEY")
if not llm_api_key:
    raise ValueError("Missing Groq API key. Set GROQ_API_KEY or API_KEY in the backend .env file.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=llm_api_key,
    temperature=0.3,
)

resume_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional resume analyser.
Analyse the given resume text and provide:
1. Key Skills found
2.Experience Level(Junior/Mid/Senior)
3.Strengths
4.Areas to Improve
5. Suggested Job Roles
Keep the analysis short and structured.
"""),("human","{resume_text}")])

resume_chain = resume_prompt |llm

def analyse_resume(resume_text:str)-> str:
    try:
        response = resume_chain.invoke({"resume_text":resume_text})
        return response.content
    except AuthenticationError:
        return "LLM authentication failed: invalid Groq API key. Update GROQ_API_KEY in backend/.env."
    except Exception as e:
        return f"LLM service error: {e}"