import os
import sys
from dotenv import load_dotenv
from google import genai




def main():

    #if len(sys.argv) < 2:
    #    print("Usage: uv run main.py [your prompt here]")
    #    sys.exit(1)

    #user_prompt = sys.argv[1]

    print("Hello from py-aigent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    #'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    response = client.models.generate_content(model='gemini-2.5-flash', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.') #user_prompt)
    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
