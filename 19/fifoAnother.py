#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/queue-two-stacks


class queue(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.inp = []
        self.out = []
    def dequeue(self):
        if len(self.out) == 0:
            if len(self.inp):
                while(len(self.inp)):
                        self.out.append(self.inp.pop())
            else:
                return None
        return self.out.pop()

    def enqueue(self,value):
            self.inp.append(value)

    def print(self):
        for i in range(len(self.inp)):
            print(self.inp[i])
        print("##### END ######")
        for i in range(len(self.out)):
            print(self.out[i])
        print("##### END ######")

q = queue()
q.enqueue('One')
q.enqueue('another')
q.enqueue('last')
q.print()
q.dequeue()
q.print()
