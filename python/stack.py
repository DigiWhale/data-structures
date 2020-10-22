class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.stack = []
    self.total = len(self.stack)

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack.append(data)

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.pop()

  def size(self):
    # write your code that returns the size of the Stack
    return len(self.stack)


# Testing
x = Stack()
x.push(5)
x.push(2)
print(x.size())
x.pop()
print(x.size())
