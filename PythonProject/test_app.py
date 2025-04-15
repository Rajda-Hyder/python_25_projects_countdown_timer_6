# imports
from app import countdown
from unittest.mock import patch

# test function
def test_countdown_test_run_without_display():
    with patch("time.sleep", return_value = None):
        countdown(3, display=False)
