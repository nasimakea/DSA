# -*- coding: utf-8 -*-
"""insertion sorting problem.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bFI9Ufw-DSMho56h52pE-RjRcPOJjImS
"""

def insertion_sort(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key < arr[j]:
      arr[j+1]=arr[j]
      j-=1

    arr[j+1]=key

  return arr

arr=[40,20,12,13,400,30]

insertion_sort(arr)

def intersect_sort(a):
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1
    while j >=0 and key<a[j]:
      a[j+1]=a[j]

      j -=1
    a[j+1]=key

  return(a)

intersect_sort(arr2)

arr2=[20,40,32,14,54,76,67]

def insertion_sort_steps(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j >=0 and key>arr[j]:
      arr[j+1]=arr[j]
      j-=1

    arr[j+1]=key


  return(arr)

l1=[34,100,300,23,400,5000,2000]

insertion_sort_steps(l1)

def insert_sort_str(arr3):
  for i in range(1,len(arr3)):
    key=arr3[i]
    j=i-1
    while j >=0 and key < arr3[j]:
      arr3[j+1]=arr3[j]
      j-=1
    arr3[j+1]=key

  return(arr3)

arr = ["banana", "apple", "cherry", "date"]
insert_sort_str(arr)

def insertion_sort_with_duplicates(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j >=0 and key <arr[j]:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  return arr

insertion_sort_with_duplicates(arr )

arr = [4, 2, 2, 8, 3, 3, 1]



"""# 1. Write a Python program to sort a list of floating-point numbers using insertion sort."""

arr=[1.2,3.4,0.1,3.9,4.5,1.9,3.8]

def insertion_float_sort(a):
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1

    while j>=0 and key <a[j]:
      a[j+1]=a[j]
      j-=1

    a[j+1]=key

  return a

print(f"The sorted array  {arr} is {insertion_float_sort(arr)}")

float_list = [
    1.23, 4.56, 7.89, 2.34, 5.67,
    8.12, 3.45, 6.78, 9.01, 1.11,
    4.32, 7.65, 2.98, 5.43, 8.76,
    3.21, 6.54, 9.87, 0.12, 2.22
]

print(f"the sorted array of {float_list} is {insertion_float_sort(float_list)}")



"""# Given an array of positive and negative integers, sort the array using insertion sort and display the sorted array."""

arr=[-1,-20,30,-40,50,60,-100,300]

def insert_sort_neg_pos(a):
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1
    while j >=0 and key < a[j]:
      a[j+1]=a[j]
      j-=1
    a[j+1]=key

  return(a)

print(f"The sorted {arr} is {insert_sort_neg_pos(arr)}")



"""# 3 Implement insertion sort to sort the elements of an array of strings by their length."""

string_list = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon"
]

def insert_len_str_sorter(a):
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1
    while j >=0 and len(key)>len(a[j]):
      a[j+1]=a[j]
      j-=1
    a[j+1]=key

  return(a)

print(f"the sorted of {string_list} is {insert_len_str_sorter(string_list)}")



"""# 4 Modify the insertion sort algorithm to sort an array of tuples based on the second element of each tuple."""

number_tuple_list = [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8),
    (9, 10),
    (11, 12),
    (13, 14),
    (15, 16),
    (17, 18),
    (19, 20)
]

def insertion_tuple_sorter(a):
  b=len(a)
  for i in range(1,b):
    key=a[i]
    j=i-1
    while j>=0 and key[1]>a[j][1]:
      a[j+1]=a[j]
      j-=1
    a[j+1]=key


  return(a)

print(f"The insertion sorted of {number_tuple_list} is {insertion_tuple_sorter(number_tuple_list)}")



"""# 5 .Sort a list of student grades (e.g., A, B, C, D) using insertion sort, with a custom comparison to sort them in descending order."""

student_grades = [
    "B", "A", "D", "C", "B",
    "A", "C", "D", "A", "B"
]

def insert_grade_sorter(a):
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key > a[j]:
      a[j+1]=a[j]
      j-=1

    a[j+1]=key

  return(a)

print(f"the greader sorter of {student_grades} sorted to {insert_grade_sorter(student_grades)}")



"""# 6. Sort a list of dictionaries by a specific key (e.g., "age") using insertion sort.
.
"""

age_list = [
    {"age": 21},
    {"age": 34},
    {"age": 19},
    {"age": 45},
    {"age": 27},
    {"age": 32},
    {"age": 29},
    {"age": 22},
    {"age": 40},
    {"age": 18}
]

def insert_dict_sort(a):
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key['age']<a[j]['age']:
      a[j+1]=a[j]
      j-=1

    a[j+1]=key

  return(a)

print(f"The sorted dict of {age_list} is----- {insert_dict_sort(age_list)}")



"""#7  Implement insertion sort to sort a list of integers in ascending order and print how many swaps were made during sorting."""

import numpy as np

a=np.random.randint(10,100,20)

a

def insert_sorter(a):
  count=0
  n=len(a)
  for i in range(1,n):
    key=a[i]
    j=i-1
    count +=1
    while j >=0 and key <a[j]:

      a[j+1]=a[j]
      j-=1
    a[j+1]=key

  return(a,count)

print(f"The sorted of {a} is --- {insert_sorter(a)}")



"""# 8.  Modify the insertion sort to sort the array in alternating ascending and descending order. For example, the first element is smaller than the second, the second is larger than the third, etc."""
