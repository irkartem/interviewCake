#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/reverse-linked-list

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverseList(lst):
    if not lst.next:
        return lst
    fst = lst 
    snd = lst.next
    fst.next = None
    while snd.next:
        tmp = snd.next
        snd.next = fst 
        fst = snd
        snd = tmp
    snd.next = fst
    return snd

# one -> second (need <-ONe) -> third (tmp) 


def printList(head):
    if head.next:
        print("{}->".format(head.value), end='')
        printList(head.next) 
    else:
        print("{}".format(head.value))



a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

printList(a)
printList(reverseList(a))
o = LinkedListNode("One element of Food")
printList(reverseList(o))
t = LinkedListNode("second Element")
o.next = t
printList(reverseList(o))
#I shoud create e->d->c->b->a

