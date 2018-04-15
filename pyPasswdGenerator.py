#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Created : Fri 13 Apr 2018 09:46:27 PM EDT
# Modified: Sun 15 Apr 2018 12:04:58 AM EDT

import better_exceptions

import logging
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from icecream import ic

import os
import sys

### Begin non-template imports -----------------------

from secrets import choice, randbelow

### Begin template code -----------------------

def baseUnixTimestamp():
    return '%s |> ' % datetime.now()


def baseCreateRotatingLog():
    """
    Creates a rotating log with output
    file based on this file's name
    """
    base = os.path.basename(__file__)
    root = os.path.splitext(base)[0]
    logFile = '.'.join([root, 'log'])

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(logFile,
                                  maxBytes=10*1024*1024,  # 10MB
                                  backupCount=5)
    logger.addHandler(handler)

    return logger


def baseDebugInfoOut(s):
    """
    icecream output function into a
    rotating log with time stamps and
    to STDOUT
    """
    global log

    log.info(s)
    print(s)


# Configure icecream with time stamp and output to
# file and screen
ic.configureOutput(prefix=baseUnixTimestamp, outputFunction=baseDebugInfoOut)

# Create log file that icecream will output to
log = baseCreateRotatingLog()

### End template code -----------------------


def randNumBetween(nrange):
    """
    Return number between
    nrange[0] and (nrange[1] - 1)
    """
    num = 0
    while(num < nrange[0]):
        num = randbelow(nrange[1])
        ic(num)
    return num


def genPasswd(words, numWords=4, nums=True, caps=True, syms=[], nrng=(10, 100)):
    """
    Returns password from words list
    """

    password = ''

    for i in range(numWords):
        word = choice(words)

        if caps:
            word = word.capitalize()

        password += word

        if i != numWords - 1:
            if nums:
                num = randNumBetween(nrng)
                password += str(nstr)

            if syms:
                # check that there are enough symbols
                if len(syms) == numWords:
                    password += syms[i]
                else:
                    ic('{} not {}'.format(len(syms), numWords))

    return password


def main():
    try:
        fn = sys.argv[1]
    except IndexError:
        print('Usage: {} file_name'.format(sys.argv[0]))
        sys.exit(1)

    ic(fn)  # default '/usr/share/dict/words'

    # On standard Linux systems, use a convenient dictionary file.
    # Other platforms may need to provide their own word-list.
    with open(fn) as f:
        words = [word.strip() for word in f]
        password = genPasswd(words,
                             numWords=3,
                             caps=False,
                             nums=True,
                             syms=[],
                             nrng=(1000, 10000))
        ic(password)


if __name__ == '__main__':
    main()
