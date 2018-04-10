#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/linked-list-cycles

class LinkedListNode(object):

  def __init__(self, value):
      self.value = value
      self.next  = None

def detectCycle(a):
    if not a.next:
        return 'No cycle found'
    slw = a
    fst = a.next
    while fst.next.next:
        fst = fst.next.next
        slw = slw.next
        if slw == fst:
            return 'Detect cycl, runners meet at {}'.format(slw.value)
    return 'No cycle found'

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(detectCycle(a))

e.next = b
print(detectCycle(a))

e.next = a
print(detectCycle(a))
