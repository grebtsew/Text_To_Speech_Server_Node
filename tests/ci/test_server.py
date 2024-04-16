import pytest
import json
from io import BytesIO
from unittest.mock import MagicMock, patch, call
import sys

sys.path.append("./src")
from server import S, server  # Import the server classes
import pytest
from threading import Thread
from server import server  # Import the server class
from unittest.mock import MagicMock, patch
from http.server import HTTPServer
from functools import partial


class TestServer:
    @patch("server.HTTPServer")
    def test_server_run(self, mock_http_server):
        # Mock HTTPServer and its instance
        mock_server_instance = MagicMock()
        mock_http_server.return_value = mock_server_instance

        # Create a mock speaker
        mock_speaker = MagicMock()

        # Create a server instance
        test_server = server(mock_speaker)

        # Start the server in a separate thread
        thread = Thread(target=test_server.run)
        thread.start()

        # Wait for a short time to ensure the server starts
        thread.join(timeout=1)

        # Check that HTTPServer was initialized with the correct arguments
        # mock_http_server.assert_called_once_with(('localhost', 8000), partial(S, mock_speaker))

        # Check that the server started serving forever
        mock_server_instance.serve_forever.assert_called_once()

        # Check that server_close was called
        mock_server_instance.server_close.assert_called_once()

        # Check that the thread is terminated
        assert not thread.is_alive()
