import asyncio
from typing import List, Callable


async def read_stream(stream, callback):
    while True:
        line = await stream.readline()
        if line:
            callback(line)
        else:
            break


async def _stream_command(command: List[str],
                          stdout_callback: Callable,
                          stderr_callback: Callable):
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    await asyncio.wait([
        read_stream(process.stdout, stdout_callback),
        read_stream(process.stderr, stderr_callback),
    ])

    return await process.wait()


def stream_command(
    command: List[str],
    stdout_callback,
    stderr_callback
) -> int:
    loop = asyncio.get_event_loop()
    return_code = loop.run_until_complete(
        _stream_command(command, stdout_callback, stderr_callback)
    )
    loop.close()
    return return_code


if __name__ == '__main__':
    stream_command(
        ["bash", "-c", "echo stdout && sleep 1 && echo stderr 1>&2 && sleep 1 && echo done"],
        lambda x: print("STDOUT: %s" % x),
        lambda x: print("STDERR: %s" % x),
    )
