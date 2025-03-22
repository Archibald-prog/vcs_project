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
