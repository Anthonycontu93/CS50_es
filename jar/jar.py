class Jar:
    def __init__(self, capacity=12, size=0):
        """ initialize the new object """

        self.capacity = capacity
        self.size = size

    def __str__(self):
        """ print out the numbers og cookies into the jar"""

        return "🍪" * self.size


    def deposit(self, n):
        """ calculate if the deposit is > then the capacity"""
        if n + self.size > self.capacity:
            raise ValueError("The number of cookies can't be > then the capacity")
        else:
            self.size = self.size + n
    # this are method, which is a function, callable from your object line 65
    def withdraw(self, n):
        """ calculate if the withdrw is > then the size"""
        if n > self.size:
            raise ValueError("The number of cookies withdraw can't be > then the size")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        """ Getter """
        return self._capacity


    @property
    def size(self):
        """ Getter """
        return self._size

    # setter aren't function. You need to use them as variables line 62
    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError("Capacity can't be 0 or negative")
        self._capacity = value



    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size can't be > then capacity")
        else:
            self._size = size




def main():

    jar = Jar()
    print(jar)
    jar.capacity = 20
    jar.deposit(15)
    jar.deposit(3)
    jar.withdraw(12)
    print(jar)


if __name__ == "__main__":
    main()