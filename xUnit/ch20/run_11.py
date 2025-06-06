class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name=name)
        
    def setUp(self):
        self.log = "setUp "
        
    def testMethod(self):
        self.log = self.log + "testMethod "
        
    def tearDown(self):
        self.log = self.log + "tearDown "
        
class TestCaseTest(TestCase):        
    def testTemplateMethod(self):
        test = WasRun("testMethod") 
        test.run()
        assert("setUp testMethod tearDown " == test.log)
        
if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
