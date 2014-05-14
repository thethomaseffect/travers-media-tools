"""Does a thing"""
from __future__ import print_function  # Stops Pylint warnings
from future.builtins import *  # Use Python 3 behaviors
import threading
from traversme.encoder.media_object import MediaObject
import re
import pexpect


class Encoder(object):

    """Represents an object that controls an encoding process"""

    def __init__(self, input_filename, output_filename):
        self.media_object = MediaObject(
            input_filename, output_filename)
        self.avconv_encoder = AvconvProcess(self.media_object)

    def start(self):
        """Do a thing"""
        self.avconv_encoder.start()

    def alive(self):
        """Do a thing"""
        return self.avconv_encoder.alive()

    def get_time_elapsed(self):
        """Do a thing"""
        return self.avconv_encoder.get_time_elapsed()


class AvconvProcess(object):

    """Represents an Avconv controllable subprocess"""

    def __init__(self, media_object):
        self.media_object = media_object
        self.encoder_thread = EncodingThread(self.media_object)

    def start(self):
        """Starts the avconv process."""
        self.encoder_thread.start()

    def alive(self):
        """
        Returns a boolean value representing if the avconv process is
        active
        """
        return self.encoder_thread.isAlive()

    def get_time_elapsed(self):
        """
        Returns a int between 0 and 100 representing the percentage
        of encoding currently completed.
        """
        # TODO: Once code builds and works replace regex with
        # .*?time=(\\d+\\.\\d+)
        time_elapsed_regex = ".*?time=([+-]?\\d*\\.\\d+)(?![-+0-9\\.])"
        regex_group = re.compile(time_elapsed_regex, re.DOTALL)
        if not self.alive():
            return -1
        subprocess_output = self.encoder_thread.subprocess_output
        percentage_elapsed = lambda x: float(
            (x / self.media_object.media_duration) * 100)
        if subprocess_output:
            regex_match = regex_group.search(subprocess_output[-1])
            if regex_match:
                # INFO: In Python 3.x round returns an int so the cast to float
                # can safely be removed
                current_percentage = percentage_elapsed(
                    round(float(regex_match.group(1))))
                return int(current_percentage)
        return -1


class EncodingThread(threading.Thread):

    """Do a thing"""

    def __init__(self, media_object):
        """Does a thing"""
        threading.Thread.__init__(self)
        self.media_object = media_object
        self.subprocess_output = []

    def run(self):
        """Does a thing"""
        # Some sensible defaults, such as overwriting if destination already
        # exists
        subprocess_command = "/usr/bin/avconv -i " + \
            self.media_object.input_filename + " -y " + \
            self.media_object.output_filename
        encoding_process = pexpect.spawn(subprocess_command)
        print ("Started %s" % subprocess_command)
        compiled_regex_list = \
            encoding_process.compile_pattern_list([pexpect.EOF, '(.+)'])
        while True:
            i = encoding_process.expect_list(compiled_regex_list, timeout=None)
            if i == 0:  # EOF
                print ("%s Process Finished" % subprocess_command)
                break
            else:
                output_line = encoding_process.match.group(0).rstrip()
                # Check the index of the first occurrence of frame=
                # Sadly this varies so we must also check 0
                if output_line.find("frame=") is 7 or 0:
                    self.subprocess_output.append(output_line)
        encoding_process.close
