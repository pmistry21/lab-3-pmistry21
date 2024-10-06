#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Name: Prasad Mistry
# Student Number: 111964193
# Student Email: pmistry21@myseneca.ca
# Course: OPS445
# Section: ZAA
# Semester: Fall 2024
# Date: 2024/10/05

def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return int(number1) - int(number2)

def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))