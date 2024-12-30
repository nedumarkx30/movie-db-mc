# def integer_num(n):
#     primes = []
#     primes1 = []
#     primes2 = []
#     total = 0
#     total1 = 0
#     total2 = 0
#     if n not in range(2, 1000):
#         print('enter numbers between 2 to 1000')
#     for i in range(2, n):
#         if n % i == 0:
#             primes.append(i)
#     for i in primes:
#         total = total + i
#     for i in range(2, total):
#         if total % i == 0:
#             primes1.append(i)
#     for i in primes1:
#         total1 = total1 + i
#     for i in range(2, total1):
#         if total1 % i == 0:
#             primes2.append(i)
#     for i in primes2:
#         total2 = total2 + i
#     return total2
# from cgi import print_environ
# from collections.abc import dict_items

# def prime(n):
#     non_prime = False
#     for i in range(2, n):
#         if n % i == 0:
#             non_prime = True
#             break
#     if non_prime:
#         print('it is not a prime number')
#     else:
#         print('it is a prime')

# import statistics
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# mean = statistics.mean(numbers)
#
# double = list(map(lambda x: x*2, numbers))
#
# filter = list(filter(lambda x: x > mean, numbers))
# print(filter)

#
# def prime(lst):
#     zeros = []
#     ones = []
#     subsequent_list = []
#     for i in lst:
#         if i == 0:
#             zeros.append(i)
#         if i == 1:
#             ones.append(i)
#     while True:
#         try:
#             subsequent_list.append(zeros.pop(0))
#             subsequent_list.append(ones.pop(0))
#         except IndexError:
#             break
#     return len(subsequent_list)
#
# numbers = [1,1,1,1,1,0,0,0,0,0,0,0, 0, 1, 9,4]
# primes = prime(numbers)
# print(primes)

# pythogras tripple
# def primitive_pyth_triples(n):
#     pythagorean_triples = []
#     for a in range(2, n):
#         for b in range(2, n):
#             for c in range(2, n):
#                 if a * a + b * b == c * c:
#                     numbers = (a, b, c)
#                     pythagorean_triples.append(numbers)
#     return len(pythagorean_triples)
#
# print(primitive_pyth_triples(15))

# lcm calculator

# def lcm_of_array(arr):
#     lcm = arr[0]
#     for i in range(1, len(arr)):
#         num1 = lcm
#         num2 = arr[i]
#         gcd = 1
#         # Finding GCD using Euclidean algorithm
#         while num2 != 0:
#             temp = num2
#             num2 = num1 % num2
#             num1 = temp
#         gcd = num1
#         lcm = (lcm * arr[i]) // gcd
#     return lcm


# hcf of numbers

# def hcf(lst):
#     def find_gcd(x, y):
#         while y:
#             x, y = y, x % y
#         return x
#     num1 = lst[0]
#     num2 = lst[1]
#     gcd = find_gcd(num1, num2)
#     for i in range(2, len(lst)):
#         gcd = find_gcd(gcd, lst[i])
#     return gcd
#
# l = [6, 8, 16]
# print(hcf(l))

# fibonacci series
# def fib(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         print(a, end = " ")
#         a, b = b, a + b
#         count += 1
#
# fib(7)


# Factorial of a number using recursion

# def recur_factorial(n):
#     if n < 0:
#         print("Sorry, factorial does not exist for negative numbers")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n*recur_factorial(n-1)
# print(recur_factorial(3))

# Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than or equal to a specified number.

# def prime_factors(num):
#     factors = []
#     factor = 2
#     while num >= 2:
#         if num % factor == 0:
#             factors.append(factor)
#             num = num / factor
#         else:
#             factor += 1
#     return factors
#
# print(prime_factors(9))


# def func(a, b=5):
#     return lambda x: x + a + b
#
# f = func(3)
# print(f(2))

# # Merge sort
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]
#
#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)
#
#     return merge(sortedLeft, sortedRight)
#
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sortedArr = mergeSort(unsortedArr)
# print("Sorted array:", sortedArr)

# # Bubble sort
# def bubble_sort(arr):
#
#     # Outer loop to iterate through the list n times
#     for n in range(len(arr) - 1, 0, -1):
#
#         # Inner loop to compare adjacent elements
#         for i in range(n):
#             if arr[i] > arr[i + 1]:
#
#                 # Swap elements if they are in the wrong order
#                 swapped = True
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#
# # Sample list to be sorted
# arr = [39, 12, 18, 85, 72, 10, 2, 18]
# print("Unsorted list is:")
# print(arr)
#
# bubble_sort(arr)
#
# print("Sorted list is:")
# print(arr)

