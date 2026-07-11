class LRUCache:

    class DNode:
        def __init__(self, val=0, key=0, next=None, prev=None):
            self.val = val
            self.key = key
            self.next = next
            self.prev = prev

    def _remove_node(self, node: DNode):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_to_head(self, node: DNode):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.head, self.tail = self.DNode(), self.DNode()
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove_node(node)
        self._add_to_head(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) + 1 > self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove_node(self.tail.prev)

            new_node = self.DNode(value, key)
            self.cache[key] = new_node

            self._add_to_head(new_node)

        else:
            node = self.cache[key]
            node.val = value
            
            self._remove_node(node)
            self._add_to_head(node)
        
