import litellm
import csv
import datetime
from data import EXPERIMENT_DATA

# --- Configuration ---
# LiteLLM model parameters (https://docs.litellm.ai/docs/providers)
MODEL_NAME = "gpt-4o-mini"  # Example: "ollama/gemma", "gpt-3.5-turbo"
# To use OpenAI models, ensure your OPENAI_API_KEY environment variable is set.
# For Ollama, ensure Ollama is running and the model is pulled (e.g., `ollama pull gemma`)

# Other parameters for litellm.completion can be added here if needed
# e.g., temperature, max_tokens
LITELLM_PARAMS = {
    "temperature": 0.3,
    "max_tokens": 250
}

OUTPUT_CSV_FILE = f"experiment_results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# --- Prompt Definitions ---
# The user specified 3 prompt types, but referred to them as "4 ways".
# Assuming it was a typo and proceeding with the 3 detailed prompt structures.

PROMPT_TYPES = {
    "simple_question": {
        "template": "{document}\n---\n{question}",
        "description": "Simple question: Document, then question."
    },
    "grounding": {
        "template": "{document}\n---\nPlease answer the following question according to the document above:\n{question}",
        "description": "Grounding: Instructs LLM to use only the document."
    },
    "grounding_idk": {
        "template": "{document}\n---\nPlease answer the following question according to the document above. If the document above does not answer the question, please reply 'The document does not provide an answer.':\n{question}",
        "description": "Grounding + IDK: Instructs LLM to use document and say 'I don't know' if answer not present."
    }
}

def get_llm_response(model_name: str, prompt_text: str, params: dict) -> str:
    """
    Sends a prompt to the specified LLM using litellm and returns the response.
    """
    try:
        messages = [{"role": "user", "content": prompt_text}]
        response = litellm.completion(model=model_name, messages=messages, **params)
        # Assuming the response structure provides content in choice's message
        content = response.choices[0].message.content.strip()
        return content
    except Exception as e:
        print(f"Error getting LLM response for model {model_name}: {e}")
        return f"Error: {e}"

def run_experiment():
    """
    Runs the LLM truth experiment.
    - Loops through documents and questions from data.py.
    - Constructs prompts based on defined types.
    - Gets LLM responses.
    - Saves results to a CSV file.
    """
    results = []
    print(f"Starting experiment. Results will be saved to: {OUTPUT_CSV_FILE}")
    print(f"Using model: {MODEL_NAME} with params: {LITELLM_PARAMS}")

    for doc_idx, doc_item in enumerate(EXPERIMENT_DATA):
        document_id = doc_item["id"]
        document_text = doc_item["document"]
        print(f"\nProcessing Document ID: {document_id} ({doc_idx+1}/{len(EXPERIMENT_DATA)})")

        for q_idx, qa_pair in enumerate(doc_item["qa_pairs"]):
            question_id = qa_pair["id"]
            question_text = qa_pair["question"]
            # We don't use qa_pair["answer"] in this script, it's for later analysis
            print(f"  Processing Question ID: {question_id} ({q_idx+1}/{len(doc_item['qa_pairs'])}) - '{question_text[:50]}...'")

            for prompt_key, prompt_info in PROMPT_TYPES.items():
                prompt_full_text = prompt_info["template"].format(document=document_text, question=question_text)

                print(f"    Prompt Type: {prompt_key}...")
                llm_answer = get_llm_response(MODEL_NAME, prompt_full_text, LITELLM_PARAMS)
                print(f"      LLM Response: {llm_answer[:100]}...") # Log a snippet

                results.append({
                    "document_id": document_id,
                    "doc_index": doc_idx,
                    "question_id": question_id,
                    "q_index": q_idx,
                    "prompt_type": prompt_key,
                    "prompt_description": prompt_info["description"],
                    "full_prompt_text": prompt_full_text, # Optional: for detailed review
                    "llm_response": llm_answer
                })

    # Save results to CSV
    if results:
        fieldnames = results[0].keys()
        with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"\nExperiment finished. {len(results)} responses saved to {OUTPUT_CSV_FILE}")
    else:
        print("No results to save.")

if __name__ == "__main__":
    # Basic check for data
    if not EXPERIMENT_DATA:
        print("No experiment data found in data.py. Please add some data to proceed.")
    else:
        run_experiment()
        # Example: How to check your OpenAI environment variable (optional)
        # import os
        # if "gpt" in MODEL_NAME and not os.getenv("OPENAI_API_KEY"):
        #     print("\nWarning: OPENAI_API_KEY environment variable is not set. OpenAI models will fail.")
        # if "ollama" in MODEL_NAME:
        #     print("\nReminder: Ensure Ollama is running and the model (e.g., 'ollama pull gemma') is available.")
