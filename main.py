import sys
import base64
from langchain_core.messages import HumanMessage
from src.agent import build_agent


def encode_image(image_path):
    """Converts local image file to base64 string for Gemini."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        return None


def get_clean_text(message):
    """Safely extracts text from Gemini's complex list response."""
    content = message.content
    

    if isinstance(content, list):
        return "".join([block.get("text", "") for block in content if "text" in block]).strip()
    
   
    return str(content).strip()

def main():
    print(" Advanced AI Chef is Ready! (Memory + Vision + Tools)")
    print("-------------------------------------------------------")
    print("Commands:")
    print(" - Type ingredients (e.g., 'chicken and rice')")
    print(" - Send Photo: 'image <filename>' (e.g., 'image fridge.jpg')")
    print(" - Quit: 'q'")

    agent = build_agent()
    
    config = {"configurable": {"thread_id": "session_user_1"}}

    while True:
        user_input = input("\nUser > ")
        if user_input.lower() in ["q", "quit"]:
            break
            
        message_content = []

        if user_input.startswith("image "):
            image_path = user_input.replace("image ", "").strip()
            base64_img = encode_image(image_path)
            
            if base64_img:
                print(f"   (Loading image: {image_path}...)")
                message_content = [
                    {"type": "text", "text": "Analyze this image and suggest recipes based on what you see."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}
                    }
                ]
            else:
                print(f" Error: File '{image_path}' not found.")
                continue
        else:
            
            message_content = user_input

       
        try:
            
            result = agent.invoke(
                {"messages": [HumanMessage(content=message_content)]},
                config=config
            )
            
            
            last_message = result["messages"][-1]
            clean_response = get_clean_text(last_message)
            
            print("\n Chef:")
            print(clean_response)
            
        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()