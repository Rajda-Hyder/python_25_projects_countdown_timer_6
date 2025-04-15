# ⏱ Countdown Timer (Python)

A simple Python countdown timer script with an optional display feature, plus unit testing using `unittest` and `unittest.mock`.

## 📁 Files

- `app.py` — Main script containing the `countdown` function and executable timer.
- `test_app.py` — Unit test for the `countdown` function.
- `README.md` — Project overview and usage instructions.

## 🧠 Features

- Countdown timer from a given number of seconds.
- Option to suppress display output (useful for testing).
- Includes unit test with mocked `time.sleep()` for faster test execution.

## ▶️ Usage

Run the timer from the command line:

```bash
python app.py
```
You’ll be prompted to enter the countdown time in seconds.

### Example:

```bash
Enter Time in seconds: 5
00:05
00:04
00:03
00:02
00:01
Timer completed successfully!
```
## 🧪 Running Tests

Make sure you have Python installed (version 3.6+ recommended).
This project uses `pytest` for running unit tests.

## To run the tests:

```bash
pytest
```

This command will automatically discover and run all test files matching the pattern test_*.py.

The test mocks time.sleep to skip actual delays, allowing for fast test execution.

## 📦 Requirements

No external dependencies are needed. This project uses only Python’s built-in libraries:

- time

- unittest

- unittest.mock

### 🤝 Contributing

Feel free to fork the project and open a pull request if you'd like to contribute!






