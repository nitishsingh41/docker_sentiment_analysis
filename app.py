import streamlit as st
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

with st.spinner('Loading model...'):
    tokenizer = AutoTokenizer.from_pretrained("AdamCodd/tinybert-sentiment-amazon")
    model = AutoModelForSequenceClassification.from_pretrained("AdamCodd/tinybert-sentiment-amazon")


user_input = st.text_area('Enter Text to Analyze')
button = st.button("Predict")


if user_input and button :
    inputs = tokenizer([user_input], padding=True, truncation=True, max_length=512,return_tensors='pt')
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    predicted_class_label = model.config.id2label[predicted_class_id]
    score = probabilities[predicted_class_id]

    # Display the results
    st.write(f"Predicted Class: {predicted_class_label}")
    st.write(f"Score: {score:.4f}")

