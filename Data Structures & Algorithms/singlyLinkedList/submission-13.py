class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None 

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:  
        if self.head is None:
            return -1
        if index == 0 and self.head is not None:
            return self.head.value
        count = 1 
        current = self.head
        while current.next is not None:
            if index == count:
                return current.next.value
            count += 1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        if self.head is None:
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head
            
    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)
            self.tail = current.next

    def remove(self, index: int) -> bool:
        if self.get(index) == -1:
            return False
        removed_value = self.get(index)
        if self.head.value == removed_value:
            self.head = self.head.next
            return True
        current = self.head

        while current.next is not None:
            if current.next.value == removed_value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values
        
        
