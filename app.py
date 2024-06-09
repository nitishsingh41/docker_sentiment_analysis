import streamlit as st
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

#setting title of app
st.header("Sentiment Analysis")

#loading my model and tokenizer from huggingface modelhub
with st.spinner('Loading model...'):
    tokenizer = AutoTokenizer.from_pretrained("AdamCodd/tinybert-sentiment-amazon")
    model = AutoModelForSequenceClassification.from_pretrained("AdamCodd/tinybert-sentiment-amazon")

#text input area and button to run inference for the inputted text
user_input = st.text_area('Enter Text to Analyze')
button = st.button("Predict")


if user_input and button :
    #tokenizing our input to feed in model
    inputs = tokenizer([user_input], padding=True, truncation=True, max_length=512,return_tensors='pt')

    #running the model for output
    with torch.no_grad():
        logits = model(**inputs).logits
        
    #processing output to get the label and probability for it
    predicted_class_id = logits.argmax().item()
    predicted_class_label = model.config.id2label[predicted_class_id]
    probabilities = torch.nn.functional.softmax(logits, dim=-1)[0].cpu().numpy()
    score = probabilities[predicted_class_id]

    # Display the results
    st.write(f"Predicted Class: {predicted_class_label}")
    st.write(f"Score: {score:.4f}")

