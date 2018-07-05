#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pexpect
import re
import shutil
import os


class SoundEffect:

    def __init__(self):
        pass

    @staticmethod
    def play(emotion):
        p = Player(os.path.dirname(os.path.realpath(__file__)) + "/../sounds/" + emotion + "mp3").playback
        p.expect(re.compile(b"have a nice day.*"))
        return p


class Player:

    def __init__(self, file):
        if self.omxplayer_exists():
            self.playback = pexpect.spawn("/usr/bin/omxplayer -o local --no-keys " + file)
        else:
            self.playback = pexpect.spawn("/usr/bin/mplayer " + file)

    def terminate(self):
        if self.playback and self.playback.isalive():
            self.playback.send("q")
            self.playback.terminate(force=True)

    def omxplayer_exists(self):
        return shutil.which("omxplayer") is not None
