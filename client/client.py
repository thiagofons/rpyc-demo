import rpyc
import sys
import os
import time

if len(sys.argv) < 2:
  exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

timeout_seconds = 60
conn = rpyc.connect(server, 18861, config={"sync_request_timeout": timeout_seconds})

n = 10000

vector: list[int] = [i for i in range(0, n)]

start = time.time()
sum = conn.root.exposed_sum_vector(vector)  
end = time.time()

elapsed_time = end - start
print(f"{elapsed_time:.2f}")