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
        
    def hasLoop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def secondLargest(self):
        if not self.head or not self.head.next:
            return None  # Not enough elements

        first = second = float('-inf')
        current = self.head

        while current:
            if current.data > first:
                second = first
                first = current.data
            elif first > current.data > second:
                second = current.data
            current = current.next

        return second if second != float('-inf') else None

    def countConsecutivePairsWithSumAtMostK(self, k):
        count = 0
        current = self.head

        while current and current.next:
            if current.data + current.next.data <= k:
                count += 1
            current = current.next

        return count
            
    def countAllPairsWithSumAtMostK(self, k):
        count = 0
        outer = self.head

        while outer:
            inner = outer.next
            while inner:
                if outer.data + inner.data <= k:
                    count += 1
                inner = inner.next
            outer = outer.next

        return count
    
    def printSecondHalf(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    # def printThirdPart(self):
    #     slow = fast = self.head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next.next
    #     temp = slow
    #     while temp:
    #         print(temp.data, end=' ')
    #         temp = temp.next
    #     print()

    def printFirstKElements(self, k):
        temp = self.head
        count = 0
        while temp and count < k:
            print(temp.data, end=' ')
            temp = temp.next
            count += 1
        print()

    def bubbleSort(self):
        end = None
        while end != self.head:
            swap = False
            prev = None
            current = self.head
            while current.next != end:
                nxt = current.next
                if current.data > nxt.data:
                    swap = True
                    current.data, nxt.data = nxt.data, current.data
                current = current.next
            if not swap:
                break
            end = current
    
    def kthLargest(self, k):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        arr.sort(reverse=True)
        return arr[k - 1] if k <= len(arr) else None


n = int(input("n: "))
ll = LinkedList()

for _ in range(n):
    ll.addNode(int(input()))

print("\nLinked List:")
ll.display()

k = int(input("\nEnter value of k: "))
count = ll.countConsecutivePairsWithSumAtMostK(k)
print("count :", count)
k = int(input("\nk: "))
count = ll.countAllPairsWithSumAtMostK(k)
print("count: ",count)

ll.printSecondHalf()

#ll.printThirdPart()

ll.printFirstKElements(k)

ll.bubbleSort()
ll.display()

ll.kthLargest(3)