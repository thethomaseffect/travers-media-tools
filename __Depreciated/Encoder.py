"""A library for encoding files"""

import subprocess


def encode(inputFilename, outputFilename):
    """Simple encoding with settings provided by file name
    extension. callback=None is used for performing operations
    asynchronously. Since we will be parsing FFMPEG's output
    for a progress bar it is required later."""

    PATH_TO_AVCONV = '/usr/bin/avconv'
    encodingProcess = subprocess.Popen([PATH_TO_AVCONV, '-i', inputFilename,
        outputFilename], stderr = subprocess.STDOUT,
        stdout = subprocess.PIPE)
    while encodingProcess.poll() is None:
        output = encodingProcess.stdout.readline()
        print output
