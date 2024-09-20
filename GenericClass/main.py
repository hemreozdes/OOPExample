from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

# Interface IStack
class IStack(Generic[T], ABC):
    
    @abstractmethod
    def push(self, item: T):
        pass
    
    @abstractmethod
    def pop(self) -> T:
        pass
    
    @abstractmethod
    def peek(self) -> T:
        pass

class LinkedListStack(IStack[T]):
    
    def __init__(self):
        self.collection = []  # Collection to hold the stack items (using a list as a LinkedList representation)
    
    def push(self, item: T):
        self.collection.append(item)
    
    def pop(self) -> T:
        if not self.collection:
            raise IndexError("Pop from an empty stack")
        return self.collection.pop()
    
    def peek(self) -> T:
        if not self.collection:
            raise IndexError("Peek from an empty stack")
        return self.collection[-1]

class ListStack(IStack[T]):
    
    def __init__(self):
        self.collection = []  # Collection to hold the stack items
    
    def push(self, item: T):
        self.collection.append(item)
    
    def pop(self) -> T:
        if not self.collection:
            raise IndexError("Pop from an empty stack")
        return self.collection.pop()
    
    def peek(self) -> T:
        if not self.collection:
            raise IndexError("Peek from an empty stack")
        return self.collection[-1]

# Example Usage
if __name__ == "__main__":
    linked_stack = LinkedListStack[int]()  # Stack of integers
    linked_stack.push(10)
    linked_stack.push(20)
    print(linked_stack.peek())
    print(linked_stack.pop())
    print(linked_stack.peek())
#The generic structure allows us to use the same functions with variable data types.
    list_stack = ListStack[str]()  # Stack of strings
    list_stack.push("Hello")
    list_stack.push("World")
    print(list_stack.peek()) 
    print(list_stack.pop())    
    print(list_stack.peek())  
