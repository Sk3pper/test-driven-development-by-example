class WasRun:
    def __init__(self, name):
        self.wasRun = None
    
    def testMethod(self):
        self.wasRun = 1
        
if __name__ == "__main__":
    # first raw WasRun test
    test = WasRun("testMethod")
    print(test.wasRun)
    test.testMethod()
    print(test.wasRun)
