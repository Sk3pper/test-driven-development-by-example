class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
        except Exception as e:
            if e.args: print(e)
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
    
    def testStarted(self):
        self.runCount += 1
        
    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
    
class TestSuite:
    def __init__(self, testCaseClass=None):
        self.tests = []
        self.testCaseClass = testCaseClass

        if testCaseClass:
            self.loadTestsFromTestCase(testCaseClass)
    
    def add(self, test):
        self.tests.append(test)
    
    def loadTestsFromTestCase(self, testCaseClass):
        self.testCaseClass = testCaseClass
        
        test_methods = [method for method in dir(self.testCaseClass) 
                        if method.startswith('test') and callable(getattr(self.testCaseClass, method))]

        for method_name in test_methods:
            test_instance = self.testCaseClass(method_name)
            self.add(test_instance)
    
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
        assert("1 run, 0 failed" == self.result.summary())
        
    def testFailedResult(self):
        test = WasRun("testBrokenMethod") 
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
        
    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())
        
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
    
    def testTearDownWithTestMethodError(self):
        test = WasRun("testBrokenMethod") 
        test.run(self.result)
        assert("setUp tearDown " == test.log)
        
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

    def testSuiteFromTestCase(self):
        suite = TestSuite(SampleTestCaseForSuiteTest)
        suite.run(self.result)
        assert("0 run, 0 failed" == self.result.summary())

class SampleTestCaseForSuiteTest(TestCase):
    pass
    
def runTestSuite():
    suite = TestSuite()

    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSetUpError"))
    suite.add(TestCaseTest("testTearDownWithTestMethodError"))
    suite.add(TestCaseTest("testSuite"))
    suite.add(TestCaseTest("testSuiteFromTestCase"))
    
    result = TestResult()
    suite.run(result=result)

    print(result.summary())
    
def runSingleTests():
    res = TestResult()
    TestCaseTest("testTemplateMethod").run(res)
    print("testTemplateMethod: \t\t\t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testResult").run(res)
    print("testResult: \t\t\t\t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testFailedResultFormatting").run(res)
    print("testFailedResultFormatting: \t\t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testFailedResult").run(res)
    print("testFailedResult: \t\t\t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testSetUpError").run(res)
    print("testSetUpError: \t\t\t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testTearDownWithTestMethodError").run(res)
    print("testTearDownWithTestMethodError: \t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testSuite").run(res)
    print("testSuite: \t\t\t\t{res}".format(res=res.summary()))
    
    res = TestResult()
    TestCaseTest("testSuiteFromTestCase").run(res)
    print("testSuiteFromTestCase: \t\t\t{res}".format(res=res.summary()))

if __name__ == "__main__":
    # runTestSuite()
    # print()
    # runSingleTests()
    # print()
    suite = TestSuite(TestCaseTest)
    result = TestResult()
    suite.run(result=result)
    print(result.summary())
    
    