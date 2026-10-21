def average(numbers):
    """Return the average of a list of numbers.

    Return None if the list is empty.
    """
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def count_words(text):
    """Count whitespace-separated words in a string."""
    return len(text.split())
