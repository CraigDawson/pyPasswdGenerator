# pyPasswdGenerator
A Python password generator for carbon based life forms 

This password generator will generate https://xkcd.com/936/ passwords by default using words from https://github.com/first20hours/google-10000-english list that has been modified.

The default list for this generator has the 1000 most common words deleted.

### Usage:

`$ pyPasswdGenerator [-c] [-s syms] [-n M N] [-w N] [-l M N] [wordlist]`

* _-c_ will turn off capitalization of each word (def: capitalize each word)
* _-s syms_ will add symbols syms to password between words (def: no symbols)
* _-n M N_ will add number between M and N-1 to password (def: no numbers)
* _-w N_ generate a password with N words (def: N=4)
* _-l M N_ will use words between M and N in length (default M=3, N=8)
* _wordlist_ will use the file wordlist for the input words

### Examples:

#### Default run
```
$ pyPasswdGenerator.py

password:  ChronicExtendsExactlyPricing

length: 28

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 15.118834100208932
```

#### Caps off
```
$ pyPasswdGenerator.py -c

password:  beatlesseminaradoptioncritics

length: 29

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 14.058202744567343`
```

#### 6 words in password
```
$ pyPasswdGenerator.py -w 6

password:  SharonWhateverPrepareChainsBaselinePastor

length: 41

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 22.342998728304725
```

#### Adding two digit numbers between words
```
$ pyPasswdGenerator.py -n 10 100

password:  Wallace88Criminal91Anymore23Trucks

length: 34

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 22.985003378228946
```

#### Use words between 10 and 15 characters long
```
$ pyPasswdGenerator.py -l 10 15

password:  AppliancesInfectiousNationwideReliability

length: 41

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 17.531166337447022
```

#### Add symbols between words
```
$ pyPasswdGenerator.py -s '!@#'

password:  Cities!Mitchell@Debate#Drinking

length: 31

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 19.469850039346124
```
