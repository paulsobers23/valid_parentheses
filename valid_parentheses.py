class Stack:
  def __init__(self):
    self.items = []
      
  def isEmpty(self):
    return self.items == []
      
  def push(self,item):
    self.items.append(item)
    
  def pop(self):
    if self.isEmpty():
        raise IndexError('This stack is empty.')
    return self.items.pop()

  def size(self):
    return len(self.items)
    

def valid_parentheses(string):
  pairs = {
    ")": "(",
    "}": "{",
    "]": "["
   }
  stack = Stack()
  for char in string:
    if char in "({[":
      stack.push(char)
    elif stack.isEmpty() or pairs[char] != stack.pop():
      return False
  return True


