#check loop, starting point, length of loop (Count)
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addNode(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def detect_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def find_loop_start(self):
        meet_point = self.detect_loop()
        if not meet_point:
            return None

        start = self.head
        while start != meet_point:
            start = start.next
            meet_point = meet_point.next
        return start

    def loop_length(self):
        meet_point = self.detect_loop()
        if not meet_point:
            return 0
        
        count = 1
        temp = meet_point.next
        while temp != meet_point:
            temp = temp.next
            count += 1
        return count
    
head1 = LinkedList()
head1.addNode(10)
head1.addNode(20)
head1.addNode(30)
head1.addNode(40)
head1.addNode(50)
head1.addNode(60)
head1.addNode(70)
head1.display()
head1.tail.next = head1.head.next.next.next # 70 and 40
print(head1.find_loop_start().data)
print(head1.loop_length())
# head1.display()