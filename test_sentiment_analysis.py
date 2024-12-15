"""
Unit tests for the sentiment analyzer function.

This module contains a test class `TestSentimentAnalyzer` that uses the 
unittest framework to validate the functionality of the `sentiment_analyzer` function. 
The test cases cover positive, negative, and neutral sentiment inputs.
"""
import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    """
    Unit tests for the `sentiment_analyzer` function.
    """

    def test_sentiment_analyzer(self):
        """
        Tests the sentiment analyzer with various sentiment inputs.

        Validates that the function correctly identifies positive, negative, 
        and neutral sentiments based on the input text.
        """

        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()
