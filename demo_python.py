"""Simple arithmetic mean example using dummy values."""


def calculate_average(numbers):
    """Return the arithmetic mean of a list, or None if the list is empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    dummy_values = [10, 20, 30, 40, 50]
    print("Average:", calculate_average(dummy_values))  # 30.0
    print("Empty list:", calculate_average([]))  # None
