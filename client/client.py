import rpyc
import sys
import os

if len(sys.argv) < 2:
  exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server,18861)

n = int(input("Insira o numero de posições do vetor: "))

vector = [i for i in range(0, n)]

print(conn.root.sum_vector(vector))