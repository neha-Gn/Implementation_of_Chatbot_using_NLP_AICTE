                                                        AI Chatbot using NLP

                                                        

                                                              Overview
                                                              
This project is an interactive AI chatbot built using Natural Language Processing (NLP) and Logistic Regression. The chatbot is designed to assist users with questions related to various topics such as Cybersecurity, Data Science, Machine Learning, Power BI, AI, and more. The interface is built using Streamlit, a powerful tool for creating web applications in Python.

                                                             Key Features:
                                                             
Intents-based Responses: The chatbot uses labeled intents and patterns to understand and respond to user input.

Training with Logistic Regression: The chatbot model is trained using Logistic Regression and a TF-IDF vectorizer to predict the intent based on the user’s query.

Real-time Chat: Users can interact with the chatbot in real-time, with chat history logged in a CSV file.

Domain-specific Assistance: The chatbot supports different domains (e.g., Cybersecurity, AI, etc.) which can be selected from the sidebar.

                                                            Technologies Used
                                                            
Python: For implementing the backend logic of the chatbot.

Streamlit: To build the web interface.

Scikit-learn: For implementing the Logistic Regression model and TF-IDF Vectorizer.

NLTK: For text processing, including tokenization and pattern matching.

CSV File: For logging conversation history.

                                                             File Structure
                                                             
script_exam.py: Main Python script that contains the backend logic for training the chatbot model, processing user input, and providing responses.

intents.json: JSON file that defines various intents, patterns, and responses for the chatbot.

chat_log.csv: CSV file where all chat history (user inputs, chatbot responses, and timestamps) is logged.

Chatbot.ipynb: Jupyter notebook for experimentation and testing of chatbot logic and training the model.

                                                                 Installation

Clone the repository or download the files to your local machine.

Install the required dependencies:



pip install -r requirements.txt

Run the Streamlit application:


streamlit run script_exam.py

                                                                 How it Works
                                                                 
Training the Model: The chatbot is trained using Logistic Regression with the patterns defined in the intents.json file. The model predicts the intent based on the user input.

User Interaction: The user interacts with the chatbot by typing queries in the input field. The chatbot then predicts the appropriate response based on the identified intent.

Logging: Every conversation is saved in the chat_log.csv file with the user's query, the chatbot’s response, and a timestamp.

                                                                Customization
                                                                
You can add more domains and intents by updating the intents.json file. Each intent should have:

tag: A label for the intent (e.g., "greeting", "pricing").

patterns: A list of possible user inputs for this intent.

responses: A list of possible chatbot responses for this intent.

To train the chatbot on new intents or patterns, simply modify the intents.json file and re-run the script to retrain the model.

                                                                About the Project
                                                                
This project is an AI-powered chatbot developed for IT services and IT businesses, designed to provide assistance and information in various domains. It aims to deliver seamless customer interaction through natural language processing and machine learning technologies.
