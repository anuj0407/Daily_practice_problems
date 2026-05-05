'''
Task: Create a class ReverseIter that takes a list and iterates through it backwards.
Requirement: Do not use reversed() or [::-1]. Implement __iter__ and __next__.
'''
class ReverseIter:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        
        curr_item = self.data[self.index]
        self.index -= 1
        return curr_item

# Execution
it = ReverseIter([1, 2, 3])
for x in it:
    print(x , end = " ") 
