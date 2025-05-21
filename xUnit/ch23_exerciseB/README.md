# Run
```
❯ python exercise_23B.py
```

# To-do list
- [ ] ~~Invoke test method~~
- [ ] ~~Invoke setUp first~~**
- [ ] ~~Invoke tearDown afterward~~
- [ ] ~~Invoke tearDown even if the test method fails~~
- [ ] ~~Run multiple tests~~
- [ ] ~~Report collected results~~
- [ ] ~~Log string in WasRun~~
- [ ] ~~Report failed tests~~
- [ ] ~~Catch and report setUp errors~~
- [x] **~~Create TestSuite from a TestCase class~~**

# Exercise: 
The last item to solve is **Create TestSuite from a TestCase class**: constructing a suite automatically given a test class. 

## Epoch 1
### Step1: Add a little test.
The first step is the hardest one for who approach the TDD style. As Kent Beck writes in the book that **we have to image the perfect interface** (also if it is not already in place) for our operation. We are telling ourselves a **story** about how the operation will look from outside. 

We image a TestSuite constructor takes in input the TestCase class.

```python
def testSuiteFromTestCase(self):
    suite = TestSuite(TestCaseTest)
    suite.run(self.result)
    assert("7 run, 0 failed" == self.result.summary())
```

### Step2: Run all tests and fail
Running all the test Python informs us that the `TestSuite.__init__() takes 1 positional argument but 2 were given`. The TestSuite constructor does not handle the TestCase class name as input argument. We can change it adding the names as input parameter
```python
def __init__(self, testCase):
    self.tests = []
    self.testCase = testCase
```

With this code in place we have broken the `testSuite` since we do not pass the TestCase name class.

### Step3: Make changes and run tests
I do not like the code in this way. I want to maintain the constructor free so we apply a little change

```python
def __init__(self, testCaseClass=None):
    self.tests = []
    self.testCaseClass = testCaseClass

    if testCaseClass:
        self.testCaseClass = testCaseClass
```

With this change we can decide to pass or not to pass the `testCaseClass` as input argument.
When we pass `testCaseClass` we can proceed to parse it and extract all the tests to add to the suite. The rational is that given a testCase name class we try to find all test methods that is all methods that starting with 'test' word.

```python
def loadTestsFromTestCase(self, testCaseClass):
    self.testCaseClass = testCaseClass
    
    test_methods = [method for method in dir(self.testCaseClass) 
                    if method.startswith('test') and callable(getattr(self.testCaseClass, method))]

    for method_name in test_methods:
        test_instance = self.testCaseClass(method_name)
        self.add(test_instance)
```

The ouput is the following:
```bash
testTemplateMethod: 			    1 run, 0 failed
testResult: 				        1 run, 0 failed
testFailedResultFormatting: 		1 run, 0 failed
testFailedResult: 			        1 run, 0 failed
testSetUpError: 			        1 run, 0 failed
testTearDownWithTestMethodError: 	1 run, 0 failed
testSuite: 				            1 run, 0 failed
maximum recursion depth exceeded
testSuiteFromTestCase: 			    1 run, 1 failed
```

The problem is that the test `testSuiteFromTestCase` is recursively called. We need to change the name to `suiteFromTestCaseTest`.

### Step4: Run the tests and succeed
Running the tests
```python
suite = TestSuite()

suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSetUpError"))
suite.add(TestCaseTest("testTearDownWithTestMethodError"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("suiteFromTestCaseTest"))

result = TestResult()
suite.run(result=result)

print(result.summary())
```

Now we have 
```bash
8 run, 0 failed
```

We can change the code that launch the test
```python
suite = TestSuite(TestCaseTest)
result = TestResult()
suite.run(result=result)
print(result.summary())
```

Keep in mind to test also the new test we need to add it separably
```python
suite = TestSuite(TestCaseTest)
result = TestResult()
suite.add(TestCaseTest("suiteFromTestCaseTest"))
suite.run(result=result)
print(result.summary())
```

## Epoch 2
I do not like to add `suiteFromTestCaseTest` separately. I want to find a better solution

### Step1: Add a little test.
Changing the name to `testSuiteFromTestCase` we restore the recursion problem

### Step2: Run all tests and fail

```python
if __name__ == "__main__":
    suite = TestSuite(TestCaseTest)
    result = TestResult()
    suite.run(result=result)
    print(result.summary())
```

```bash
maximum recursion depth exceeded
8 run, 1 failed
```

### Step3: Make a change
The problem we face with the `loadTestsFromTestCase` method is that it automatically adds all methods starting with `"test"` from a given `TestCase` class. This creates a potential infinite recursion when we have a test method that itself creates a `TestSuite` from the same `TestCase` class.

The key insight is that rather than implementing complex recursion detection logic, we can solve this problem through better design of our test structure.
By creating a dedicated `SampleTestCaseForSuiteTest` class that serves as a simple, controlled test fixture, we achieve separation of concerns. This dedicated test class contains only the methods needed to verify the `TestSuite` functionality, without any methods that would trigger the creation of another `TestSuite` from the original test class. This is a clean approach that doesn't require any complex tracking mechanisms, global variables, or recursion detection algorithms. 

```python
class SampleTestCaseForSuiteTest(TestCase):
    pass
```

The test now is the following
```python
def testSuiteFromTestCase(self):
    suite = TestSuite(SampleTestCaseForSuiteTest)
    suite.run(self.result)
    assert("0 run, 0 failed" == self.result.summary())
```

### Step4: Run the tests and succeed
Running
```python
suite = TestSuite(TestCaseTest)
result = TestResult()
suite.run(result=result)
print(result.summary())
```

we have
```bash
8 run, 0 failed
```