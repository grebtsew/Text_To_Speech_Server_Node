import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime
import sys

sys.path.append("./src")

# Import your save_text_as_audio function from your_module
from recorder import save_text_as_audio


# Mock the datetime class to control the current time in the test
@pytest.fixture
def mock_datetime():
    with patch("recorder.datetime") as mock_datetime:
        yield mock_datetime


# Test save_text_as_audio function
def test_save_text_as_audio(mock_datetime):
    # Set a fixed current time for the test
    mock_datetime.now.return_value = datetime(2024, 4, 17, 10, 30, 15)

    # Define the text to save
    text_to_save = "Hello, world!"

    # Mock the gTTS class and its save method
    mock_gTTS = MagicMock()
    mock_gTTS_instance = mock_gTTS.return_value
    with patch("recorder.gTTS", mock_gTTS):
        # Call the save_text_as_audio function
        saved_file = save_text_as_audio(text_to_save)

    # Generate the expected filename based on the fixed current time
    expected_filename = "recordings/17-04-2024_10-30-15.mp3"

    # Assert that the gTTS constructor was called with the correct text
    mock_gTTS.assert_called_once_with(text=text_to_save, lang="en")

    # Assert that the save method of the gTTS instance was called with the expected filename
    mock_gTTS_instance.save.assert_called_once_with(expected_filename)

    # Assert that the function returned the expected filename
    assert saved_file == expected_filename
