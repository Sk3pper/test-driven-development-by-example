class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        result = TestResult()
        result.testStarted()

        try:
            self.setUp()
        except Exception as e:
            if e.args: print(e)
            result.testHaveSetUpError()
            result.testFailed()

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
        self.log = ""
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
        raise Exception

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
        assert("1 run, 0 failed (setUp: OK)" == result.summary())
        
    def testFailedResult(self):
        test = WasRun("testBrokenMethod") 
        result = test.run()
        assert("1 run, 1 failed (setUp: OK)" == result.summary())
        
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed (setUp: OK)" == result.summary())
        
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        result = test.run()
        assert("1 run, 1 failed (setUp: ERROR)" == result.summary())
        
class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        self.setUpError = False
    
    def testStarted(self):
        self.runCount += 1
        
    def testFailed(self):
        self.errorCount += 1
        
    def testHaveSetUpError(self):
        self.setUpError = True

    def summary(self):
        setUpStatus = "ERROR" if self.setUpError else "OK"
        return "%d run, %d failed (setUp: %s)" % (self.runCount, self.errorCount, setUpStatus)
        
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
    