import unittest
from command_streamer import stream_command


class StreamCommandTestCase(unittest.TestCase):

    def test_stream_command(self):
        def on_output(s):
            print(s)

        command = ['bash', '-c',
                   'for i in `seq 1 5`; do echo $i && sleep 1; done']
        stream_command(
            command,
            on_output,
            on_output
        )
