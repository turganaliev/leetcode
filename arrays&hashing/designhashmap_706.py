class MyHashMap:

    def __init__(self):
        self.dict = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        return self.dict[key]

    def remove(self, key: int) -> None:
        self.dict[key] = -1
