import unittest
from command_streamer import stream_command

class StreamCommandTestCase(unittest.TestCase):

    def test_stream_command(self):
        stream_command()
