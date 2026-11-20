class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.index = {}
        print("INIT")

    def get(self, key: int) -> int:
        print("GET START, key = ", key)
        if key not in self.index:
            return -1

        fetched_node = self.index[key]
        self.remove(fetched_node.key)

        most_recent: ListNode = self.head.next

        new_node = ListNode(fetched_node.val, fetched_node.key, most_recent, self.head)
        self.head.next = new_node
        most_recent.previous = new_node
        self.index[key] = new_node
        self.size += 1

        print("GET END, key = ", key)

        return fetched_node.val

    def put(self, key: int, value: int) -> None:
        print("PUT START, key = ", key)
        new_node = ListNode(value=value, key=key)

        # case-1 : first node
        if self.capacity == 0:
            self.head.next = new_node
            new_node.previous = self.head
            new_node.next = self.tail
            self.tail.previous = new_node
            self.index[key] = new_node
            self.size += 1
            return

        # case-2 : capacity full, new node
        if self.capacity == self.size:
            to_removed = self.tail.previous
            self.remove(to_removed.key)

        # case-3 : update node
        if key in self.index:
            fetched_node: ListNode = self.index[key]
            self.remove(fetched_node.key)

        most_recent = self.head.next

        self.head.next = new_node
        new_node.previous = self.head
        
        
        most_recent.previous = new_node
        new_node.next = most_recent
        self.index[key] = new_node
        self.size += 1
        print("PUT END, key = ", key)
        if key==3:
            print(self.index.keys())
        return
    
    def remove(self, key: int) -> None:
        print("REMOVE START, key = ", key)
        to_removed: ListNode = self.index[key]

        next_node: ListNode = to_removed.next
        previous_node: ListNode = to_removed.previous

        previous_node.next = next_node
        next_node.previous = previous_node
        self.index.pop(key)
        self.size -= 1



class ListNode:
    def __init__(self, value: int, key: int | None = None, next: any | None = None, previous: any | None = None):
        self.val = value
        self.key = key
        self.next = next
        self.previous = previous