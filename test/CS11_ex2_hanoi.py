#http://courses.cms.caltech.edu/cs11/material/python/lab2/lab2.html

'''
thoughts
1. So a class can be store in a[0] as long as I define the lists "a"
# Seemed this is not the good way to use class
'''

from sys import argv

script, n = argv


class hanoi:

    def __init__(self, n):
        self.stack = [0, 1, 2]
        self.stack[0] = []
        self.stack[1] = []
        self.stack[2] = []
        for i in range(n, 0, -1):
            self.stack[0].append(i)

        self.display()
        print("\n")
        self.solve(n, 0, 1, 2)

    def display(self):
        for i in range(0, 3):
            print(self.stack[i])
            # print(i + ":  ")

    def solve(self, n, init, temp, dest):
        if n == 1:
            self.move(init, dest)
            return

        self.solve(n - 1, init, dest, temp)
        self.move(init, dest)
        self.solve(n - 1, temp, init, dest)

    def move(self, init, dest):
        temp = self.stack[init].pop()
        self.stack[dest].append(temp)
        self.display()
        print("\n")
        # assert
        self.assertMethod()

    def assertMethod(self):
        for i in range(0, 3):
            assert self.stack[i] == sorted(self.stack[i], reverse=True)

a = hanoi(4)
