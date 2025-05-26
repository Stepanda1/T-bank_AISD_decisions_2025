import sys

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    stack = MinStack()
    result = []

    for _ in range(n):
        command = sys.stdin.readline().strip().split()
        if command[0] == '1':
            stack.push(int(command[1]))
        elif command[0] == '2':
            stack.pop()
        elif command[0] == '3':
            result.append(str(stack.get_min()))

    sys.stdout.write("\n".join(result) + "\n")

