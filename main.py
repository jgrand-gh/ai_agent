import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    else:
        print("ERROR: A prompt must be provided as an argument")
        sys.exit(1)

    verbose = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            verbose = True

    # temporary one-item list that will eventually hold the whole conversation
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages)

        if not verbose:
            print(f"{response.text}")
        if verbose:
            print(f"User prompt: {response.text}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    except Exception as e:
        print("Something went wrong with the Gemini API call")
        print(str(e))

if __name__ == "__main__":
    main()