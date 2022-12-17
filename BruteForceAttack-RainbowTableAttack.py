import itertools
import hashlib
import string
import sys
import time


characters = string.ascii_lowercase
target_hash = '' #MD5

count = 0

start_time = time.perf_counter()

while True:
    count += 1
    for password in itertools.product(characters, repeat=count):
        password = ''.join(password)
        create_hash = hashlib.md5(password.encode()).hexdigest()

        if create_hash == target_hash:
            print('PASS: ' + password)
            end_time = time.perf_counter()
            print('処理時間: ' + str(round(end_time-start_time, 2)) + '秒')
            sys.exit()
