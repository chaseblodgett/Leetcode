class MyQueue(object):

    def __init__(self):
        self.arr = []
        self.front = 0
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        self.size += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.size > 0:
            self.size -= 1
            elem = self.arr[self.front]
            self.front += 1
            return elem
    def peek(self):
        """
        :rtype: int
        """
        if self.size > 0:
            return self.arr[self.front]

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0