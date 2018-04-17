# pyPasswdGenerator
A Python password generator for carbon based life forms 

This password generator will generate https://xkcd.com/936/ passwords by default using words from https://github.com/first20hours/google-10000-english and favoring less frequently used words.

The default list for this generator has the 1000 most common words deleted.

### Some proposed switches:

`$ pyPasswdGenerator [-c] [-s syms] [-n M N] [-w N] [-l M N] [wordlist]`

* _-c_ will capitalize each word (def: capitalize each word)
* _-s syms_ will add symbols syms to password between words (def: no symbols)
* _-n M N_ will add number between M and N-1 to password (def: no numbers)
* _-w N_ generate a password with N words (def: N=4)
* _-l M N_ will use words between M and N in length (default M=3, N=8)
* _wordlist_ will use the file wordlist for the input words

TODO: examples
