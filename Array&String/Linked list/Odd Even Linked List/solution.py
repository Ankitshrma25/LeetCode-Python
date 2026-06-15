class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def odd_even(self,head):

        if not head or not head.next: 
            return head
        odd = head
        even = head.next

        even_head=even   

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next


        odd.next = even_head     
        return head



if __name__ == "__main__":

    Node_list = [1,2,3,4,5,6]

    head = ListNode(Node_list[0])
    current = head

    for val in Node_list[1:]:
        current.next = ListNode(val)
        current = current.next

    head=solution().odd_even(head)
    # verify the list
    temp = head
    while temp:
        print(temp.val, end=" -> " if temp.next else " -> None\n")
        temp = temp.next