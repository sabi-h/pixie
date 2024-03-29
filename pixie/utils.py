import math
import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print( '%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


def nCr(n,r):
    f = math.factorial
    return int(( f(n) / f(r) ) / f(n-r))