from functools import wraps
import time


def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f'{method.__name__}: {((te-ts)*1000):.2f} ms')
        return result

    return timed
