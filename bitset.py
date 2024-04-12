# C++ bitset implementation in Python
# following are supported operations
# set, reset, flip, count, test, any, none, all, size, to_string


class BitSet:
    """This class mimic the c++ bitset functionalities
    """
    def __init__(self, size: int, initial_value=None) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError(f"Invalid size provided: {size}")
        if initial_value is not None:
            if isinstance(initial_value, str):
                temp = list(map(int, initial_value))
                if len([item for item in temp if item not in (0, 1)]) > 0:
                    raise ValueError("Invalid value provided")
                rem = []
                if len(temp) < size:
                    rem = [0] * (size - len(temp))
                self._arr = rem + temp
            elif isinstance(initial_value, int):
                self._arr = BitSet.decimal_to_binary(initial_value, size)
            else:
                raise ValueError("Invalid value provided")
            if size and len(self._arr) > size:
                raise ValueError(f"size {size} must be greater than binary value of {initial_value}")
        else:
            self._arr = [0] * size
        self._size = size
        self._count = sum(self._arr)

    @staticmethod
    def decimal_to_binary(num, size):
        res = ""
        while num > 0:
            res += str(num%2)
            num /= 2
        while len(res) < size:
            res += "0"
        return list(map(int, res[::-1]))

    @staticmethod
    def _get_index(index):
        return -(index+1)

    def size(self) -> int:
        return self._size

    def count(self) -> int:
        return self._count
    
    def _validate_index(self, index):
        if index and index >= self.size():
            raise IndexError(f"Index out of bound: {index}")

    def set(self, index=None) -> None:
        self._validate_index(index)
        if index is None:
            for ind, value in enumerate(self._arr):
                if value == 0:
                    self._arr[ind] = 1
            self._count = self._size
        elif not self._arr[BitSet._get_index(index)]:
            self._arr[BitSet._get_index(index)] = 1
            self._count += 1
    
    def reset(self, index=None) -> None:
        self._validate_index(index)
        if index is None:
            for ind, value in enumerate(self._arr):
                if value == 1:
                    self._arr[ind] = 0
            self._count = 0
        elif self._arr[BitSet._get_index(index)]:
            self._arr[BitSet._get_index(index)] = 0
            self._count -= 1
    
    def flip(self, index=None) -> None:
        self._validate_index(index)
        if index is None:
            for ind, value in enumerate(self._arr):
                self._arr[ind] = 1 - value
            self._count = self._size - self._count
        else:
            actual_index = BitSet._get_index(index)
            self._count += (1 if self._arr[actual_index] else -1)
            self._arr[actual_index] = 1 - self._arr[actual_index]

    def test(self, index) -> bool:
        if index >= self.size():
            raise IndexError(f"Index out of bound: {index}")
        return bool(self._arr[BitSet._get_index(index)])

    def any(self) -> bool:
        return self.count() > 0
    
    def none(self) -> bool:
        return self.count() == 0

    def all(self) -> bool:
        return self.count() == self.size()

    def to_string(self) -> str:
        return "".join(list(map(str, self._arr)))

    def __repr__(self) -> str:
        return self.to_string()


# example usage
if __name__ == '__main__':
    bs = BitSet(5, "11111")
    print(bs)
    print(bs.any())
    print(bs.all())
    print(bs.none())
    print(bs.test(2))
    bs.set(2)
    print(bs)
    bs.reset(2)
    print(bs)
    bs.flip()
    print(bs.size())
    print(bs)
