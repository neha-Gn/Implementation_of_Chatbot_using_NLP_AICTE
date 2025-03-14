import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter
    
    st.title("Transform Your IT Business with General Advisor *AI* Chatbots")

    # Custom CSS to modify text and sidebar colors
    st.markdown("""
        <style>
        /* Smooth background with a light purple gradient */
        body, .stApp {
            background: #C09AE3;  /* Light purple background */
            color: #0C1721;  /* Text color set to #0C1721 (dark slate blue) */
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }

        /* Chatbot container */
        .block-container {
            max-width: 700px;
            margin: auto;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* Proper title alignment and spacing */
        .stApp h1 {
            color: #0A161F !important;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }

        /* Sidebar Styling */
        .css-1d391kg, .css-1v3fvcr {
            background: #633B9C !important;  /* Sidebar color set to #633B9C (purple) */
            color: C0ACDC !important;  /* C0ACDC text in sidebar */
            border-radius: 10px;
            padding: 15px;
        }

        /* Input Box */
        .stTextInput>div>div>input {
            width: 100%;
            background: rgba(255, 255, 255, 0.9) !important;
            color: black !important;
            font-size: 16px;
            padding: 12px;
            border-radius: 10px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease-in-out;
        }
        .stTextInput>div>div>input:focus {
            border-color: #7dc9ff !important;
            box-shadow: 0px 0px 10px rgba(125, 201, 255, 0.6);
        }

        /* Chatbot Response Box */
        .stTextArea>div>textarea {
            width: 100%;
            background: rgba(255, 255, 255, 0.9) !important;
            color: black !important;
            font-size: 16px;
            border-radius: 10px;
            padding: 12px;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(to right, #7dc9ff, #5372ff) !important;
            color: white !important;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px;
            transition: 0.3s ease-in-out;
            border: none;
        }
        
        .stButton>button:hover {
            background: linear-gradient(to right, #5372ff, #7dc9ff) !important;
            box-shadow: 0px 0px 10px rgba(125, 201, 255, 0.6);
        }

        /* Change color of "You" and "Chatbot" text */
        .stTextInput input {
            color: #6A5ACD;  /* "You" text color (purple) */
        }

        .stTextArea textarea {
            color: #FF4500;  /* "Chatbot" text color (orange) */
        }

        /* Styling for subheader text color */
        .stApp h2 {
            color: #FF8C00; /* Warm orange color for subheaders */
            font-size: 24px;
            font-weight: 500;
            text-align: center;
        }
        
        /* Sidebar Styling */
        .css-1d391kg, .css-1v3fvcr {
            background-color: #633B9C !important;  /* Sidebar color set to #633B9C (purple) */
            color: white !important;  /* White text in sidebar */
            border-radius: 10px;
            padding: 15px;
        }

        </style>
    """, unsafe_allow_html=True)

    # Create a sidebar menu with options for selecting domain
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Sidebar for selecting a domain
    domain = st.sidebar.selectbox("Select Domain", ["General", "Cybersecurity", "Data Science", "Machine Learning", "Power BI", "AI", "Software Development", "Deep Learning"])

    # Home Menu
    if choice == "Home":
        st.markdown(f"<h2 style='text-align: center; color: #28184C;'>Chatting in <span style='color: #4D0740; font weight= bold'>{domain}</span> domain. Type your query below.</h2>", unsafe_allow_html=True)


        # Check if the chat_log.csv file exists, and if not, create it with column names
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You:", key=f"user_input_{counter}")

        if user_input:
            # Convert the user input to a string
            user_input_str = str(user_input)

            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime(f"%d-%m-%y %H:%M:%S")

            # Save the user input and chatbot response to the chat_log.csv file
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()

    # Conversation History Menu
    elif choice == "Conversation History":
        # Display the conversation history
        st.header("Conversation History")
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")

    # About Menu
    elif choice == "About":
        st.write("Welcome to the chatbot built using NLP and Intents. This chatbot can answer queries related to various topics.")

        st.subheader("Project Overview:")

        st.write("""
        The project is a **chatbot** that understands and responds to user input based on labeled **intents**. The system uses **Natural Language Processing (NLP)** and **Logistic Regression** to categorize and match the user's message with the corresponding intent. The interface is built using **Streamlit**, a powerful tool for building interactive web apps in Python.
        """)

        st.subheader("Intents Covered:")

        st.write("""
        The chatbot handles the following topics:
        1. ***Cybersecurity*** - Information about website security, encryption, DDoS, and phishing.
        2. ***Data Science*** - Information on data analysis, tools like Python, R, and data science workflows.
        3. ***Machine Learning*** - Covers various machine learning algorithms, use cases, and tools.
        4. ***Power BI*** - Explains how to use Power BI for data visualization, reports, and dashboards.
        5. ***AI*** - General AI topics including its impact, use cases, and how AI improves business operations.
        6. ***Software Development*** - Information on development methodologies, tools, and best practices.
        7. ***Deep Learning*** - Discusses neural networks, training models, and AI applications like image recognition.
        """)

        st.subheader("Technologies Used:")

        st.write("""
        - ***Natural Language Processing (NLP)***: We used NLP to process and classify user input, enabling the chatbot to understand user queries and respond accordingly.
        - ***Logistic Regression***: A machine learning model to predict the intent from user input.
        - ***Streamlit***: A web framework used to build the chatbot interface, making it easy for users to interact with the chatbot.
        - ***CSV File***: All conversation data is logged in a CSV file for review.
        """)

        st.subheader("Conclusion:")

        st.write("""
        This chatbot is designed to improve communication with users by responding to their questions based on predefined **intents**. The project can be expanded by incorporating additional data, using more advanced machine learning algorithms, or adding more functionalities like **voice recognition** and **multilingual support**.
        """)

if __name__ == '__main__':
    main()
