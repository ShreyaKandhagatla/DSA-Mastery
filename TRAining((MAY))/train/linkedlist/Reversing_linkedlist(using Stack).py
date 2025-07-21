class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def reverseUsingStack(self):
        if not self.head:
            return
        stack = []
        temp = self.head

        #  Push all nodes onto stack
        while temp:
            stack.append(temp)
            temp = temp.next

        #  Pop nodes to rebuild list in reverse
        self.head = stack.pop()
        temp = self.head

        while stack:
            temp.next = stack.pop()
            temp = temp.next

        temp.next = None  # End of list

ll = LinkedList()
arr = list(map(int,input().split()))
for num in arr:
    ll.addNode(num)

print("Original Linked List:")
ll.display()

ll.reverseUsingStack()

print("Reversed Linked List:")
ll.display()
