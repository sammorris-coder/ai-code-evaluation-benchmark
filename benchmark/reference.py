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



def is_positive_integer(value):
    """Return True if value is a positive integer, excluding booleans."""
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value > 0
    )



def unique_in_order(items):
    """Return unique items in their original order."""
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result



def cart_total(prices, discount_percent=0):
    """Calculate a cart total after applying a percentage discount."""
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative")

    subtotal = sum(prices)
    discount = subtotal * discount_percent / 100

    return subtotal - discount
