from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    pool = Pool(processes=4)
    result = pool.apply_async(f, [214257325934876 ** 231])
    print result.get(timeout=1)
    print pool.map(f, range(10))
