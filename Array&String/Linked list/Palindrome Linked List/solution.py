class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_LL(head):
    curr = head
    prev = None
    while curr:
        nxt_node = curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node

    return prev 


class solution:
    def isPalindrome(self, head):

        # step1: middle find
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        # reverse second part
        second = reverse_LL(slow.next)
        second_head = second

        first = head

        # compair both the part of the linkedlist
        while second_head:
            if first.val != second_head.val:
                reverse_LL(second)
                return False
            first = first.next
            second_head = second_head.next

        reverse_LL(second)
        return True
    


if __name__ == "__main__":

    Node_list = [1,2,3,2,1,3]

    head = ListNode(Node_list[0])
    current = head

    

    for val in Node_list[1:]:
        current.next = ListNode(val)
        current = current.next

    test=solution().isPalindrome(head)
    print(test)
    # verify the list
    temp = head
    while temp:
        print(temp.val, end=" -> " if temp.next else " -> None\n")
        temp = temp.next