import argparse
import logging
from textblob import TextBlob
from dataclasses import dataclass

# Constants for emojis
POSITIVE_EMOJI = '😊'
NEGATIVE_EMOJI = '😒'
NEUTRAL_EMOJI = '😐'


@dataclass
class Mood:
    """Represents the mood based on the sentiment analysis of the input text."""
    emoji: str
    sentiment: float


def get_sentiment(input_text: str) -> float:
    """Calculate the sentiment polarity of the input text."""
    try:
        return TextBlob(input_text).sentiment.polarity
    except Exception as e:
        logging.error(f"Failed to calculate sentiment: {e}")
        raise


def get_mood(input_text: str, *, threshold: float) -> Mood:
    """Analyze the sentiment of the input text and return the corresponding mood."""
    if not input_text:
        raise ValueError("Input text cannot be empty.")
    sentiment = get_sentiment(input_text)

    if sentiment >= threshold:
        return Mood(POSITIVE_EMOJI, sentiment)
    elif sentiment <= -threshold:
        return Mood(NEGATIVE_EMOJI, sentiment)
    else:
        return Mood(NEUTRAL_EMOJI, sentiment)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Analyze text sentiment and display mood.')
    parser.add_argument('--text', help='Input text to analyze.')
    parser.add_argument('--threshold', type=float, default=0.3,
                        help='Threshold for sentiment analysis.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    text = args.text or input('Text: ')
    mood = get_mood(text, threshold=args.threshold)
    print(f'{mood.emoji} ({mood.sentiment})')


if __name__ == '__main__':
    main()
