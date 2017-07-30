import unittest
from command_streamer import stream_command


class StreamCommandTestCase(unittest.TestCase):

    def test_stream_command(self):
        def on_output(s):
            print(s)
        stream_command(
            ["bash", "-c", "echo stdout && sleep 1 && echo stderr 1>&2 && sleep 1 && echo done"],
            on_output,
            on_output
        )
