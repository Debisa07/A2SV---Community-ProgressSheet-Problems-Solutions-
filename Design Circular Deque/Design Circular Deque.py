class MyCircularDeque:

    def __init__(self, k: int):
        self._data = []
        self.size = 0
        self.full_size = k
    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self._data.insert(0,value)
        self.size += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self._data.append(value)
        self.size += 1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self._data.remove(self._data[0])
        self.size -= 1
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self._data.pop()
        self.size -= 1
        return True
    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self._data[0]
    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self._data[-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size >= self.full_size