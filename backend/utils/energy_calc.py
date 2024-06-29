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
    

    # get count
    tok_count = tokenize(prompt)

    # calc total cost
    mistral_cost *= tok_count
    gpt4_cost *= tok_count

    # get winner
    if mistral_cost < gpt4_cost and mistral_cost < google_cost:
        best_route = "mistral"
    else:
        best_route = "google"

    return {"response_kWh" : {"mistral" : mistral_cost,
                          "gpt-4" : gpt4_cost,
                          "google" : google_cost,
                          "winner": best_route},
            "response_mi" : {"mistral" : mistral_cost/kWh_per_ft,
                          "gpt-4" : gpt4_cost/kWh_per_ft,
                          "google" : google_cost/kWh_per_ft}}

if __name__ == "__main__":
    print(calculate_energy_out(" a half after its launch, ChatGPT has 180 million users. The AI chatbot is used for all sorts of things, from creating a travel itinerary to writing a paper or just asking a silly question.However, ChatGPT consumes a lot of energy in the process, up to 25 times more than a Google search. Additionally, a lot of water is also used in cooling for the servers that run all that software. Per conversation of about 20 to 50 queries, half a litre of water evaporates – a small bottle, in other words.To the moon and backHowever, those ‘conversations’ are not even the biggest energy drain. By far the most energy goes into training the language model GPT (the software behind the chatbot), which is done with hyper-fast supercomputers fed with huge amounts of text from the internet."))