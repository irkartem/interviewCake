#!/usr/bin/env python3 
# artemirk@gmail.com https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k,lst):
    out = lst
    slow = lst
    fst = lst
    for _ in range(k-1):
        fst = fst.next
    while fst.next:
        fst = fst.next
        slow = slow.next
    return slow

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
print(kth_to_last_node(2, a).value)
print(kth_to_last_node(4, a).value)


# I use the two runners. One behind seconf in k steps
