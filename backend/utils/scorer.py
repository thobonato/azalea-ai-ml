import joblib
import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import contractions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def get_csv_online():
    splits = {'train': 'train.csv', 'test': 'test.csv'}
    df = pd.read_csv("hf://datasets/BhabhaAI/DEITA-Complexity/" + splits["train"])
    df.to_csv("scorer_data.csv")

def preprocess(text):
    # Check if the input is a string
    if not isinstance(text, str):
        return ''  # Return an empty string for non-string input
    
    # Expand contractions
    text = contractions.fix(text)

    # Remove HTML tags, special characters, keep alpha numberic + punctuation
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s\-\']', ' ', text)
    
    # Lowercase, Tokenize the text
    text = text.lower()
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Combine tokens back into a single string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text


def run_preprocess(df):
    # preprocess prompt
    df["processed_prompt"]=df["prompt"].apply(preprocess)
    
    # remove outliers
    df = df[df["score"] > 0]
    df = df[df["score"] < 7]
    df = df.dropna(how="all")

    # save
    df.to_csv("scorer_data.csv")

    return df 


def train_model(df):
    sentences = df["prompt"].fillna("")
    complexity_scores = df["score"]

    # Preprocessing and feature extraction
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    y = np.array(complexity_scores)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)

    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    
    return model, vectorizer

# Function to predict complexity
def predict_complexity(model, vect, sentence):
    features = vect.transform([sentence])
    score = model.predict(features)
    return score[0]

def save_model_vect(model, vectorizer):
    # Assume `model` is your trained model
    joblib.dump(model, 'scorer_rnd_forest_mdl.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')


def load_model_vect(model_name="scorer_rnd_forest_mdl.pkl",vect_name='tfidf_vectorizer.pkl'):
    return joblib.load(model_name), joblib.load(vect_name)



if __name__ == "__main__":
    # ##>---- Preprocess CSV and Save -----<##
    # ########################################
    # get_csv_online()
    # df = pd.read_csv("scorer_data.csv")
    # run_preprocess(df)
    
    
    # ##>--------- Train and Save ---------<##
    # ########################################
    # df = pd.read_csv("scorer_data.csv")
    # from tqdm import tqdm
    # tqdm.pandas()
    # model, vectorizer = train_model(df)
    # save_model_vect(model, vectorizer)

    #>--------- Load and Inference ---------<##
    #######################################
    sample_sentences = ["How complex is this sentence?", 
                        "PrerequisitesBefore we start, make sure that you have the PyMongo distribution installed. In the Python shell, the following should run without raising an exception:import pymongoThis tutorial also assumes that a MongoDB instance is running on the default host and port. Assuming you have downloaded and installed MongoDB, you can start it like so:$ mongod",
                        "botta hella complex",
                        "write me a really insane essay on dogs.",
                        "who was the 15th president usa",
                        "write me a full stack project on astrophysics with visualization",
                        "Create a speech about miso soup and its health benefits and why we should eat it everyday. Do it based on the guidelines I am sending you and make sure it is about 9 minutes in length. You can create the visual aid yourself. Make it about how miso soup is made.  Guidelines: Overview A speaking outline is a condensed version of a preparation outline. You use the speaking outline when you deliver your speech. It contains just enough information to jog your memory and remind you of what you want to say. It should not have so much information on it that you could read it out loud and it would make sense. Instead, it consists of sentence fragments or key words. There are two exceptions to this rule: Quotations and oral citations. If you quote someone in your speech, it should be written on the speaking outline exactly as the source stated it. The speaking outline also includes detailed oral citations.  Please see the Oral Citation Guide for additional information on what to include in an oral citation.  Divide and label the outline into the main components of a speech, Introduction, Body, and Conclusion. Include transitions between each section of the speech. The transitions should be in parenthesis. Include more detailed oral citationsInclude exact wording of quotations if using Include brief visual aid indicators. In other words, what you plan to say to introduce the visual aid, how you will explain the visual aid, and what you plan to say immediately after you show your visual aid to the audience. MAKE SURE TO GIVE ME THE VISUAL AID AND ONLY USE REAL SOURCES AND PROVIDE LINKS TO THOSE SOURCES"]
    loaded_model,loaded_vect = load_model_vect()
    
    for sent in sample_sentences:
        print("Predicted complexity score:", predict_complexity(loaded_model, loaded_vect, sent))