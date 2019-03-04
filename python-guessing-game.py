#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:46:31 2019

@author: Sathira Kittisukmongkol
"""

from random import randint

# Guess the number
min = 0
max = 100
answerNumber = randint(min, max)

# Guessing game console
isEnd = False
userGuessCount = 0
while not isEnd:
    userNumber = int(input('Guess some number : '))
    if userNumber == answerNumber:
        print('You are correct!')
        print('The answer is ' + str(answerNumber))
        isEnd = True
    elif userNumber < min or userNumber > max:
        print('Out of bound')
        userGuessCount += 1
    elif userNumber > answerNumber:
        print('Less than ' + str(userNumber))
        userGuessCount += 1
    elif userNumber < answerNumber:
        print('More than ' + str(userNumber))
        userGuessCount += 1
    else:
        print('Try again')
    print('User guess : ' + str(userGuessCount))