from langchain_core.tools import tool
from tavily import TavilyClient
from src.config import settings


tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)

@tool
def web_search_tool(query: str) -> str:
    """
    Search the web for specific recipes, cooking techniques, or unknown ingredients.
    """
    try:
        print(f"    (Searching web for: '{query}'...)")
        response = tavily_client.search(query)
        return response.get("results", [])
    except Exception as e:
        return f"Error performing search: {str(e)}"

@tool
def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """
    Converts cooking units (e.g., grams to cups, Celsius to Fahrenheit).
    Example inputs: 200, 'grams', 'cups' OR 180, 'celsius', 'fahrenheit'.
    """
    print(f"    ( Converting {value} {from_unit} to {to_unit}...)")
    
    
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return f"{value}°C is {(value * 9/5) + 32:.1f}°F"
    
    if from_unit == "grams" and to_unit == "cups":
       
        return f"{value}g is approx {value / 120:.2f} cups (varies by ingredient)"
        
    return f"Conversion from {from_unit} to {to_unit} not supported yet."