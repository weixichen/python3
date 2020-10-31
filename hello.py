#!/usr/bin/env python3

# print("Hello", "World!")
import sys
L = [2, 3, 5, 7]
for x in reversed(L):
    print(x)

for x in reversed(range(1, 10)):
    print(x)

L = ("hello")
for x in reversed(L):
    print(x)

L = sorted("hello")
print(L)

print(sys.argv)