
TEST_CASES = {
    "average": [
        {
            "input": ([2, 4, 6],),
            "expected": 4.0,
            "description": "Average of positive integers",
        },
        {
            "input": ([-2, 0, 2],),
            "expected": 0.0,
            "description": "Average with negative numbers",
        },
        {
            "input": ([],),
            "expected": None,
            "description": "Empty list returns None",
        },
    ],
    "count_words": [
        {
            "input": ("Hello Python world",),
            "expected": 3,
            "description": "Count words in normal text",
        },
        {
            "input": ("  Hello   Python  ",),
            "expected": 2,
            "description": "Ignore extra whitespace",
        },
        {
            "input": ("",),
            "expected": 0,
            "description": "Empty text contains no words",
        },
    ],
    "is_positive_integer": [
        {
            "input": (5,),
            "expected": True,
            "description": "Positive integer",
        },
        {
            "input": (0,),
            "expected": False,
            "description": "Zero is not positive",
        },
        {
            "input": (3.5,),
            "expected": False,
            "description": "Float is not an integer",
        },
        {
            "input": (True,),
            "expected": False,
            "description": "Boolean is not accepted",
        },
    ],
    "unique_in_order": [
        {
            "input": ([1, 2, 1, 3, 2],),
            "expected": [1, 2, 3],
            "description": "Remove duplicates and preserve order",
        },
        {
            "input": (["a", "b", "a"],),
            "expected": ["a", "b"],
            "description": "Preserve order of strings",
        },
        {
            "input": ([],),
            "expected": [],
            "description": "Empty list remains empty",
        },
    ],
    "cart_total": [
        {
            "input": ([10, 20, 30],),
            "expected": 60,
            "description": "Cart without discount",
        },
        {
            "input": ([10, 20, 30], 10),
            "expected": 54,
            "description": "Cart with ten percent discount",
        },
        {
            "input": ([],),
            "expected": 0,
            "description": "Empty cart total",
        },
        {
            "input": ([10, -5],),
            "expected_exception": ValueError,
            "description": "Negative price raises ValueError",
        },
        {
            "input": ([50], 110),
            "expected_exception": ValueError,
            "description": "Invalid discount raises ValueError",
        },
    ],
}
