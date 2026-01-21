from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver 
from src.tools import web_search_tool, unit_converter
from src.config import settings


SYSTEM_PROMPT = """
You are an Advanced Personal Chef with multi-modal capabilities.
1. VISUAL: If the user sends an image, analyze the ingredients visible in it.
2. MEMORY: Remember the user's allergies, diet, and previous requests.
3. TOOLS: 
   - Use 'unit_converter' if the user asks about measurements.
   - Use 'web_search_tool' for specific recipes you don't know.
"""

def build_agent():
    
    model = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",  
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0.5
    )

    
    tools = [web_search_tool, unit_converter]

   
    memory = MemorySaver()

   
    agent = create_react_agent(
        model=model, 
        tools=tools, 
        prompt=SYSTEM_PROMPT,
        checkpointer=memory
    )
    
    return agent