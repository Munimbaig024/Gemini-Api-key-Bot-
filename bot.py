import os
from google import genai
from google.genai.errors import APIError

# --- IMPORTANT: Direct Key Access ---
# This line initializes the client directly using the API key you provided.
# NOTE: Replace 'YOUR_API_KEY_HERE' if you change your key later.
# For security, storing keys in a file is usually discouraged, but this is the fastest way to test.
client = genai.Client(api_key="API_KEY_HERE")

def generate_educational_content(prompt_text: str):
    """
    Sends a prompt to the Gemini model using the pre-initialized client
    and prints the generated text.

    Args:
        prompt_text: The query or instruction to send to the model.
    """
    # Using the fast, general-purpose model
    model_name = "gemini-2.5-flash"
    print(f"--- Sending request to Model: {model_name} ---")
    print(f"Prompt: {prompt_text}\n")

    try:
        # Call the API to generate content
        response = client.models.generate_content(
            model=model_name,
            contents=prompt_text
        )

        print("--- Generated Response ---")
        print(response.text)
        print("\n" + "="*50)

    except APIError as e:
        # This error often means the key is invalid or rate limits were hit
        print(f"An API Error occurred: {e}")
        print("ACTION REQUIRED: Please double-check your API key or check your quota.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # --- Example Educational Prompt ---
    educational_prompt = (
        "Explain the concept of 'Net Present Value' (NPV) in finance using a "
        "simple, real-world example suitable for a high school student."
    )

    generate_educational_content(educational_prompt)

    # --- Another Example ---
    creative_prompt = "Write a short, four-line poem about the Python programming language."
    generate_educational_content(creative_prompt)