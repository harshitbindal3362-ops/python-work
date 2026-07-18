# # # # x = 1
# # # # while x <= 5:
# # # #     print("Hello World!")
# # # #     x += 1

# # # i = 1 
# # # while i <= 1000:
# # #     print("Hello")
# # #     i += 1


# # # print(i)

# # # print numbers from 5 to 1:

# # x = 5
# # while x >= 1:
# #     print(x)
# #     x -= 1

# # Print numbers from 1 to 100:

# a = 1
# while a <= 100:
#     print(a)
#     a += 1

#  Print numbers from 100 to 1:
 
# a = 100
# while a >= 1:
#     print(a)
#     a -= 1

# Print the multiplication table of a number n:

# n = int(input("Enter Number:"))
# i = 1
# while i<= 10:
#     multi = n * i
#     print(f"{n} * {i} = {multi}")
#     i += 1


        
# n = int(input("Enter Number:"))
# i = 1
# while i<= 10:
#     print(n*i)
#     i+=1

# Print the elements of the following list using a loop

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heros = ["IronMan", "Thor", "Superman", "Batman"]

# index_value = 0
# while index_value < len(heros):
#     print(heros[index_value])
#     index_value+=1

# Search for a number x in this tuple using loop:

# a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# idx = 0
# for num in a:
#     print(a[idx])
#     idx += 1

# x = int(input("Enter the number you want to find"))
# idx = 0
# for num in a:
#     if(a[idx]==x):
#         print("Found at", idx )
#     else:
#         print("Not Found")
#         break
#     idx += 1

# for i in range(100, 1, -1):
#     print(i)

# n = int(input("Enter Number: "))
# for i in range(1, 11):
#     print( n * i)

# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# class Solution:
#     def checkStatus(self, a, b, flag):
#         # code here
#         if flag == False:
#             return (a >= 0 and b < 0) or (a < 0 and b >= 0)
#         else:
#             return a < 0 and b < 0

# arr = tuple(map(int, input().split()))

# # code here
# arr = (1, 5, 2, 4, 7, 8)

# distinct = True
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]==arr[j]:
#             distinct = False
# print(distinct)

# S= "gFgabcdEGfG"
# b = S.lower()
# if (b[0:3] == b[-3:]):
#     print("Yes")
# else:
#     print("No")


# class Node:
#     def init_(self, data):
#         self.data = data
#         self.next = None #this is to initialize the next pointer to None

# first = Node(1) #this is to create a new node with data 1
# second = Node(2) #this is to create a new node with data 2
# first.next = second #this is to link the first node to the second node

# print(first.data) #this is to print the data of the first node
# print(first.next.data) #this is to print the data of the second node



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None    

# class LinkedListStack:

#     def __init__(self):
#         self.top = None #this is to initialize the top of the stack as None
#         self._size = 0

#     def push(self, item):

#         new_node = Node(item)
#         new_node.next = self.top
#         self.top = new_node
#         self._size += 1

#     def pop(self):
#         if self.is_empty():
#             print("Stack is empty") #this is to print a message if the stack is empty
#             return None
#         popped_item = self.top.data
#         self.top = self.top.next
#         self._size -= 1
#         return popped_item
    
#     def peek(self):
#         if self.is_empty():
#             print("Stack is empty") #this is to print a message if the stack is empty
#             return None
#         return self.top.data
    
#     def is_empty(self):
#         return self.top is None
    
#     def size(self):
#         return self._size
    

# ll_stack = LinkedListStack() #this is to create a new stack
# ll_stack.push(1) #this is to add an item to the stack
# ll_stack.push(2) #this is to add another item to the stack
# ll_stack.push(3) #this is to add another item to the stack

# print("Stack size:", ll_stack.size()) #this is to print the size of the stack
# print("Top item:", ll_stack.peek()) #this is to print the item at the top of the stack
# print("Popped item:", ll_stack.pop()) #this is to remove and return the item from the top of the stack and print it
# print("Stack size after pop:", ll_stack.size()) #this is to print the size of the stack after popping an item




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# #Create Nodes
# first = Node(10)
# second = Node(20)
# third = Node(30)

# #Linking Nodes
# first.next = second
# second.next = third

# #Head of the linked list
# head = first

# class LinkedListQueue:
#     def __init__(self):
#         self.front =None
#         self.rear = None
#         self._size = 0

#     def enqueue(self, item):
#         new_node = Node(item)

#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#             self._size += 1
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self._size += 1

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty") #this is to print a message if the queue is empty
#             return None
#         dequeued_item = self.front.data
#         self.front = self.front.next
#         self._size -= 1
#         return dequeued_item
    
#     def peek(self):
#         if self.is_empty():
#             print("Queue is empty") #this is to print a message if the queue is empty
#             return None
#         return self.front.data
    
#     def is_empty(self):
#         return self.front is None
    
#     def size(self):
#         return self._size
    
# ll_queue = LinkedListQueue() #this is to create a new queue
# ll_queue.enqueue(1) #this is to add an item to the queue
# ll_queue.enqueue(2) #this is to add another item to the queue
# ll_queue.enqueue(3) #this is to add another item to the queue

# print("Queue size:", ll_queue.size()) #this is to print the size of the queue
# print("Front item:", ll_queue.peek()) #this is to print the item at the front of the queue
# print("Dequeued item:", ll_queue.dequeue()) #this is to remove and return the item from the front of the queue and print it
# print("Queue size after dequeue:", ll_queue.size()) #this is to print the size of the queue after dequeueing an item


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_begining(self, data):
#         #insert a new node with 'data' at the start of the list.
#         #Time complexity O(1)
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self, data):
#         #insert a new node with 'data' at the end of the list.
#         #Time complexity O(n)
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def delete_by_value(self, key):
#         #deletes the first node that contains the value key.
#         #Time complexity O(N)
#         current = self.head

#         #Case1 The head node itself holds the value to be deleted.
#         if current and current.data == key:
#             self.head = current.next
#             return True
        
#         #Case2 Search for the key, keep track of the previous node.
#         prev = None
#         while current and current.data != key:
#             prev = current
#             current = current.next

#         #Case3 key was not present in the list.
#         if not current:
#             return False
        
#         #Unlink the node from the linked list.
#         prev.next = current.next
#         return True
    
#     def search(self, key):
#         #search for a value in a list, return True if found otherwise false.
#         #Time complexity O(N)
#         current = self.head
#         while current:
#             if current.data == key:
#                 return True
#             current = current.next
#         return False
    
#     def reverse(self):
#     #reverse the list in=place
#     # Time complexity O(N)
#     # Space complexity O(1)
#         prev = None
#         current = self.head
#         while current:
#             nxt = current.next
#             current.next = prev
#             prev = current
#             current = nxt
#         self.head = prev

#     def has_cycle(self):
#         #detects if the linked list has cycle using Floyd's Tortoise and Hare's Algorithm.
#         #Time complexity O(N)
#         #Space complexity O(1)
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
        

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# #Create Nodes
# first = Node(10)
# second = Node(20)
# third = Node(30)

# #Linking Nodes
# first.next = second
# second.next = third

# #Head of the linked list
# head = first

# #printing linked list
# current = head
# while current:
#     print(current.data, end=" ->")
#     current = current.next

# print("None")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

head = first

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
