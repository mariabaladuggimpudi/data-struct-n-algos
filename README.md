# Data Structures and Algorithms

This repository contains a collection of common data structures and algorithms implemented in [programming language of your choice]. These implementations are meant for educational purposes and can be used as a reference for learning and understanding fundamental concepts in computer science.

## Table of Contents

- [Data Structures](#data-structures)
  - [1. Arrays and Strings](#arrays-n-strings)
  - [2. Stacks and Queues](#stacks-n-queues)
  - [3. Binary Trees](#binary-trees)
  - [4. Heap Trees](#heap-trees)
  - [5. Binary Search Trees](#binary-search-trees)
  - [6. Hash Tables](#hash-tables)
  - [7. Graphs](#graphs)
- [Algorithms](#algorithms)
  - [1. Sorting](#sorting)
  - [2. Searching](#searching)
  - [3. Dynamic Programming](#dynamic-programming)
  - [4. Graph Algorithms](#graph-algorithms)
  - [5. Recursion](#recursion)
  - [6. Greedy Algorithms](#greedy-algorithms)


## The source of this code repository is EPI Judge. The book is "Elements of Programming Interviews". Solutions to the problems are provided.

## Data Structures

### 1. Linked Lists

- Description: Implementation of singly and doubly linked lists.
- [Code](/data-structures/linked-lists)
- Usage example:

```python
# Example code snippet for using a linked list
from linked_list import LinkedList

# Create a new linked list
my_list = LinkedList()

# Insert elements
my_list.append(1)
my_list.append(2)
my_list.prepend(0)

# Remove an element
my_list.remove(2)

# Print the linked list
print(my_list)


