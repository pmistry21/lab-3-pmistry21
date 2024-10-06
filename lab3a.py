#!/usr/bin/env python3

# return_text_value() function

# Name: Prasad Mistry
# Student Number: 111964193
# Student Email: pmistry21@myseneca.ca
# Course: OPS445
# Section: ZAA
# Semester: Fall 2024
# Date: 2024/10/05

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))