class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.queue = []
    self.total = len(self.queue)

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.append(data)

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.queue.pop(0)

  def size(self):
    # write your code that returns the size of the Queue
    return len(self.queue)

x = Queue()
x.enqueue(5)
print(x.size())
x.dequeue()
print(x.size())