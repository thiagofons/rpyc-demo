import rpyc
import sys
import os
import time




if len(sys.argv) < 2:
  exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server,18861)

n = 10000

vector = [i for i in range(0, n)]

for i in range(10):
  start = time.time()
  sum = conn.root.sum_vector(vector)
  end = time.time()

  elapsed_time = end - start
  print(f"{elapsed_time:.2f}")