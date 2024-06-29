# backend/utils/scorer.py

# dataset: https://huggingface.co/datasets/hkust-nlp/deita-complexity-scorer-data
# dataset: https://huggingface.co/datasets/BhabhaAI/DEITA-Complexity?row=36

import pandas as pd

splits = {'train': 'train.csv', 'test': 'test.csv'}
df = pd.read_csv("hf://datasets/BhabhaAI/DEITA-Complexity/" + splits["train"])

print(df.head)