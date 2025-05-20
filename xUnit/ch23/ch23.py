class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self, result):
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
    
class TestSuite:
    def __init__(self):
        self.tests = []
        
    def add(self, test):
        self.tests.append(test)
        
    def run(self, result):     
        for test in self.tests:
            test.run(result)
            
        return result

class TestCaseTest(TestCase):
    
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod") 
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
        
    def testResult(self):
        test = WasRun("testMethod") 
        test.run(self.result)
        assert("1 run, 0 failed (setUp: OK)" == result.summary())
        
    def testFailedResult(self):
        test = WasRun("testBrokenMethod") 
        test.run(self.result)
        assert("1 run, 1 failed (setUp: OK)" == result.summary())
        
    def testFailedResultFormatting(self):
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed (setUp: OK)" == result.summary())
        
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        test.run(self.result)
        assert("1 run, 1 failed (setUp: ERROR)" == result.summary())
        
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == result.summary())
        
if __name__ == "__main__":
    
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSetUpError"))
    
    result = TestResult()
    suite.run(result=result)
    
    print(result.summary())
    