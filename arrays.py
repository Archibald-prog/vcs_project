from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = map(lambda x: nums.index(x),
                  filter(lambda x: x % 2 == 0, nums))
    return list(new_arr)


if __name__ == '__main__':
    some_list = [3, 8, 4, 7, 5, 6, 2, 10]
    print(f"The exec time for func_1(): "
          f"{timeit('func_1(some_list)', globals=globals())}")
    print('===============================================')
    print(f"The exec time for func_2(): "
          f"{timeit('func_2(some_list)', globals=globals())}")
