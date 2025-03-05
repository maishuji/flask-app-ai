''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

#Initiate the flask app
app = Flask(__name__)

# Configure IBM Watson API
API_KEY = os.getenv("WATSON_API_KEY")
API_URL = os.getenv("WATSON_URL")

# TODO: Integrate dotenv credentials for use with ibm watson 
#if not API_KEY or not API_URL:
#    raise EnvironmentError("Please set WATSON_API_KEY and WATSON_URL in the .env file.")

#authenticator = IAMAuthenticator(API_KEY)

@app.route("/sentimentAnalyzer")
def sent_analyser():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # DONE
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyser function and store the response
    response = sentiment_analyser(text_to_analyze)
    # Extract the label and score from the response
    label = response['label']
    score = response['score']
    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #DONE
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    #DONE
    app.run(host="0.0.0.0", port=5000, debug=True)
