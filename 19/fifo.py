#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/queue-two-stacks


class queue(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.one = []
        self.two = []
    def dequeue(self):
        if len(self.one) == 0:
            return None
        return self.one.pop()

    def enqueue(self,value):
        if len(self.one) == 0:
            self.one.append(value)
        else:
            while len(self.one):
                self.two.append(self.one.pop())
            self.one.append(value)
            while len(self.two):
                self.one.append(self.two.pop())
    def print(self):
        for i in range(len(self.one)):
            print(self.one[i])
        print("##### END ######")

q = queue()
q.enqueue('One')
q.enqueue('another')
q.enqueue('last')
q.print()
q.dequeue()
q.print()
