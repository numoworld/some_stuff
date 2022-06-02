class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def appendleft(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current_node = self._get_current_node()
        current_node.next = node

    def insert_after(self, target_data, data):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_data:
                new_node = Node(data)
                new_node.next= node.next
                node.next = new_node
                return
        raise Exception('Node not found')

    def insert_before(self, target_data, data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_data:
            return self.appendleft(data)

        prev_node = self.head
        for node in self:
            if node.data == target_data:
                new_node = Node(data)
                new_node.next = node
                prev_node.next= new_node
                return
            prev_node = node
        raise Exception('Node not found')

    def remove(self, target_data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception('Node not found')

    def _get_current_node(self):
        for current_node in self:
            pass
        return current_node

    def __getitem__(self, key):
        if self.head is None:
            raise Exception('List is empty')

        c = 0
        for node in self:
            if key == self:
                return node.data
            c += 1

        raise IndexError('Index out of range')

    def reverse(self):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.next is None:
            return

        prev_node = None
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        self.head = prev_node


    def __len__(self):
        c = 0
        for node in self:
            c += 1
        return c

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)
