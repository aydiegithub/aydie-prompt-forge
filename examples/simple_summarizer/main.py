import aydie_prompt_forge
from pathlib import Path

# --- Configuration ---
# Define the path to your prompt repository.
# Using Path from pathlib makes path handling more robust.
PROMPT_FILE = Path(__file__).parent / "prompts.yml"

def demonstrate_summarizer():
    """
    Demonstrates loading and using the summarization prompt.
    """
    print("--- Running Summarizer Demonstration ---")
    
    # 1. Load the entire repository from the file.
    # This is the main entry point of the prompt-forge library.
    repo = aydie_prompt_forge.load(PROMPT_FILE)
    print(f"Repository '{PROMPT_FILE.name}' loaded successfully!")
    
    # 2. Get a specific prompt by its unique ID.
    # The .get() method returns None if the ID is not found.
    prompt_id = "summarize_article_v1.1"
    summarize_prompt = repo.get(prompt_id=prompt_id)
    
    if summarize_prompt:
        # 3. Prepare your dynamic data.
        long_article = (
            "Generative AI is a type of artificial intelligence technology that "
            "can produce various types of content, including text, imagery, "
            "audio, and synthetic data. It has seen rapid advancements and is "
            "being adopted across numerous industries for tasks like content "
            "creation, code generation, and data augmentation."
        )
        
        # 4. Fill the prompt template with your data using the .fill() method.
        final_prompt = summarize_prompt.fill(article_text=long_article)
        
        # The final_prompt is now a complete string, ready to be sent to an LLM API.
        print(f"\nSuccessfully prepared prompt for ID: '{prompt_id}'")
        print("\n--- Generated Prompt ---")
        print(final_prompt)
        print("--------------------------")
        
        # You can also easily access the metadata defined in the YAML file.
        print("\n--- Associated Metadata ---")
        print(f"Author: {summarize_prompt.author}")
        print(f"Version: {summarize_prompt.version}")
        print(f"Model parameters to use: {summarize_prompt.model_parameters}")
        print("--------------------------")
        
    else:
        print(f"Error: Prompt with ID '{prompt_id}' not found in the repository.")

def main():
    """
    Main function to run the demostation.
    """
    try:
        demonstrate_summarizer()
    except aydie_prompt_forge.AydieException as e:
        # This will catch any custom errors from our library,
        # such as InvalidPromptFileError.
        print(f"An error occured with Prompt-Forge: {e}")
    except FileNotFoundError:
        print(f"Error: The prompt file '{PROMPT_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    main()