class CountingClicker:
    """A Class can/should have a docstring, just like a function"""
    
    def __init__(self, count = 0):
        self.count = count 
    def __repr__(self):
        return f"CountingClicker(Count={self.count})"

    def click(self, num_times =1):
        """Click the clicker some number of tiems"""
        self.count += num_times
    def read(self):
        return self.count
    def reset(self):
        self.count = 0



clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count = 100)

clicker = CountingClicker();
assert clicker.read() == 0, "clicker should start with count 0"

clicker.click()
clicker.click()

assert clicker.read() == 2, "after two clicks, clicker should have count 2"

clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

class NoResetClicker(CountingClicker):
    def reset(self):
        pass


clicker4 = NoResetClicker()
assert clicker4.read() == 0
clicker4.click()
assert clicker4.read() == 1
clicker4.reset()
assert clicker4.read() == 1, "reset should not do anything"

print(clicker4.read())