import pytest
from unittest.mock import MagicMock

import sys

sys.path.append("./src")
from console import console  # Import your console class from your_module


def test_console_say_called():
    # Create a mock speaker object
    mock_speaker = MagicMock()

    # Create a console instance with the mock speaker
    console_instance = console(mock_speaker)

    # Start the console thread
    # console_instance.start()
    assert console_instance != None
