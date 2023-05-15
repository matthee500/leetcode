# Roman to Integer Converter
This project provides a Python implementation for converting Roman numerals to integers.

## Usage
To use this converter, create an instance of the `Solution` class and call its `romanToInt` method with a Roman numeral string as an argument. The method will return the integer equivalent of the Roman numeral.

## Implementation Details
The Solution class has two methods: `map_symbols` and `romanToInt`.

The `map_symbols` method takes a Roman symbol as an argument and returns its integer value.

The `romanToInt` method takes a Roman numeral string as an argument and returns its integer equivalent. It does this by looping through the string and using the `map_symbols` method to get the integer values of the symbols. It follows the rules of Roman numerals to add or subtract these values to get the final result.

## LeetCode Problem
https://leetcode.com/problems/roman-to-integer/