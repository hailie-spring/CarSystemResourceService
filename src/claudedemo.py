from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
# ANSI color codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"


# Initialize the Anthropic client
client = Anthropic(
    api_key=API_KEY, 
    base_url=BASE_URL, 
    default_headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

def chat_with_claude():
    print("Welcome to the Claude Chatbot!")
    print("Type 'quit' to exit the chat.")
    
    conversation = []
    
    while True:
        user_input = input(f"{BLUE}You: {RESET}")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        print(f"{GREEN}Claude: {RESET}", end="", flush=True)
        
        stream = client.messages.create(
            model=MODEL_NAME,
            max_tokens=1000,
            messages=conversation,
            stream=True
        )
        
        assistant_response = ""
        for chunk in stream:
            if chunk.type == "content_block_delta":
                content = chunk.delta.text
                print(f"{GREEN}{content}{RESET}", end="", flush=True)
                assistant_response += content
        
        print()  # New line after the complete response
        
        conversation.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    chat_with_claude()