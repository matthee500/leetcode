class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Check if the list of strings is empty
        if not strs:
            return ""
        
        # Find the shortest string in the list
        shortest_string = min(strs, key=len)
        
        # Iterate through each character in the shortest string
        for i, ch in enumerate(shortest_string):
            # Compare the character with the corresponding character in each string
            for other in strs:
                if other[i] != ch:
                    # If characters don't match, return the common prefix up to this point
                    return shortest_string[:i]
        
        # If all characters match, return the entire shortest string
        return shortest_string


def main():
    my_prefix = Solution()
    my_val = ['car', 'cat']
    result = my_prefix.longestCommonPrefix(my_val)
    print(result)


if __name__=='__main__':
    main()
