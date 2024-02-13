import pytest
from master import get_mood, POSITIVE_EMOJI, NEGATIVE_EMOJI, NEUTRAL_EMOJI


def test_positive_sentiment():
    """Test that positive sentiment returns the correct mood."""
    text = "I love this product!"
    mood = get_mood(text, threshold=0.3)
    assert mood.emoji == POSITIVE_EMOJI
    assert mood.sentiment > 0


def test_negative_sentiment():
    """Test that negative sentiment returns the correct mood."""
    text = "This product is terrible."
    mood = get_mood(text, threshold=0.3)
    assert mood.emoji == NEGATIVE_EMOJI
    assert mood.sentiment < 0


def test_neutral_sentiment():
    """Test that neutral sentiment returns the correct mood."""
    text = "This product is okay."
    mood = get_mood(text, threshold=0.3)
    assert mood.emoji == NEUTRAL_EMOJI
    assert abs(mood.sentiment) < 0.3


def test_invalid_input():
    """Test that invalid input raises an exception."""
    with pytest.raises(ValueError):
        get_mood("", threshold=0.3)
