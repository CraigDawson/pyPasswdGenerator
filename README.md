# pyPasswdGenerator
A Python password generator for carbon based life forms 

This password generator will generate https://xkcd.com/936/ passwords by default using words from https://github.com/first20hours/google-10000-english and favoring less frequently used words.

The default list for this generator has the 1000 most common words deleted.

### Some proposed switches:

`$ pyPasswdGenerator [-s N] [-n N] [-w N] [-l M N] [-f wordlist]`

* _-s N_ will add N symbols to password (default N=0)
* _-n N_ will add N numbers to password (default N=0)
* _-w N_ generate a password with N words (default N=4)
* _-l M N_ will use words between M and N in length (default M=3, N=8)
* _-f wordlist_ will use the file wordlist for the input words
