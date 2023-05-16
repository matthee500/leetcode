from typing import Optional# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the new merged list
        dummy = ListNode()
        current = dummy

        # Iterate through both lists until we reach the end of one of them
        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val < list2.val:
                # If the value in list1 is smaller, add it to the new list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # If the value in list2 is smaller or equal, add it to the new list
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next

            # Move to the next node in the new merged list
            current = current.next

        # If we reached the end of one of the lists, append the remaining nodes from the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the head of the new merged list (skipping the dummy node)
        return dummy.next


def create_linked_list(lst):
    # Create a dummy node to serve as the head of the new linked list
    dummy = ListNode()
    current = dummy

    # Iterate through the input list and create a new node for each value
    for val in lst:
        current.next = ListNode(val)
        current = current.next

    # Return the head of the new linked list (skipping the dummy node)
    return dummy.next

def main():
    # Create an instance of the Solution class
    my_merge = Solution()

    # Define two lists to be merged
    my_list_1 = [1, 2, 3]
    my_list_2 = [6, 5, 4]

    # Create linked lists from the regular lists
    my_linked_list_1 = create_linked_list(my_list_1)
    my_linked_list_2 = create_linked_list(my_list_2)

    # Call the mergeTwoLists method to merge and sort the two linked lists
    result = my_merge.mergeTwoLists(my_linked_list_1, my_linked_list_2)

    # Print the result (as a regular list for readability)
    result_list = []
    current = result
    while current:
        result_list.append(current.val)
        current = current.next
    sorted_result_list = sorted(result_list)
    print(sorted_result_list)

if __name__=='__main__':
    main()
