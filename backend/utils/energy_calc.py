from transformers import GPT2Tokenizer

def tokenize(prompt):
    # tokenize with GPT2 (publicly available)
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokens = tokenizer.encode(prompt, add_special_tokens=False)  # add_special_tokens=False to exclude special tokens like [CLS], [SEP]

    return len(tokens)



# Per conversation of about 20 to 50 queries, half a litre of water evaporates – a small bottle, in other words.
# source: https://www.brusselstimes.com/1042696/chatgpt-consumes-25-times-more-energy-than-google

# assumption of inference costs:
#   mistral: 0.05 kWh     per 1k tokens
#   gpt4o: 0.2 kWh        per 1k tokens
#   google: 0.0003 kWh    per query  # 
    # source: https://www.nytimes.com/2011/09/09/technology/google-details-and-defends-its-use-of-electricity.html#:~:text=Google%20also%20released%20an%20estimate,be%20difficult%20to%20understand%20intuitively.
    
def calculate_energy_out(prompt):

    # per tok cost and google
    mistral_cost = 0.00001  # assumption: mistral 1% size of GPT-4, safe to assume ~4x more energy efficient
    gpt4_cost = 0.000375   # assumption: gpt4 is 25x more expensive than google on an avg query (~200 tokens), therefore this is the cost
    google_cost = 0.0003

    # convert to miles in electric car: 0.35kWh per mi
    # source: https://diminishedvaluecarolina.com/how-much-electricity-does-an-electric-car-consume#:~:text=Calculating%20Energy%20Consumption&text=Conversely%2C%20an%20inefficient%20EV%20using,month%20for%20the%20average%20driver.
    kWh_per_ft = 0.35 / 5280
    
    # in mls per 1,000 toks
    mistral_water = 3.58   # assuming 4x more efficient than gpt4
    gpt4_water = 14.3
    google_water = 0.572
    
    # get tok count
    tok_count = tokenize(prompt)

    # COMPARE TO RECYCLING: plastic bags
    # production of plastic bag generates ~200g of CO2

    # calc total cost
    mistral_cost *= tok_count
    gpt4_cost *= tok_count
    mistral_water *= tok_count
    gpt4_water *= tok_count

    # get winner
    if mistral_cost < gpt4_cost and mistral_cost < google_cost:
        best_route = "mistral"
    else:
        best_route = "google"

    return {"response_kWh" : {"mistral" : mistral_cost,
                          "gpt-4" : gpt4_cost,
                          "google" : google_cost,
                          "winner": best_route},
            "response_ft" : {"mistral" : mistral_cost/kWh_per_ft,
                          "gpt-4" : gpt4_cost/kWh_per_ft,
                          "google" : google_cost/kWh_per_ft},
            "response_ml" : {"mistral" : mistral_water,
                          "gpt-4" : gpt4_water,
                          "google" : google_water}}

if __name__ == "__main__":
    print(calculate_energy_out("Ok this is the information I get from my function, but I want it to somehow draw a parallel to recycling. In what ways could I make it more tangible for the user?Ok this is the information I get from my function, but I want it to somehow draw a parallel to recycling. In what ways could I make it more tangible for the user?Ok this is the information I get from my function, but I want it to somehow draw a parallel to recycling. In what ways could I make it more tangible for the user?"))

    
    
    # Avg CO2 Emissions from Energy Usage:
    # 0.42kg of cO2 per kWh
    # Avg CO2 Emissions from Car Miles Driven:
    # According to the EPA, the average passenger vehicle emits about 0.404 kg of CO2 per mile. 