import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["orders","products","customers","reviews","cancels"]

def my_func(i):
    wait = random.randint(1,10)
    time.sleep(wait)
    print("Table Name:",i," Processing Time:",wait,"seconds")

# SEQUENTIAL
print("SEQUENTIAL EXECUTION")

for i in tables:
    my_func(i)

# PARALLEL
print("PARALLEL EXECUTION")

with ThreadPoolExecutor(max_workers = len(tables)) as executor:
    futures = executor.map(my_func,tables)
    # for i in tables:
    #     future = executor.submit(my_func,i)