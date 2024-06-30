from transformers import GPT2Tokenizer

def tokenize(prompt):
    # tokenize with GPT2 (publicly available)
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokens = tokenizer.encode(prompt, add_special_tokens=False)  # add_special_tokens=False to exclude special tokens like [CLS], [SEP]

    return len(tokens)

# Initialize variables to track total kWh, water, bags, and feet driven per model
overall_cost = 0
overall_water = 0
overall_bag = 0
overall_feet = 0

overall_mistral_cost = 0
overall_mistral_water = 0
overall_mistral_bag = 0
overall_mistral_feet = 0

overall_gpt4_cost = 0
overall_gpt4_water = 0
overall_gpt4_bag = 0
overall_gpt4_feet = 0

overall_google_cost = 0
overall_google_water = 0
overall_google_bag = 0
overall_google_feet = 0

def calculate_energy_out(prompt):
    # get token count
    tok_count = tokenize(prompt)

    # current kWh consumed
    current_mistral_cost = 0.0001 * tok_count # assumption: mistral 1% size of GPT-4, safe to assume ~4x more energy efficient
    current_gpt4_cost = 0.000375 * tok_count # assumption: gpt4 is 25x more expensive than google on an avg query (~200 tokens), therefore this is the cost
    current_google_cost = 0.0003 * tok_count

    # PER LITER OF WATER CONSUMPTION
    # The national weighted average for thermoelectric and hydroelectric water use is 7.6  of evaporated water per kWh of electricity consumed at the point of end use. 
    current_mistral_water = current_mistral_cost * 7.6 
    current_gpt4_water = current_gpt4_cost * 7.6
    current_google_water = current_google_cost * 7.6

    # PER PLASTIC BAG
    # production of plastic bag generates ~200g of CO2, which converts to 0.966 kWh of emissions
    current_mistral_bag = current_mistral_cost / 0.966
    current_gpt4_bag = current_gpt4_cost / 0.966
    current_google_bag = current_google_cost / 0.966

    # PER FEET ELECTRIC CAR DRIVEN
    # convert to miles in electric car: 0.35kWh per mi
    # source: https://diminishedvaluecarolina.com/how-much-electricity-does-an-electric-car-consume#:~:text=Calculating%20Energy%20Consumption&text=Conversely%2C%20an%20inefficient%20EV%20using,month%20for%20the%20average%20driver.
    current_mistral_feet = (current_mistral_cost * 5280) / 0.35
    current_gpt4_feet = (current_gpt4_cost * 5280) / 0.35
    current_google_feet = (current_google_cost * 5280) / 0.35

    return {
        "mistral": {
            "cost": current_mistral_cost,
            "water": current_mistral_water,
            "bag": current_mistral_bag,
            "feet": current_mistral_feet
        },
        "gpt4": {
            "cost": current_gpt4_cost,
            "water": current_gpt4_water,
            "bag": current_gpt4_bag,
            "feet": current_gpt4_feet
        },
        "google": {
            "cost": current_google_cost,
            "water": current_google_water,
            "bag": current_google_bag,
            "feet": current_google_feet
        }
    }

def update_overall(model, results):
    global overall_cost, overall_water, overall_bag, overall_feet
    global overall_mistral_cost, overall_mistral_water, overall_mistral_bag, overall_mistral_feet
    global overall_gpt4_cost, overall_gpt4_water, overall_gpt4_bag, overall_gpt4_feet
    global overall_google_cost, overall_google_water, overall_google_bag, overall_google_feet

    if model == "mistral":
        overall_mistral_cost += results['mistral']['cost']
        overall_mistral_water += results['mistral']['water']
        overall_mistral_bag += results['mistral']['bag']
        overall_mistral_feet += results['mistral']['feet']
         
        overall_cost += results['mistral']['cost']
        overall_water += results['mistral']['water']
        overall_bag += results['mistral']['bag']
        overall_feet += results['mistral']['feet']
    
    elif model == "gpt4":
        overall_gpt4_cost += results['gpt4']['cost']
        overall_gpt4_water += results['gpt4']['water'] 
        overall_gpt4_bag += results['gpt4']['bag']
        overall_gpt4_feet += results['gpt4']['feet']

        overall_cost += results['gpt4']['cost']
        overall_water += results['gpt4']['water']
        overall_bag += results['gpt4']['bag']
        overall_feet += results['gpt4']['feet']
    
    elif model == "google":
        overall_google_cost += results['google']['cost']
        overall_google_water += results['google']['water'] 
        overall_google_bag += results['google']['bag']
        overall_google_feet += results['google']['feet']
        
        overall_cost += results['google']['cost']
        overall_water += results['google']['water']
        overall_bag += results['google']['bag']
        overall_feet += results['google']['feet']

if __name__ == "__main__":
    while True:
        # Get user input
        # THIS WILL CHANGE BASED ON INPUT FROM OTHER FUNCTION
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        model = input("Enter the model (mistral, gpt4, google): ").lower()

        current_results = calculate_energy_out(prompt)

        # Set model flags based on user input
        mistral = model == "mistral"
        gpt4 = model == "gpt4"
        google = model == "google"

        if mistral:
            update_overall("mistral", current_results)
        elif gpt4:
            update_overall("gpt4", current_results)
        elif google:
            update_overall("google", current_results)
        else:
            print("Invalid model. Please enter 'mistral', 'gpt4', or 'google'.")
            continue

        comprehensive_results = [overall_cost, overall_water, overall_bag, overall_feet]

        print("Results for current prompt:", current_results)
        print("Comprehensive Results:", comprehensive_results)
        print("Overall Mistral:", {
            "cost": overall_mistral_cost,
            "water": overall_mistral_water,
            "bag": overall_mistral_bag,
            "feet": overall_mistral_feet
        })
        print("Overall GPT-4:", {
            "cost": overall_gpt4_cost,
            "water": overall_gpt4_water,
            "bag": overall_gpt4_bag,
            "feet": overall_gpt4_feet
        })
        print("Overall Google:", {
            "cost": overall_google_cost,
            "water": overall_google_water,
            "bag": overall_google_bag,
            "feet": overall_google_feet
        })
