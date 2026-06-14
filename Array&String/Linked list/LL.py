# Constructor to initialize a new node with data
class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None

class LinkedList:
    # construct a function to convert array to linked list
    @staticmethod
    def array_to_linkedlist(arr):
        # create head of the linkedlist with first element of the array
        head = Node(arr[0])
        # mover in our walking points. It always point to the last node
        mover = head 

        for i in range(1, len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover = temp
        return head
    
if __name__ == '__main__':

    array = [1,12,3,2,4,7]

    head = LinkedList.array_to_linkedlist(arr=array)
    
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next

    # print(head.data)