# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/2
# @Version 1.0

# List is a collection which is ordered and changeable. Allow duplicate members.

# Create a list
nums = [1, 1, 2, 3, 4, 5]
nums2 = list((1, 23, 4, 7, 8))
fruits = ['Apples', 'Bananas', 'Oranges']

print(nums, nums2)

# Get a value
print(nums[3])

# Get length of a list
print(len(nums))

# Append element
fruits.append('Peaches')
print(fruits)

# Remove element
fruits.remove('Apples')
print(fruits)

# Insert element
fruits.insert(0, 'Watermelons')
print(fruits)

# Reverse sort
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
