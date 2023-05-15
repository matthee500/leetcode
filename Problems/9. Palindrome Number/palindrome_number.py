class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert the integer to a string and check if it reads the same forwards and backwards
        return str(x) == str(x)[::-1]

def main():
    # Create an instance of the Solution class
    my_palindrome = Solution()

    # Define an integer to check if it's a palindrome
    my_int = 122

    # Call the isPalindrome method on the instance of the Solution class with my_int as an argument
    result = my_palindrome.isPalindrome(my_int)

    # Print the result
    print(result)

# Run the main function if this file is run as a script
if __name__=='__main__':
    main()