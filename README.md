# goit-algo-hw-02

Homework 2: basic data structures, queues and deques.

## Setup

Python 3.10 or newer is required. Both tasks use the standard library only;
no third-party packages need to be installed.

Optional virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

The repository includes EditorConfig and VS Code settings for Python formatting,
plus recommendations for the Python and Black Formatter extensions.

## Tasks

| Task | File | Description |
| ---- | ---- | ----------- |
| 1 | `task_01/task_01.py` | Service center simulation using `queue.Queue` |
| 2 | `task_02/task_02.py` | `is_palindrome(text)` using `collections.deque` |

## Run

Run each script from the repository root:

```bash
python3 task_01/task_01.py
python3 task_02/task_02.py
```

Task 1 automatically generates a request with a unique sequential ID, adds it to
the queue and processes the oldest request every second. Press Ctrl+C to stop
the simulation. The `process_request()` function also reports an empty queue
when no requests are available.

Task 2 prompts for a string and compares characters from both ends of a deque.
It ignores letter case and whitespace, including tabs and line breaks, and
handles both even and odd lengths. Punctuation remains part of the comparison.
Empty strings, whitespace-only strings and single characters are palindromes.

Examples:

| Input | Result |
| ----- | ------ |
| `Abba` | Palindrome |
| `Race car` | Palindrome |
| `Я несу гусеня` | Palindrome |
| `Python` | Not a palindrome |
