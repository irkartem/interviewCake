#!/usr/bin/env python3
# artemirk@gmail.com https://www.interviewcake.com/question/python/largest-stack?
class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.mxstack = []

    def push(self, item):
        if len(self.mxstack):
            if item > self.mxstack[-1]:
                self.mxstack.append(item)
            else:
                self.mxstack.append(self.mxstack[-1])
        else:
            self.mxstack.append(item)
        self.items.append(item)


    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        self.mxstack.pop()
        return self.items.pop()

    def getmax(self):
        if len(self.mxstack):
            return self.mxstack[-1]
        return None

st = MaxStack()
st.push(10)
st.push(4)
print(st.getmax())
st.push(34)
print(st.getmax())

st.pop()
print(st.getmax())

