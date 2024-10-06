#!/usr/bin/env python3

# Name: Prasad Mistry
# Student Number: 111964193
# Student Email: pmistry21@myseneca.ca
# Course: OPS445
# Section: ZAA
# Semester: Fall 2024
# Date: 2024/10/05

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    space = p.stdout.read().decode('utf-8').strip()
    return space

if __name__ == "__main__":
    print(free_space())