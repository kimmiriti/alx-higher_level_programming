#!/usr/bin/python3
for i in range (100):
    if i ==99:
        print("{}" .format(i), "\n")
    else:
        print("{:02}" .format(i), end=", ")
        