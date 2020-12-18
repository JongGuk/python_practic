class TestModule():
    def __init__(self, name):
        self.name = name
        print("Instance [" + self.name + "] Test1.py / TestModule")

    def in_module_msg(self):
        print("Instance [" + self.name + "] Test1.py / TestModule / in_module_msg")

    def plus(self, num1, num2):
        print("[{0}] results : {1}".format(self.name, num1+num2))

# print('\033c') # clear terminal

def plus(num1, num2):
    print("Function result : {}".format(num1+num2))

# ins1 = TestModule("nnnnaaaame")
# ins1.in_module_msg()
# ins1.plus(5,3)
# ins2 = TestModule("old")
# ins2.plus(5,333)

# plus(3,3)