# # linked list python
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     # Insertion at Beginning in Linked List
#     def insertAtBegin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node
#
#     # Insert a Node at a Specific Position in a Linked List
#     # Method to add a node at any index
#     # Indexing starts from 0.
#     def insertAtIndex(self, data, index):
#         if (index == 0):
#             self.insertAtBegin(data)
#
#         position = 0
#         current_node = self.head
#         while (current_node != None and position + 1 != index):
#             position = position + 1
#             current_node = current_node.next
#
#         if current_node != None:
#             new_node = Node(data)
#             new_node.next = current_node.next
#             current_node.next = new_node
#         else:
#             print("Index not present")
#
#     # Insertion in Linked List at End
#     def inserAtEnd(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while (current_node.next):
#             current_node = current_node.next
#
#         current_node.next = new_node
#
#     # Update the Node of a Linked List
#     # Update node of a linked list
#     # at given position
#     def updateNode(self, val, index):
#         current_node = self.head
#         position = 0
#         if position == index:
#             current_node.data = val
#         else:
#             while (current_node != None and position != index):
#                 position = position + 1
#                 current_node = current_node.next
#
#             if current_node != None:
#                 current_node.data = val
#             else:
#                 print("Index not present")
#
#     # Remove First Node from Linked List
#     def remove_first_node(self):
#         if (self.head == None):
#             return
#
#         self.head = self.head.next
#
#     # Remove Last Node from Linked List
#     def remove_last_node(self):
#
#         if self.head is None:
#             return
#
#         curr_node = self.head
#         while (curr_node.next != None and curr_node.next.next != None):
#             curr_node = curr_node.next
#
#         curr_node.next = None
#
#     # Delete a Linked List Node at a given Position
#     # Method to remove at given index
#     def remove_at_index(self, index):
#         if self.head is None:
#             return
#
#         current_node = self.head
#         position = 0
#
#         if index == 0:
#             self.remove_first_node()
#         else:
#             while current_node is not None and position < index - 1:
#                 position += 1
#                 current_node = current_node.next
#
#             if current_node is None or current_node.next is None:
#                 print("Index not present")
#             else:
#                 current_node.next = current_node.next.next
#
#     # Delete a Linked List Node of a given Data
#     def remove_node(self, data):
#         current_node = self.head
#
#         # Check if the head node contains the specified data
#         if current_node.data == data:
#             self.remove_first_node()
#             return
#
#         while current_node is not None and current_node.next.data != data:
#             current_node = current_node.next
#
#         if current_node is None:
#             return
#         else:
#             current_node.next = current_node.next.next
#
#     # Linked List Traversal in Python
#     def printLL(self):
#         current_node = self.head
#         while (current_node):
#             print(current_node.data)
#             current_node = current_node.next
#
#     # Get Length of a Linked List in Python
#     def sizeOfLL(self):
#         size = 0
#         if (self.head):
#             current_node = self.head
#             while (current_node):
#                 size = size + 1
#                 current_node = current_node.next
#             return size
#         else:
#             return 0
#

    # Example of linked list
    # Create a Node class to create a node
    # class Node:
    #     def __init__(self, data):
    #         self.data = data
    #         self.next = None
    #
    # # Create a LinkedList class
    # class LinkedList:
    #     def __init__(self):
    #         self.head = None
    #
    #     # Method to add a node at begin of LL
    #     def insertAtBegin(self, data):
    #         new_node = Node(data)
    #         if self.head is None:
    #             self.head = new_node
    #             return
    #         else:
    #             new_node.next = self.head
    #             self.head = new_node
    #
    #     # Method to add a node at any index
    #     # Indexing starts from 0.
    #     def insertAtIndex(self, data, index):
    #         if (index == 0):
    #             self.insertAtBegin(data)
    #
    #         position = 0
    #         current_node = self.head
    #         while (current_node != None and position + 1 != index):
    #             position = position + 1
    #             current_node = current_node.next
    #
    #         if current_node != None:
    #             new_node = Node(data)
    #             new_node.next = current_node.next
    #             current_node.next = new_node
    #         else:
    #             print("Index not present")
    #
    #     # Method to add a node at the end of LL
    #     def insertAtEnd(self, data):
    #         new_node = Node(data)
    #         if self.head is None:
    #             self.head = new_node
    #             return
    #
    #         current_node = self.head
    #         while (current_node.next):
    #             current_node = current_node.next
    #
    #         current_node.next = new_node
    #
    #     # Update node of a linked list
    #     # at given position
    #     def updateNode(self, val, index):
    #         current_node = self.head
    #         position = 0
    #         if position == index:
    #             current_node.data = val
    #         else:
    #             while (current_node != None and position != index):
    #                 position = position + 1
    #                 current_node = current_node.next
    #
    #             if current_node != None:
    #                 current_node.data = val
    #             else:
    #                 print("Index not present")
    #
    #     # Method to remove first node of linked list
    #
    #     def remove_first_node(self):
    #         if (self.head == None):
    #             return
    #
    #         self.head = self.head.next
    #
    #     # Method to remove last node of linked list
    #     def remove_last_node(self):
    #
    #         if self.head is None:
    #             return
    #
    #         current_node = self.head
    #         while (current_node != None and current_node.next.next != None):
    #             current_node = current_node.next
    #
    #         current_node.next = None
    #
    #     # Method to remove at given index
    #     def remove_at_index(self, index):
    #         if self.head == None:
    #             return
    #
    #         current_node = self.head
    #         position = 0
    #         if position == index:
    #             self.remove_first_node()
    #         else:
    #             while (current_node != None and position + 1 != index):
    #                 position = position + 1
    #                 current_node = current_node.next
    #
    #             if current_node != None:
    #                 current_node.next = current_node.next.next
    #             else:
    #                 print("Index not present")
    #
    #     # Method to remove a node from linked list
    #     def remove_node(self, data):
    #         current_node = self.head
    #
    #         if current_node.data == data:
    #             self.remove_first_node()
    #             return
    #
    #         while (current_node != None and current_node.next.data != data):
    #             current_node = current_node.next
    #
    #         if current_node == None:
    #             return
    #         else:
    #             current_node.next = current_node.next.next
    #
    #     # Print the size of linked list
    #     def sizeOfLL(self):
    #         size = 0
    #         if (self.head):
    #             current_node = self.head
    #             while (current_node):
    #                 size = size + 1
    #                 current_node = current_node.next
    #             return size
    #         else:
    #             return 0
    #
    #     # print method for the linked list
    #     def printLL(self):
    #         current_node = self.head
    #         while (current_node):
    #             print(current_node.data)
    #             current_node = current_node.next
    #
    # # create a new linked list
    # llist = LinkedList()
    #
    # # add nodes to the linked list
    # llist.insertAtEnd('a')
    # llist.insertAtEnd('b')
    # llist.insertAtBegin('c')
    # llist.insertAtEnd('d')
    # llist.insertAtIndex('g', 2)
    #
    # # print the linked list
    # print("Node Data")
    # llist.printLL()
    #
    # # remove a nodes from the linked list
    # print("\nRemove First Node")
    # llist.remove_first_node()
    # print("Remove Last Node")
    # llist.remove_last_node()
    # print("Remove Node at Index 1")
    # llist.remove_at_index(1)
    #
    # # print the linked list again
    # print("\nLinked list after removing a node:")
    # llist.printLL()
    #
    # print("\nUpdate node Value")
    # llist.updateNode('z', 0)
    # llist.printLL()
    #
    # print("\nSize of linked list :", end=" ")
    # print(llist.sizeOfLL())


