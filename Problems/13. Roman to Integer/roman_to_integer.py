class Solution(object):
    # Method to map Roman symbols to their integer values
    def map_symbols(self, s):
        if (s == 'I'):
            return 1
        if (s == 'V'):
            return 5
        if (s == 'X'):
            return 10
        if (s == 'L'):
            return 50
        if (s == 'C'):
            return 100
        if (s == 'D'):
            return 500
        if (s == 'M'):
            return 1000
        return -1

    # Method to convert a Roman numeral string to an integer
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize variables
        i = 0
        ans = 0
        # Loop through the string to get the values
        while(i < len(s)):
            x1 = self.map_symbols(s[i])
            if(i + 1 < len(s)):
                x2 = self.map_symbols(s[i + 1])
                if (x1 >= x2):
                    ans = ans + x1
                    i = i + 1
                else:
                    ans = ans + x2 - x1
                    i = i + 2
            else:
                ans = ans + x1
                i = i + 1
        return ans

def main():
    my_romanToInt = Solution()

    my_numeral = 'V'

    result = my_romanToInt.romanToInt(my_numeral)

    print(result)


if __name__=='__main__':
    main()
