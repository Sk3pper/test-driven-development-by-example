class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        
    def setUp(self):
        pass
    

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name=name)
        
    def setUp(self):
        self.wasSetUp = 1
        
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
    TestCaseTest("testSetup").run()
