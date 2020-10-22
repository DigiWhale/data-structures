class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head=None):
    self.head = head
    self.length = 0 

  def add(self, data):
    # write your code to ADD an element to the Linked List
    # Pseudocode
    # Make a new node
    new_node = Node(data)
    # Attach to end of list
    current = self.head
    if self.head == None:
      self.head = new_node
      self.length += 1
      return
    while current.next != None:
      # Starting at self.head, make a variable that continues on each next, until we reach the end (next = None)
      current = current.next
      # Set next = our new node
    current.next = new_node
    # Add 1 to length
    self.length += 1

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    if self.head == None:
      return
    # If our head matches the input data value,
    if self.head.data == data:
      # Remove the head, keeping track of head's next value
      # Set our head to the previous head's next value
      self.head = self.head.next
      # Length -= 1
      self.length -= 1
      
    # Else, we are going to remove something after the head  
    current = self.head.next
    previous = self.head
    while current != None:
      if current.data == data:
        previous.next = current.next
        self.length -= 1
        return
      previous = current
      current = current.next
    

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    current = self.head
    while current != None:
      if current.data == element_to_get:
        print(current)
      current = current.next

  def display(self):
    """Return a string of all values separated by commas"""
    output = ''
    current = self.head
    while current != None:
      output += str(current.data) + ', '
      current = current.next
    print(output)

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data=None):
    self.data = data
    self.next = None
    
ll = LinkList()
ll.display()
ll.add(4)
ll.display()
ll.add(7)
ll.display()
ll.add(2)
ll.get(2)
ll.display()
ll.remove(7)
ll.display()
ll.remove(4)
ll.display()
