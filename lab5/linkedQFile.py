class Node:
    def __init__(self, value):
        self.value = value  # Värdet som noden innehåller
        self.next = None  # Referens till nästa nod i listan


class LinkedQ:
    def __init__(self):
        self._first = None  # Referens till den första noden i kön
        self._last = None  # Referens till den sista noden i kön

    def enqueue(self, item):
        new_node = Node(item)
        if self.isEmpty():  # om kön är tom
            self._first = new_node  # skapar en ny nod
            self._last = new_node
        else:   # om kön inte är tom
            self._last.next = new_node
            self._last = new_node  # knyter den nya noden till slutet av kön

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            value = self._first.value  # hämtar value (data) från första noden i kön
            self._first = self._first.next
            if self._first is None:
                self._last = None  # om första noden är tom så är sista noden också tom
            return value

    def check_length(self):
        # Skapar ny noder i kön
        count = 0
        current = self._first
        while current is not None:
            count += 1
            current = current.next
        return count

    """def size(self):
        count = 0
        current = self._first
        while current is not None:
            count += 1
            current = current.next
        return count"""

    def isEmpty(self):
        # Kollar om kön är tom
        return self._first is None