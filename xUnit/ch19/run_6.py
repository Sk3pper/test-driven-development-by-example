class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name=name)
    
    def testMethod(self):
        self.wasRun = 1
        
class TestCaseTest(TestCase):

    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
        
    def testSetup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)
        
if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetup").run() # [ok] AttributeError: 'WasRun' object has no attribute 'wasSetUp'
