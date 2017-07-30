import asyncio
from typing import List, Callable


async def read_stream(stream, callback):
    while True:
        line = await stream.readline()
        if line:
            callback(line)
        else:
            break


def print_message(s):
    return print(s)


async def _stream_command(command: List[str],
                          on_stdout: Callable,
                          on_stderr: Callable):
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    if not on_stdout:
        on_stdout = print_message

    if not on_stderr:
        on_stderr = on_stdout

    await asyncio.wait([
        read_stream(process.stdout, on_stdout),
        read_stream(process.stderr, on_stderr),
    ])

    return await process.wait()


def stream_command(
    command: List[str],
    on_stdout=None,
    on_stderr=None
) -> int:
    loop = asyncio.get_event_loop()
    return_code = loop.run_until_complete(
        _stream_command(command, on_stdout, on_stderr)
    )
    loop.close()
    return return_code
