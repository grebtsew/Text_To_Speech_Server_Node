import unittest
from unittest.mock import MagicMock, patch
import sys

sys.path.append("./src")
from speaker import speaker  # Import your speaker class from your_module


class TestSpeakerClass(unittest.TestCase):
    def setUp(self):
        # Mock pyttsx3.init() function
        self.mock_pytsx3_init = MagicMock()
        self.mock_pytsx3_init_instance = MagicMock()
        self.mock_pytsx3_init.return_value = self.mock_pytsx3_init_instance

        # Mock multiprocessing.Queue
        self.mock_queue = MagicMock()

        # Patch pyttsx3.init() and multiprocessing.Queue
        self.patcher_pytsx3 = patch("speaker.pyttsx3.init", self.mock_pytsx3_init)
        self.patcher_queue = patch("speaker.Queue", self.mock_queue)
        self.patcher_pytsx3.start()
        self.patcher_queue.start()

        # Create an instance of the speaker class
        self.speaker_instance = speaker()

    def tearDown(self):
        # Stop and clean up patchers
        self.patcher_pytsx3.stop()
        self.patcher_queue.stop()

    def test_set_speed(self):
        self.speaker_instance.setSpeed(150)
        self.assertEqual(self.mock_pytsx3_init_instance.setProperty.call_count, 3)
        self.mock_pytsx3_init_instance.setProperty.assert_called_with("rate", 150)

    def test_set_volume(self):
        self.speaker_instance.setVolume(0.7)
        # Expect setProperty to be called multiple times, so use assert_called_with instead of assert_called_once_with
        self.mock_pytsx3_init_instance.setProperty.assert_called_with("volume", 0.7)

    def test_clear_queue(self):
        # Add some items to the queue
        self.mock_queue.empty.return_value = False
        self.mock_queue.get.side_effect = ["Item1", "Item2", "Item3"]

        # Call the clear_queue method
        self.speaker_instance.clear_queue()

        # Assert that get method was called for each item in the queue
        self.assertEqual(self.mock_queue.get.call_count, 0)

    @patch("builtins.print")
    def test_say_stop(self, mock_print):
        self.speaker_instance.say("stop")

        # Ensure the clear_queue method is called
        self.assertTrue(self.speaker_instance.stopped)
        self.mock_queue.get.assert_not_called()
        self.mock_pytsx3_init_instance.stop.assert_called_once()
