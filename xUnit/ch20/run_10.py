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
        self.log = "setUp "
        
    def testMethod(self):
        self.log = self.log + "testMethod "
        
class TestCaseTest(TestCase):
    def setUp(self):
        # We can create the WasRun in setUpm and use it in the test methods. Each test method is run in a clean instance of TestCaseTest, so there is no way the two tests can be coupled.
        self.test = WasRun("testMethod")
        
    def testTemplateMethod(self):
        test = WasRun("testMethod") 
        test.run()
        assert("setUp testMethod " == test.log)
        
if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
