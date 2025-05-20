class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()

        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            if e.args: print(e)
            result.testFailed()

        self.tearDown()
        return result
        
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
        
    def testBrokenMethod(self):
        raise Exception
    
class BrokenSetUpWasRun(WasRun):
    def setUp(self):
        self.log = "Error setUp "

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    def testTemplateMethod(self):
        test = WasRun("testMethod") 
        test.run()
        assert("setUp testMethod tearDown " == test.log)
        
    def testResult(self):
        test = WasRun("testMethod") 
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
        
    def testFailedResult(self):
        test = WasRun("testBrokenMethod") 
        result = test.run()
        assert("1 run, 1 failed" == result.summary())
        
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
        
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        test.run()
        assert("Error setUp testMethod tearDown " == test.log)
        
class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    
    def testStarted(self):
        self.runCount += 1
        
    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
        
if __name__ == "__main__":
    result = TestCaseTest("testTemplateMethod").run()
    print("testTemplateMethod: \t\t{result}".format(result=result.summary()))
    
    result = TestCaseTest("testResult").run()
    print("testResult: \t\t\t{result}".format(result=result.summary()))
    
    result = TestCaseTest("testFailedResultFormatting").run()
    print("testFailedResultFormatting: \t{result}".format(result=result.summary()))
    
    result = TestCaseTest("testFailedResult").run()
    print("testFailedResult: \t\t{result}".format(result=result.summary()))
    
    result = TestCaseTest("testSetUpError").run()
    print("testSetUpError: \t\t{result}".format(result=result.summary()))
    