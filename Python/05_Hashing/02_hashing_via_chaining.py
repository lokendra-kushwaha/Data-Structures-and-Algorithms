class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Empty Linked List -> 0 Nodes (Head = None)
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self):
        curr = self.head
        result = ''

        while curr is not None:
            result += str(curr.key) + ' -> ' + str(curr.value) + ', '
            curr = curr.next

        # Slicing [:-3] removes the trailing ' -> ' (changed to [:-2] for better formatting)
        if len(result) > 0:
            return result[:-2]
        return result

    def size(self):
        temp = self.head
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next
        return counter

    def append(self, key, value):
        new_node = Node(key, value)
        
        # Edge Case: If the list is completely empty
        if self.head is None:
            self.head = new_node
            self.n += 1
            return

        # Traversal to find the last node
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        # Connect the last node to the new node
        curr.next = new_node
        self.n += 1

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head is None:
            raise IndexError("Cannot delete head from an empty linked list")
        
        # Move head pointer to the second node, severing the first
        self.head = self.head.next
        self.n -= 1

    def remove(self, key):
        if self.head is None:
            raise ValueError(f"LinkedList.remove(x): {key} not in list")

        # Case: If the item to be removed is at the head
        if self.head.key == key:
            self.delete_head()
            return

        curr = self.head

        # Traverse, looking one node ahead (curr.next.key) to maintain the link
        while curr.next is not None:
            if curr.next.key == key:
                break
            curr = curr.next
 
        # Case 1: Item not found (reached the end)
        if curr.next is None:
            raise ValueError(f"LinkedList.remove(x): {key} not in list")
        # Case 2: Item found, bypass it to remove it from the chain
        else:
            curr.next = curr.next.next
            self.n -= 1

    def search(self, key):
        curr = self.head
        pos = 0

        while curr is not None:
            if curr.key == key:
                return pos
            curr = curr.next
            pos += 1

        return -1  # Fixed indentation here

    def get_node_at_index(self, index):
        temp = self.head
        counter = 0
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next  # Fixed indentation here
            counter += 1      # Fixed indentation here
        return None

    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr is not None:
            if pos == index:
                return curr.value 
            curr = curr.next       
            pos += 1               

        raise IndexError("Linked List index out of bounds")


class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # Create array of Linked List
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        List = []
        for _ in range(capacity):
            List.append(LinkedList())
        return List

    def __len__(self):
        return self.size

    def __str__(self):
        result = ''
        for linked_list in self.buckets:
            result += linked_list.__str__()

        if len(result) > 0:
            return '{' + result + '}'
        return '{}'

    def put(self, key, value):
        bucket_index = self.hash_function(key)

        node_index = self.get_node_index(bucket_index, key)
        if node_index == -1:
            # insert
            self.buckets[bucket_index].append(key, value)
            self.size += 1
    
            load_factor = self.size / self.capacity
            if load_factor >= 2:
                self.rehash()
        else:
            # update
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value

    def get_node_index(self, bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        bucket_index = self.hash_function(key)

        res = self.buckets[bucket_index].search(key)
        if res == -1:
            raise ValueError("Not present")
        else:
            node = self.buckets[bucket_index].get_node_at_index(res)
            return node.value

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)
        self.size -= 1

    def rehash(self):
        self.capacity = self.capacity * 2
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        for linked_list in old_buckets:
            for node in range(linked_list.size()):
                node_index = linked_list.get_node_at_index(node)
                key_item = node_index.key
                value_item = node_index.value
                self.put(key_item, value_item)

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity


# ---------------------------------------------
# Testing Code
# ---------------------------------------------
D = Dictionary(3)

D.put('python', 34)
D.put('c', 1000)
D.put('c++', 10000)
D.put('ruby', 20000)
D.put('java', 56)
D.put('js', 56)
D.put('html', 56)
D.put('css', 56)
D.put('cuda', 56)

D['php'] = 120

print(D.buckets[0])
print(D['php'])
print(D['c'])

del D['c']

print(D)
print(len(D))