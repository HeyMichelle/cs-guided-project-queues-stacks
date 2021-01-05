class Stack: 
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        last_item = self.items.pop()
        return last_item

    # to remove an end item of an array in python: pop()
    # popping the last item is average O(1) worst case
    # appending is also O(1) avg worst case

    ##### Below is attempt using linked list, which is more efficient, but sometimes not what they want to see in an interview. The above code is done with an ARRAY #####
    
    # class LinkledListNode:
    #     def __init__(self, data):
    #         self.data = data
    #         self.next = None

    # class Stack:
    #     def __init__(self):
    #         self.top = None

    #     def push(self, item):
    #         # create a new LL node
    #         new_node = LinkedListNode(item)
    #         # point new node to the current top of the stack
    #         new_node.next = self.top
    #         # set the TOP variable to the new node
    #         self.top = new_node

    #     def pop(self):
    #         # don't remove anything from an empty stack
    #         if self.top is None:
    #             return None
            
    #         old_top = self.top
    #         self.top = old_top.next

    #         old_top.next = None # optional
    #         return old_top.data

    # # Why bother about linked lists to implement a stack or when dealing with qeues and stacks? Why is it more efficient over any other data structure? 
    #     # Because we are utlizing to adding/inserting to the front or back of a linked list
    #     # Not efficient to insert into the middle of any data structure
    #     # You don't have to shift everything around in front or back
    #     # Stacks are only added to in the front
    #     # Qeues, only removing from the front and adding to the back
