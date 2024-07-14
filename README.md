
# Building a ChatGPT Interface with OLA Krutrim's Mistral-7B-Instruct Model

This repository contains a Flask application that interacts with the OLA Krutrim OpenAI service to provide conversational responses using the Mistral-7B-Instruct model.

## Overview

The Flask application allows users to ask questions via a web interface and receive responses from the ChatGPT model hosted on OLA Krutrim's OpenAI service using the Mistral-7B-Instruct model. The application demonstrates how to securely manage API keys using environment variables and interact with an external API.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. Install dependencies:

    pip install -r requirements.txt

3. Set up environment variables:

    Create a .env file in the root directory of your project.
    Add your OLA Krutrim API key to the .env file:

    API_KEY="your_ola_krutrim_api_key_here"

    Note: Replace "your_ola_krutrim_api_key_here" with your actual API key obtained from [OLA Krutrim API Key creation page](https://cloud.olakrutrim.com/console/inference-service?section=api-keys)

4. Run the Flask application:

    python app.py

5. Open your web browser and navigate to http://localhost:5000 to access the application

### Usage
Enter a question in the input field and click "Ask".
The application will send the question to the ChatGPT model (Mistral-7B-Instruct) via the OLA Krutrim API and display the response on the webpage.

### Folder Structure

.
├── app.py                # Flask application code
├── templates/            # HTML templates
│   └── index.html        # Main template for the web interface
├── static/               # Static files (CSS, images)
│   └── style.css         # CSS styles for the web interface
├── .env                  # Environment variables file (ignored by Git)
└── requirements.txt      # Python dependencies
