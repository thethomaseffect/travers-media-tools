""" TODO: Add docstring """
import re
import pexpect


class MediaObject(object):

    """Represents an encodable object"""

    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.media_duration = self.get_media_duration()
        # INFO: All other media information could potentially be put here too

    def get_media_duration(self):
        """
        Spawns an avprobe process to get the media duration.

        Spawns an avprobe process and saves the output to a list, then uses
        regex to find the duration of the media and return it as an integer.
        """

        info_process = pexpect.spawn("/usr/bin/avprobe " + self.input_filename)
        subprocess_output = info_process.readlines()
        info_process.close
        # Non-greedy match on characters 'Duration: ' followed by
        # number in form 00:00:00:00
        regex_group = re.compile(".*?Duration: .*?(\\d+):(\\d+):(\\d+).(\\d+)",
                                 re.IGNORECASE | re.DOTALL)
        # Exits as soon as duration is found
        # PERF: Perform some tests to find the min number of lines
        # certain not to contain the duration, then operate on a slice
        # not containing those lines
        for line in subprocess_output:
            regex_match = regex_group.search(line)
            if regex_match:
                # Return the total duration in seconds
                return ((int(regex_match.group(1)) * 3600) +  # Hours
                        (int(regex_match.group(2)) * 60) +    # Minutes
                        int(regex_match.group(3)) +           # Seconds
                        # Round milliseconds to nearest second
                        1 if int(regex_match.group(3)) > 50 else 0)
        # Not found so it's possible the process terminated early or an update
        # broke the regex. Unlikely but we must return something just in case.
        return -1
