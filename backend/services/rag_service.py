import os
from dotenv import load_dotenv
from groq import AuthenticationError
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from services.qdrant_service import search_jobs

load_dotenv()

llm_api_key = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY") or os.getenv("GEMINIAPIKEY")
if not llm_api_key:
    raise ValueError("Missing Groq API key. Set GROQ_API_KEY or API_KEY in the backend .env file.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=llm_api_key,
    temperature=0.3,
)
rag_prompt=ChatPromptTemplate.from_messages([
    ("system","""You are a job search assistant.
     Use the following job listings retrieved from the database to answer
     if not relevant jobs are found,say so clearly.
     Retrieved Jobs:
     {context}"""),
     ("human","{question}")
     
])

rag_chain = rag_prompt | llm 
def rag_job_search(question:str) -> str:
    results =search_jobs(question ,top_k=5)
    if not results:
        return "No jobs found in the database. Please embed jobs first using the /rag/embed-jobs endpoint."
    context = "\n".join([
        f"-{r['title']}:{r['description']} (Salary:{r['salary']},March: {r['score']})"
        for r in results
    ])

    try:
        response = rag_chain.invoke({"context": context,"question":question})
        return response.content
    except AuthenticationError:
        return "LLM authentication failed: invalid Groq API key. Update GROQ_API_KEY in backend/.env."
    except Exception as e:
        return f"LLM service error: {e}"