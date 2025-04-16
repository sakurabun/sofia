import streamlit as st
import joblib
from scripts.features_extraction import extract_features  # Ensure this function is correctly defined

# load model
model = joblib.load("model/gender_model.pkl")

# streamlit interface
st.title("gender prediction from name")

name_input = st.text_input("enter a name:")

if st.button("Predict"):
    if not name_input.strip():
        st.warning("please enter a name.")
    else:
        # extract features from the input name
        features = extract_features(name_input)
        # predict gender using the model
        prediction = model.predict(features)[0]
        # map prediction to male or female
        gender = "male" if prediction == 1 else "female"
        # show result in the app
        st.success(f"predicted gender: **{gender}**")
