#!/usr/bin/env python3
# artemirk@gmail.com programming for fun https://www.interviewcake.com/question/python/reverse-words 

def reverse_words(s):
    old = 0
    l = len(s)
    i = 0
    while (i < l+1):
        if i == len(s) or s[i] == ' ':
#            print("{} swap {} {}".format(old,i,s[i-1]))
            s = reverse_fr_to(s,old,i)
            old = i
        i += 1
    return s[::-1]

def reverse_fr_to(ray,fr,to):
    if fr == 0:
        return ray[to-1::-1]+ray[to:]
    else:
        return ray[0:fr+1]+ray[to-1:fr:-1]+ray[to:]



print(''.join(reverse_words(list("Hello my bueatiful girl"))))


# Complexity of this script is O(n), memory usage is O(1)
# Hm it's almost the same solution as a author. 
# We reverse each words, and after reverse entire string
# very intresting information about how to python pass the variables 
# by value or by reference. The answer is YES
