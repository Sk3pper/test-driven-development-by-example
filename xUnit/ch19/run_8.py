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
        TestCase.__init__(self, name=name)
        
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    
    def testMethod(self):
        self.wasRun = 1
        
class TestCaseTest(TestCase):
    def setUp(self):
        # We can create the WasRun in setUp and use it in the test methods. Each test method is run in a clean instance of TestCaseTest, so there is no way the two tests can be coupled.
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
        
    def testSetup(self):
        self.test.run()
        assert(self.test.wasSetUp)
        
if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetup").run()
