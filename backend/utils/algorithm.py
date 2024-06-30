import os
import sys
from transformers import GPT2Tokenizer
import scorer
import energy_calc

# Add the path to the utils folder
sys.path.append("/Users/thomazbonato/Desktop/Personal/Summer24/Coding/Azalea/backend/utils")

# Initialize tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Initialize prompt count (hardcoded for now)
prompt_count = 1

def calculate_scores(prompt, model):
    global prompt_count

    # Calculate energy metrics using energy_calc.py
    energy_metrics = energy_calc.calculate_energy_out(prompt)

    # Calculate complexity using scorer.py
    complexity_score = scorer.get_complexity_score(prompt)

    # Get current cost from energy metrics
    current_cost = energy_metrics[model]['cost']

    # Weights for the algorithm
    environmental_weight = 1.0
    complexity_weight = 1.0
    chat_history_weight = 1.0

    # Adjust weights based on prompt count
    if prompt_count == 1:
        environmental_weight = 1.5
        complexity_weight = 1.0
        chat_history_weight = 0.5
    elif prompt_count > 1:
        environmental_weight = 1.0
        complexity_weight = 1.0
        chat_history_weight = 1.5

    # Calculate final score
    final_score = (environmental_weight * current_cost +
                   complexity_weight * complexity_score +
                   chat_history_weight * prompt_count)

    # Update prompt count for the next run
    prompt_count += 1

    return final_score, energy_metrics, complexity_score

if __name__ == "__main__":
    while True:
        # Get user input
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        model = input("Enter the model (mistral, gpt4, google): ").lower()

        # Validate model input
        if model not in ["mistral", "gpt4", "google"]:
            print("Invalid model. Please enter 'mistral', 'gpt4', or 'google'.")
            continue

        # Calculate scores
        final_score, energy_metrics, complexity_score = calculate_scores(prompt, model)

        print(f"Model: {model}")
        print(f"Environmental Metrics: {energy_metrics[model]}")
        print(f"Complexity Score: {complexity_score}")
        print(f"Final Score: {final_score}")

        # Print overall results
        print("Comprehensive Results:", [energy_calc.overall_cost, energy_calc.overall_water, energy_calc.overall_bag, energy_calc.overall_feet])
        print("Overall Mistral:", {
            "cost": energy_calc.overall_mistral_cost,
            "water": energy_calc.overall_mistral_water,
            "bag": energy_calc.overall_mistral_bag,
            "feet": energy_calc.overall_mistral_feet
        })
        print("Overall GPT-4:", {
            "cost": energy_calc.overall_gpt4_cost,
            "water": energy_calc.overall_gpt4_water,
            "bag": energy_calc.overall_gpt4_bag,
            "feet": energy_calc.overall_gpt4_feet
        })
        print("Overall Google:", {
            "cost": energy_calc.overall_google_cost,
            "water": energy_calc.overall_google_water,
            "bag": energy_calc.overall_google_bag,
            "feet": energy_calc.overall_google_feet
        })
