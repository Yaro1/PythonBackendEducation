class CustomList(list):
    def __to_one_size__(self, other):
        diff_size = len(self) - len(other)
        tmp_self, tmp_other = self.copy(), other.copy()
        if diff_size > 0:
            tmp_other.extend([0]*diff_size)
        elif diff_size < 0:
            tmp_self.extend([0]*-diff_size)
        return tmp_self, tmp_other

    def __add__(self, *args, **kwargs):
        other = list(args[0])
        tmp_self, tmp_other = self.__to_one_size__(other)
        return CustomList([i + j for i, j in zip(tmp_self, tmp_other)])

    def __sub__(self, other):
        tmp_self, tmp_other = self.__to_one_size__(other)
        return CustomList([i - j for i, j in zip(tmp_self, tmp_other)])

    def __eq__(self, other):
        return sum(self) == sum(other)


c_l_1 = CustomList([1])
print([1, 2] + c_l_1)
print(c_l_1 + [1, 2])
