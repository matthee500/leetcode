class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Create a dictionary of valid bracket pairs
        pairs = {')': '(', '}': '{', ']': '['}
        # Iterate over the characters in the string
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack.pop() != pairs[char]:
                    return False
        return not stack


def main():
    # Create an instance of the Solution class
    my_test = Solution()
    # Define a test string
    my_value = '()'
    # Call the isValid method on the test string
    result = my_test.isValid(my_value)
    print(result)


if __name__ == '__main__':
    main()
