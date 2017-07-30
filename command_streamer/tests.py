from unittest.mock import MagicMock, call
import unittest
from command_streamer import stream_command


class StreamCommandTestCase(unittest.TestCase):

    def test_stream_command(self):
        on_stdout = MagicMock(return_value=0)
        on_stderr = MagicMock(return_value=1)
        command = ['bash', '-c',
                   'for i in `seq 1 2`; '
                   'do echo $i && echo $i 1>&2 && sleep 1; done']
        stream_command(
            command,
            on_stdout,
            on_stderr
        )
        on_stdout.assert_has_calls([
            call(b'1\n'),
            call(b'2\n'),
        ])
        on_stderr.assert_has_calls([
            call(b'1\n'),
            call(b'2\n'),
        ])
