from collections import deque


def is_palindrome(text: str) -> bool:
    """Check a palindrome, ignoring letter case and whitespace."""
    characters = deque(char for char in text.casefold() if not char.isspace())

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True


def main() -> None:
    try:
        text = input("Enter text to check: ")
    except (EOFError, KeyboardInterrupt):
        print("\nPalindrome check cancelled.")
        return

    if is_palindrome(text):
        print("The text is a palindrome.")
    else:
        print("The text is not a palindrome.")


if __name__ == "__main__":
    main()
