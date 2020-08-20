'''
You’re given the pointer to the head nodes of two sorted linked lists. The data in both lists will be sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has data in ascending order. Either head pointer given may be null meaning that the corresponding list is empty.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    temp1 = head1
    temp2 = head2
    head3 = None
    while True:
        if temp1==None and temp2==None:
            break
        if temp1!=None and temp2!=None:
            if temp1.data<=temp2.data:
                if head3==None:
                    head3 = temp1
                    temp3 = head3
                else:
                    temp3.next = temp1
                    temp3 = temp3.next
                temp1 = temp1.next
            else:
                if head3==None:
                    head3 = temp2
                    temp3 = head3
                else:
                    temp3.next = temp2
                    temp3 = temp3.next
                temp2 = temp2.next
        elif temp1==None:
            temp3.next = temp2
            temp2 = temp2.next
            temp3 = temp3.next
        elif temp2==None:
            temp3.next = temp1
            temp1 = temp1.next
            temp3 = temp3.next
    return head3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
