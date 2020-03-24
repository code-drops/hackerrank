/*

A Node class is provided for you in the editor. A Node object has an integer data field,data , and a Node instance pointer,next , pointing to another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to the head  node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.

*/

import java.io.*;
import java.util.*;
class Node{
	int data;
	Node next;
	Node(int d){
        data=d;
        next=null;
    }
	
}
class Solution
{
    public static Node removeDuplicates(Node head)
    {
      //Write your code here
        if(head==null || head.next==null)
        {
            return head;
        }
        Node current = head;
        while(current.next!=null){
            if(current.data==current.next.data){
                current.next = current.next.next;
            }else{
            current = current.next;
            }
        }
        return head;
    }
	 public static  Node insert(Node head,int data)
