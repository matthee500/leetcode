class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create an empty dictionary to store the numbers and their indices
        num_dict = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_dict:
                # If it is, return the indices of the current number and its complement
                return[num_dict[complement], i]

            # If not, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no pair of numbers add up to the target, return an empty list
        return []

def main():
    # Create an instance of the Solution class
    my_twoSum = Solution()
    # Define an array of numbers
    my_array = [1, 2, 3, 4, 5]
    # Define a target sum
    my_target = 7
    # Call the twoSum method on the instance of Solution with the array and target as arguments
    result = my_twoSum.twoSum(my_array, my_target)
    # Print the result
    print(result)

if __name__=='__main__':
    main()
