#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Please think of a number between 0 and 100!")

begin=0
end=100

while(True):
    guess=int((end+begin)/2)
    print("Is your secret number " + str(guess) +"?")
    answer=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
    if answer == 'h':
        end = guess
    elif answer == 'l':
        begin = guess
    elif answer == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")