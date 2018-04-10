#!/usr/bin/env python3
# artemirk@gmail.com https://www.interviewcake.com/question/python/delete-node

class LinkedListNode(object):

  def __init__(self, value):
      self.value = value
      self.next  = None

def delete_node(b):
    if not b.next:
        return False
    b.value=b.next.value
    b.next=b.next.next
    return True

def printList(head):
    if head.next:
        print("{}->".format(head.value), end='')
        printList(head.next)
    else:
        print("{}".format(head.value))

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
printList(a)
delete_node(b)
printList(a)
