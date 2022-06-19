"""
Runtime Complexity:
- O(n), as we are traversing the list using two pointers slow and fast. The while loop causes the loop to go iteratively till the end of the linked list.
-push() takes O(1), as we add a node at the beginning of the list and we just change the pointers and head.

Space Complexity:
O(n) - 'n' nodes to store and compute.

-Yes, the code worked on leetcode.

- To find the middle, I had to know the order in which the elements are added to the list. So I decided to write an extra function to print the list. So that I can make sure my solution is right.
"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = fast= self.head
        while fast and fast.next:
            slow = slow.next            #reaches the middle of the list
            fast = fast.next.next       #reaches the end of the list-- we can print this node's data if we were asked to find the last element of the list
        print("\n")
        print("The middle element of the list is: "+ str(slow.data))
    
    def printList(self):
        result =[]
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        
        
        
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printList()

list1.printMiddle() 
