#!/usr/bin/env python3

def char_count(str):
    countdict={}
    for char in str:
        c = countdict.get(char)
        if c is None:
            countdict[char] = 1
        else:
            countdict[char] += 1
    print(countdict)
    #char_list = set(str)
    #for char in char_list:
    #    print(char,str.count(char))


if __name__ == '__main__':

    s = input("Enter a string:")
    char_count(s)