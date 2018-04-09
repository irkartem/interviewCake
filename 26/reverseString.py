#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/reverse-string-in-place 

#python crazy way 
def reverse(s):
    return "".join(list(s)[::-1])

#Good programmer writes code what can understand other human
def reverseHuman(s):
    strt = 0
    end = len(s)-1
    ray = list(s)
    while(strt < end):
        ray[strt],ray[end] = ray[end],ray[strt]
        strt += 1
        end -= 1
    return "".join(ray)

print(reverse("Very intresting gnirts ereh"))
print(reverseHuman("Very intresting gnirts ereh"))
