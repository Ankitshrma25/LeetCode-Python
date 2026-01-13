# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Linked List Utility Class
class LinkedList:

    # Create linked list from array
    def create_list(self, arr):
        head = None
        tail = None
        
        for val in arr:
            new_node = ListNode(val)
            if not head:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        
        return head

    # Display linked list
    def print_list(self, head):
        temp = head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


# Palindrome Checker Class
class Solution:

    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second_half = self.reverse_list(slow)

        # Step 3: Compare halves
        first_half = head
        temp = second_half

        while temp:
            if first_half.val != temp.val:
                return False
            first_half = first_half.next
            temp = temp.next

        return True

    # Reverse linked list
    def reverse_list(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev


# ---------------- MAIN DRIVER ----------------

if __name__ == "__main__":

    ll = LinkedList()
    solver = Solution()

    arr = [1, 2, 2, 1]   # Test input
    head = ll.create_list(arr)

    ll.print_list(head)

    result = solver.isPalindrome(head)
    print("Palindrome:", result)
