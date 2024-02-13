from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    """Represents the mood based on the sentiment analysis of the input text."""
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, threshold: float) -> Mood:
    """Analyze the sentiment of the input text and return the corresponding mood."""
    try:
        sentiment = TextBlob(input_text).sentiment.polarity  # type: ignore
    except Exception as e:
        raise ValueError("Failed to analyze sentiment") from e

    if sentiment >= threshold:
        return Mood('😊', sentiment)
    elif sentiment <= -threshold:
        return Mood('😒', sentiment)
    else:
        return Mood('😐', sentiment)


if __name__ == '__main__':
    while True:
        text: str = input('Text: ')
        mood: Mood = get_mood(text, threshold=0.3)

        print(f'{mood.emoji} ({mood.sentiment})')