# def sum(input, target):
#     for i in range(len(input)):
#         for j in range(len(input)):
#             if input[i] + input[j] == target:
#                 return i, j

#
# def sum_two(input, target):
#     for i in range(len(input)):
#         for j in range(len(input)):
#             if input[i] + input[j] == target:
#                 return [i ,j]
# x = [2, 7, 11, 15]
# print(sum_two(x, 9))

#
# def sum2(input, target):
#     harshMap = {}
#     for i, value in enumerate(input):
#         num = target - value
#         if num in harshMap:
#             return [harshMap[num], i]
#         else:
#             harshMap[value] = i
#
# x = [2, 7, 11, 15]
#
# print(sum2(x, 9))
#
# def duplicate_num(input):
#     for i in range (len(sorted(input))):
#         if input[i]==input[i+1]:
#             return True


# def product_num(num):
#     product = 1
#     result = []
#     for i in num:
#         product = product * i
#     for j in num:
#         res = int(product/j)
#         result.append(res)
#     return result
#
# print(product_num([1,2,3,4]))

# x = [1,2,3,4]
# res = [1] * len(x)
# print(res)


# def smaller(num):
#     sorted_num = sorted(num, reverse=True)
#     result
#     for i, value in enumerate(num):
#
#     return lst
# lst = [8, 3, 5, 1]
# print(smaller(lst))


# def fib(n, memo = {}):
#     if n in memo:
#         return memo[n]
#     if n <=2:
#         return 1
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[n]
#
# print(fib(50))

# def fib_tabulation(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     bottomUP = [0] * (n+1)
#     bottomUP[1] = 1
#     bottomUP[2] = 1
#     for i in range(2, n+1):
#         bottomUP[i] = bottomUP[i-1] + bottomUP[i-2]
#     return bottomUP[n]
#
# print(fib_tabulation(50))


fruits = ["apple", "banana", "tomatoes", "mango"]

hashMap = dict(enumerate(fruits))

del hashMap[0]

print(hashMap)