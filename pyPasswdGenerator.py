#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Created : Fri 13 Apr 2018 09:46:27 PM EDT
# Modified: Tue 17 Apr 2018 08:37:25 PM EDT

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
import argparse
from zxcvbn import zxcvbn
import pprint

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
    handler = RotatingFileHandler(
        logFile,
        maxBytes=10 * 1024 * 1024,  # 10MB
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
    #print(s)


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
    ic(nrange)
    while (num < nrange[0]):
        num = randbelow(nrange[1])
        ic(num)
    return num


def wordLen(words, wlen):
    """
    Return a word between the
    lengths wlen[0] and wlen[1]
    """
    word = ''
    ic(wlen)
    while not wlen[0] <= len(word) <= wlen[1]:
        word = choice(words)
        ic(len(word))
    return word


def genPasswd(words,
              numWords=4,
              caps=True,
              syms=[],
              nrng=(10, 100),
              wlen=(6, 8)):
    """
    Returns password from words list

    TODO: add test code here
    """

    password = ''

    for i in range(numWords):
        word = wordLen(words, wlen)

        if caps:
            word = word.capitalize()

        password += word

        if i != numWords - 1:
            if nrng:
                num = randNumBetween(nrng)
                password += str(num)

            try:
                if syms: # TODO: up to N-1 syms???
                    password += syms[i]
            except Exception as e:
                s = '{} symbols given, {} needed.'.format(len(syms), numWords - 1)
                ic(s)
                print(s)
                raise

    return password


def main():

    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        "-c",
        "--capitalizeOff",
        help="turn off capitalization for all words",
        default=True,
        action="store_false")

    argparser.add_argument(
        "-w",
        "--numberOfWords",
        help="number of words to use",
        default=4,
        type=int,
        choices=range(2, 9))

    argparser.add_argument(
        "-n",
        "--numberRange",
        help="use numbers in the range of M to N-1",
        default=[],
        type=int,
        nargs=2)

    argparser.add_argument(
        "-l",
        "--wordLengths",
        help="use words of lengths M to N-1",
        default=[6, 8],
        type=int,
        nargs=2)

    argparser.add_argument(
        "-s",
        "--symbols",
        help="string of symbols to use between words",
        default="")

    argparser.add_argument(
        "filename",
        help=
        "word list file (default: google-10000-english-usa-no-swears_modified.txt",
        default="google-10000-english-usa-no-swears_modified.txt",
        nargs="?")

    args = argparser.parse_args()

    ic(args.filename)

    with open(args.filename) as f:
        try:
            words = [word.strip() for word in f]
            password = genPasswd(
                words,
                numWords=args.numberOfWords,
                caps=args.capitalizeOff,
                syms=args.symbols,
                nrng=tuple(args.numberRange),
                wlen=tuple(args.wordLengths))

            results = zxcvbn(password)
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(results)
            
            print('\npassword:  {}\n\nlength: {}\n'.format(password, len(password)))

            print('zxcvbn analysis:')
            score = results['score']
            print('         _____')
            print('Score: {} {}'.format(score, (score + 1)*'#'))
            if results['feedback']['suggestions']:
                print('suggestions:')
                for s in results['feedback']['suggestions']:
                    print('\t{}'.format(s))
            if results['feedback']['warning']:
                print('warning:\n\t{}'.format(results['feedback']['warning']))
            print('Crack time: {}'.format(results['crack_times_display']['online_no_throttling_10_per_second']))
            print('guesses_log10: {}'.format(results['guesses_log10']))

        except Exception as e:
            ic(repr(e))
            pass


if __name__ == '__main__':
    main()
