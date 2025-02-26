class stack:
    def __init__(self):
        self.Element = []
    def push(self, value):
        self.Element.append(value)
    def pop(self):
        return self.Element.pop()
    def empty(self):
        return self.Element == []
    def show(self):
        for value in reversed(self.Element):
            print(value)

def bottomInsert(s, value):
    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        bottomInsert(s, value)
        s.push(popped)

def reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        reverse(s)
        bottomInsert(s, popped)


stk = stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Stack is ")
stk.show()


print("Reversed Stack is ")
reverse(stk)
stk.show()


