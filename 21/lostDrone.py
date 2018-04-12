#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/find-unique-int-among-duplicates?

ray = [10,5,6,7,8,34,67,89,67,34,8,7,6,5,10]

out = 0 
for i in ray:
    out = out ^ i
print(out)
