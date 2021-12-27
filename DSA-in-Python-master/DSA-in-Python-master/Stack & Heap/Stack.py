#--------------- STACK DATA STRUCTURE -----------------------

# Stack follows the principle of Last In First Out(LIFO) which means element which is added last will be accessed first.
# It's like a pile of books where we will pick top book of the pile which was put last on the pile hence LIFO
# Common use case of Stack is like UNDO and BROWSER BACK button functionality where thing which was accessed last will be processed first or reversing the string/filename etc.
# Both PUSH and POP in a stack will work at the same end, which is the top of the stack. 

#--------- Common Operations involving STACK --------------

# S.push(e): Add element e to the top of stack S;an error occurs if the stack is full
# S.pop(): Remove and return the top element from the stack S;an error occurs if the stack is empty.
# S.top/peek(): Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
# S.is_empty( ): Return True if stack S does not contain any elements.
# S.is_full(): Return true if Stack S is full
# len(S): Return the number of elements in stack S; in Python,

# All above operations have time complexity of O(1) and space complexity of O(n) since we need n space in memory to hols stack of n length

# ----------Implementation in Python -----------------

class Stack:
    
    def __init__(self):
        """Create a new stack"""
        
        self.stack = []
        
    def push(self,data):
        """Add a element to the stack"""
        
        self.stack.append(data)
    
    def pop(self):
        """Remove the top element of the stack"""
        
        if self.is_empty():
            raise Exception("Nothing to pop")
        
        return self.stack.pop()
    
    def peek(self):
        """Have a look at top element of the stack"""
        
        if self.is_empty():
            raise Exception("Nothing to peek")
        
        return self.stack[len(self.stack) - 1]
    
    def is_empty(self):
        """Returns true if stack is empty"""
        return len(self.stack) == 0
    
    def size(self):
        """Returns size of the stack"""
        return len(self.stack)
stack1 =Stack()
stack1.push(20)
print(stack1.stack)
