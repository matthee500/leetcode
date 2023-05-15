# Longest Common Prefix
This repository contains a Python implementation of an algorithm to find the longest common prefix of a list of strings.

## Usage
The code defines a Solution class with a method `longestCommonPrefix` that takes a list of strings as input and returns the longest common prefix of those strings.

To use the code, create an instance of the `Solution` class and call its `longestCommonPrefix` method with a list of strings as an argument.

## How it works
The `longestCommonPrefix` method first checks if the input list is empty. If it is, it returns an empty string.

Next, it finds the shortest string in the input list. This is done using the `min` function with the `key` argument set to `len`, which returns the element of the list with the smallest length.

The method then iterates through each character in the shortest string. For each character, it compares it with the corresponding character in each string in the input list. If any characters don’t match, it returns the common prefix up to this point.

If all characters match for all strings in the input list, it returns the entire shortest string as the longest common prefix.

## LeetCode Problem
https://leetcode.com/problems/longest-common-prefix/