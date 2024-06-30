import os
import sys
sys.path.append('/Users/thomazbonato/Desktop/Personal/Summer24/Coding/Azalea/backend/utils')

import scorer
import energy_calc

def normalize_cost(cost, max_cost=50):
    return (max_cost - cost) / max_cost  # Returns a value between 0 and 1

def get_model_score(relative_cost, complexity, model):
    # Adjust weights based on complexity
    if complexity <= 2:
        cost_weight = 0.7
        complexity_weight = 0.3
    elif complexity <= 4:
        cost_weight = 0.6
        complexity_weight = 0.4
    else:
        cost_weight = 0.5
        complexity_weight = 0.5

    # Normalize the relative cost
    normalized_cost = normalize_cost(relative_cost)

    # Adjust score based on model and complexity
    if model == "google":
        if complexity <= 2:
            complexity_score = 1.0
        elif complexity <= 4:
            complexity_score = 0.5
        else:
            complexity_score = 0.2
    elif model == "mistral":
        if complexity <= 2:
            complexity_score = 0.5
        elif complexity <= 4:
            complexity_score = 1.0
        else:
            complexity_score = 0.7
    else:  # chatgpt
        if complexity <= 2:
            complexity_score = 0.2
        elif complexity <= 4:
            complexity_score = 0.7
        else:
            complexity_score = 1.0

    # Calculate weighted score
    score = (normalized_cost * cost_weight) + (complexity_score * complexity_weight)
    return score * 6  # Scale to 0-6 range

def calculate_relative_costs(energy_results):
    total_cost = sum(energy_results[model]["cost"] for model in energy_results)
    
    if total_cost == 0:
        return {model: 0 for model in energy_results}
    
    return {model: energy_results[model]["cost"] / total_cost for model in energy_results}

def recommend_model_with_complexity_and_count(prompt, complexity):
    # Calculate energy consumption for the current prompt
    energy_results = energy_calc.calculate_energy_out(prompt)

    # Calculate relative costs
    relative_costs = calculate_relative_costs(energy_results)

    # Calculate scores for each model
    mistral_score = get_model_score(relative_costs["mistral"], complexity, "mistral")
    chatgpt_score = get_model_score(relative_costs["chatgpt"], complexity, "chatgpt")
    google_score = get_model_score(relative_costs["google"], complexity, "google")


    return {
        "complexity" : complexity,
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

        complexity = float(input("Enter complexity (1-6): "))
        recommendation = recommend_model_with_complexity_and_count(prompt, complexity)
        print(f"Recommendation: {recommendation}")