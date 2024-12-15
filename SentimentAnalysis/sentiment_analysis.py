"""
    This module provide function to call the sentiment analyzer
    and get the result of the analysis
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the given text using the Watson Sentiment BERT API.

    This function sends a text input to the Watson Sentiment BERT API and returns
    the sentiment label and score based on the analysis. It handles successful 
    responses as well as server errors.

    Args:
        text_to_analyse (str): The text to be analyzed for sentiment.

    Returns:
        dict: A dictionary containing:
            - 'label' (str or None): The sentiment label ('SENT_POSITIVE', 
              'SENT_NEGATIVE', 'SENT_NEUTRAL'), or None if an error occurs.
            - 'score' (float or None): The sentiment score (ranging from -1 to 1), 
              or None if an error occurs.
    """
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/' \
            'v1/' \
            'watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    label = None
    score = None
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, let label and score  set to None


    # Return the label and score in a dictionary
    return {'label': label, 'score': score}
