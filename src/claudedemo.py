from anthropic import Anthropic
from dotenv import load_dotenv


# ANSI color codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQUktMTc3MDM0NzQ1MDg5NCIsInJvbGVzIjpbIjM1Il0sInVzZXJfaWQiOjE3NTQsInVzZXJuYW1lIjoiaGFpbGllX2Nob3UiLCJyb2xlX25hbWVzIjpbIlJPUC1haWVuZHBvaW50LVVzZXIiXSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsImV4cCI6MTc3ODEyMzQ1NCwianRpIjoiNzJhMzdiNTYtMDMwOS0xMWYxLTkxMjgtNjIxOTg5YjUxZjJlIiwidmVyc2lvbiI6IjIwMjQtMTEtMDEifQ.36T3zcKjB33jQ6e2Fa22sBf4OAwv-tJbC0PcmxKugxs"
MODEL_NAME = "claude-3.5-haiku"
BASE_URL= "https://api.rdsec.trendmicro.com/prod/aiendpoint"

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