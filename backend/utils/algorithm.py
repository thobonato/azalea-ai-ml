import os
import sys

sys.path.append('/Users/thomazbonato/Desktop/Personal/Summer24/Coding/Azalea/backend/utils')

import scorer
import energy_calc

def get_model_score(relative_cost, complexity, prompt_count, scaling_factor=5):
    # Weighting factors (can be adjusted based on requirements)
    cost_weight = 0.5
    complexity_weight = 0.3
    prompt_count_weight = 0.2

    # Example dynamic weighting adjustment
    if prompt_count > 1:
        cost_weight -= 0.1
        prompt_count_weight += 0.1

    if complexity > 1:
        complexity_weight += 0.1
        cost_weight -= 0.1

    # Scale the relative cost
    scaled_cost = relative_cost * scaling_factor

    # Calculate weighted score
    score = (scaled_cost * cost_weight) + (complexity * complexity_weight) + (prompt_count * prompt_count_weight)
    return score

def calculate_relative_costs(energy_results):
    # Calculate relative costs
    total_cost = (energy_results["chatgpt"]["cost"] + 
                  energy_results["google"]["cost"] + 
                  energy_results["mistral"]["cost"])

    if total_cost == 0:
        relative_cost_chatgpt = relative_cost_google = relative_cost_mistral = 0
    else:
        relative_cost_chatgpt = 1 - (energy_results["chatgpt"]["cost"] / total_cost)
        relative_cost_google = 1 - (energy_results["google"]["cost"] / total_cost)
        relative_cost_mistral = 1 - (energy_results["mistral"]["cost"] / total_cost)

    return relative_cost_mistral, relative_cost_chatgpt, relative_cost_google

def recommend_model_with_complexity_and_count(prompt, complexity, prompt_count):
    # Calculate energy consumption for the current prompt
    energy_results = energy_calc.calculate_energy_out(prompt)

    # Calculate relative costs
    relative_cost_mistral, relative_cost_chatgpt, relative_cost_google = calculate_relative_costs(energy_results)

    # Calculate scores for each model
    mistral_score = get_model_score(relative_cost_mistral, complexity, prompt_count)
    chatgpt_score = get_model_score(relative_cost_chatgpt, complexity, prompt_count)
    google_score = get_model_score(relative_cost_google, complexity, prompt_count)

    return {
        "mistral": {
            "score": mistral_score,
            "cost": energy_results["mistral"]["cost"],
            "water": energy_results["mistral"]["water"],
            "bag": energy_results["mistral"]["bag"],
            "feet": energy_results["mistral"]["feet"]
        },
        "chatgpt": {
            "score": chatgpt_score,
            "cost": energy_results["chatgpt"]["cost"],
            "water": energy_results["chatgpt"]["water"],
            "bag": energy_results["chatgpt"]["bag"],
            "feet": energy_results["chatgpt"]["feet"]
        },
        "google": {
            "score": google_score,
            "cost": energy_results["google"]["cost"],
            "water": energy_results["google"]["water"],
            "bag": energy_results["google"]["bag"],
            "feet": energy_results["google"]["feet"]
        }
    }

if __name__ == "__main__":
    while True:
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break

        prompt_count = 0
        complexity_score = 4

        # Calculate energy consumption
        energy_results = energy_calc.calculate_energy_out(prompt)

        
        recommendation = recommend_model_with_complexity_and_count(prompt, complexity_score, prompt_count)
        print(f"Recommendation: {recommendation}")
