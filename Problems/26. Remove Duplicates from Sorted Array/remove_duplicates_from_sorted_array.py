from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the first pointer `i` to the first element
        i = 0
        # Iterate over the list from the second element to the end
        for j in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[j] != nums[i]:
                # Increment the `i` pointer
                i += 1
                # Copy the current element to the position after the last unique element
                nums[i] = nums[j]
        # Return the number of unique elements in the list
        return i + 1


def main():
    # Create an instance of the `Solution` class
    my_duplicates = Solution()
    # Define a list of integers containing duplicates
    num_array = [1, 2, 2, 3, 3, 3]
    # Call the `removeDuplicates()` method on the instance to remove duplicates from the list
    result = my_duplicates.removeDuplicates(num_array)
    # Print the number of unique elements and the modified list
    print(result, num_array[:result])

if __name__=='__main__':
    main()
