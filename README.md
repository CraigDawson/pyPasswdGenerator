# pyPasswdGenerator
A Python password generator for carbon based life forms 

This password generator will generate https://xkcd.com/936/ passwords by default using words from https://github.com/first20hours/google-10000-english list that has been modified.

The default list for this generator has the 1000 most common words deleted.

Uses https://github.com/dwolfhub/zxcvbn-python to estimate password strength 

### Usage:


`$ pyPasswdGenerator.py [-h] [-1] [-5] [-c] [-w {2,3,4,5,6,7,8}] [-n NUMBERRANGE NUMBERRANGE] [-l WORDLENGTHS WORDLENGTHS] [-s SYMBOLS] [filename]`

*  -h, --help            show this help message and exit
*  -1, --leetModerate    1337 code [Moderate] (def: no leet code)
*  -5, --leetSimple      1337 code [Simple] (def: no leet code)
*  -c, --capitalizeOff   turn off capitalization for all words (def: capitalize each word)
*  -w {2,3,4,5,6,7,8}, --numberOfWords {2,3,4,5,6,7,8}
*                        generate a password with N words (def: N=4)
*  -n NUMBERRANGE NUMBERRANGE, --numberRange NUMBERRANGE NUMBERRANGE
*                        will add numbers between M and N-1 to between words (def: no numbers)
*  -l WORDLENGTHS WORDLENGTHS, --wordLengths WORDLENGTHS WORDLENGTHS
*                        will use words between M and N in length (default M=6, N=8)
*  -s SYMBOLS, --symbols SYMBOLS
*                        will add symbol in SYMBOLS between word (def: no symbols)

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

#### Weak password
```
$ pyPasswdGenerator.py -w 2 -l 4 4

password:  HatsTold

length: 8

zxcvbn analysis:
         _____
Score: 2 ###
suggestions:
	Add another word or two. Uncommon words are better.
	Capitalization doesn't help very much.
Crack time: 3 days
guesses_log10: 6.4126285205443745
```

#### Very strong password
```
$ pyPasswdGenerator.py -w 6 -n 1000 10000 -s '^%$#@'

password:  Weekends6612^Exchange7858%Employ6340$Holmes2071#Counting1320@Mutual

length: 67

zxcvbn analysis:
         _____
Score: 4 #####
Crack time: centuries
guesses_log10: 53.21987904205257
```

