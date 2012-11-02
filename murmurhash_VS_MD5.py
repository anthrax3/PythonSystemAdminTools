import time
import random
import string
from hashlib import md5
from sklearn.utils import murmurhash3_32

digits = string.lowercase + string.uppercase + string.digits

def test_murmurhash_sklearn(iterable):
    [ murmurhash3_32(item) for item in iterable ]

def test_md5_hexdigest(iterable): # mask global variables
    [ md5(item).hexdigest() for item in iterable ]

def timeit(func, *args, **kwargs): #higher order function
    now = time.clock()
    func(*args, **kwargs)
    return time.clock() - now

# start generator
gen_str = (''.join(random.sample(digits, 10)) for _ in range(1000000))

print timeit(test_md5_hexdigest, gen_str)

# start generator
gen_str = (''.join(random.sample(digits, 10)) for _ in range(1000000))

print timeit(test_murmurhash_sklearn, gen_str)
