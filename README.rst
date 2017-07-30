.. image:: https://travis-ci.org/conanfanli/command-streamer.svg?branch=master
  :alt: Build Status
  :target: https://travis-ci.org/conanfanli/command-streamer
  
command-streamer 
================
Stream command output with asyncio

Usage
----------
.. code-block:: python

    from command_streamer import stream_command
    
    stream_command(['bash', '-c', 'for i in `seq 1 2`; do echo $i; done'])
