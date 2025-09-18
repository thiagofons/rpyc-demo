import rpyc
import time

class MyService(rpyc.Service):
  def on_connect(self, conn):
    print("CONECTADO: ", conn)
    pass

  def on_disconnect(self, conn):
    pass

  def exposed_get_answer(self): 
    return 42
  
  def exposed_sum_vector(self, vector: list[int]): 
    start = time.time()

    sum_val = 0
    for item in vector:
        sum_val += item

    end = time.time()

    elapsed_time = end - start
    print(f"{elapsed_time:.2f}")

    return sum_val

  exposed_the_real_answer_though = 43 
  
  def get_question(self): # este método não é exposto
    return "Qual é a cor do cavalo branco de Napoleão?"
  
if __name__ == "__main__":
  from rpyc.utils.server import ThreadedServer

  t = ThreadedServer(MyService, port=18861)
  t.start()