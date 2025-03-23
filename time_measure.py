from timeit import timeit


def memorize(func, memory=None):
    if memory is None:
        memory = {}

    def wrapper(num_f):
        res = memory.get(num_f)
        if res is None:
            res = func(num_f)
            memory[num_f] = res
        return res

    return wrapper


@memorize
def func_fib_1(num):
    if num < 2:
        return num
    return func_fib_1(num - 1) + func_fib_1(num - 2)


@memorize
def func_fib_2(num):
    if num < 3:
        return 1
    return func_fib_1(num - 1) + func_fib_1(num - 2)


if __name__ == '__main__':
    n = 10
    print(func_fib_1(n))
    print('====================================')
    print(func_fib_2(n))
    print('====================================')
    print(f"Exec time for func_fib_1: "
          f"{timeit('func_fib_1(n)', globals=globals())}")
    print('====================================')
    print(f"Exec time for func_fib_2: "
          f"{timeit('func_fib_2(n)', globals=globals())}")
