# Run
```
❯ python exercise_22.py
```

# To-do list
- [ ] ~~Invoke test method~~
- [ ] ~~Invoke setUp first~~**
- [ ] ~~Invoke tearDown afterward~~
- [ ] Invoke tearDown even if the test method fails
- [ ] Run multiple tests
- [ ] ~~Report collected results~~
- [ ] ~~Log string in WasRun~~
- [ ] ~~Report failed tests~~**
- [x] **~~Catch and report setUp errors~~**

** New item

# Exercise: 
There is a subtlety hidden inside this method. The way it is written, if a disaster happens during **setUp(),** then the exception won't be caught. That can't be what we mean - we want our tests to run independently of one another. I'll leave that next test and its implementation as an exercise for you (sore fingers, again).

Make in practice what we learn so far.

### Step 0: Add print results
Before starting with the first step we have to address another big problem. When an assert is not True, since we catch all the Exception the error is not show. Let me show an example

If we edit the `testResult` assert from `assert("1 run, 0 failed" == result.summary())` to `assert("0 run, 0 failed" == result.summary())` with the code in place we do not see any error or message that tell us that something is wrong. To overcome this issue we add the following code in our test:

```python
    result = TestCaseTest("testTemplateMethod").run()
    print("testTemplateMethod: \t\t{result}".format(result=result.summary()))

    result = TestCaseTest("testResult").run()
    print("testResult: \t\t\t{result}".format(result=result.summary()))

    result = TestCaseTest("testFailedResultFormatting").run()
    print("testFailedResultFormatting: \t{result}".format(result=result.summary()))

    result = TestCaseTest("testFailedResult").run()
    print("testFailedResult: \t\t{result}".format(result=result.summary()))
```

With this change we can see that now the `testResult` is broken
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 1 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
```

Roll back to `assert("1 run, 0 failed" == result.summary())` and we have:
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 0 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
```

**Lesson learned:** the `assert` works but it does not tell us any hint about where the test code is failed.

I will propose three solutions. The first one manage the setUp error looking for the `WasRun` log, the second manage the possibility of raise exception by the `setUp ` method and the last one catch the raise exception and report it.

## Solution 1
### Step1: Add a little test.
We write a test that have a broken setUp. We need a fake `WasRun` object with a broken `setUp` method. When it is called it put Error setUp in the logs.
```python
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        test.run()
        assert("Error setUp testMethod tearDown " == test.log)
```

### Step2: Run all tests and fail.
Run the tests and we have the following print messages
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 0 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
    testSetUpError: 		    1 run, 1 failed
```

In this situation we do not have any much hint about where the `testSetUpError` test is broken but we can imagine the source root of the problem is because we do not have the `BrokenSetUpWasRun` object.

We can add for this moment a print message to be sure in `run` method in the `TestCase` class
```python
    try:
        method = getattr(self, self.name)
        method()
    except Exception as e:
        if e.args: print(e)
        result.testFailed()
```
We will have the following printed message

```bash
    name 'BrokenSetUpWasRun' is not defined
    testSetUpError: 		1 run, 1 failed
```

### Step3: Make a change.
Now we can add the `BrokenSetUpWasRun` class. As you can see the setUp log message is different and a Error string was added.
```python
class BrokenSetUpWasRun(WasRun):
    def setUp(self):
        self.log = "Error setUp "
```

### Step4: Run the tests and succeed.
If we run the code we will have the following printed message.
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 0 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
    testSetUpError: 		    1 run, 0 failed
```

### Step5: Refactor to remove duplication.
No needed.

## Solution 2
### Step1: Add a little test.
In this case the test is quite different. We have the same `BrokenSetUpWasRun` but we expect ad failure message (not in the log.)
```python
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        result = test.run()
        assert("1 run, 1 failed" == result.summary())
```
### Step2: Run all tests and fail.
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 0 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
    testSetUpError: 		    1 run, 1 failed
```
### Step3: Make a change
Add raise Exception.

```python
    class BrokenSetUpWasRun(WasRun):
        def setUp(self):
            raise Exception
```

Catch the Exception when setUp is called
**TestCase**
```python
    try:
        self.setUp()
        method = getattr(self, self.name)
        method()
    except Exception as e:
        if e.args: print(e)
        result.testFailed()
```

### Step4: Run the tests and succeed.
In the first run we have the following error `'BrokenSetUpWasRun' object has no attribute 'log'`. We need set up the log in the `BrokenSetUpWasRun` object:
```python
    class BrokenSetUpWasRun(WasRun):
        def setUp(self):
            self.log = "setUp "
            raise Exception
```
Now everything is ok:
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 0 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
    testSetUpError: 		    1 run, 0 failed
```
### Step5: Refactor to remove duplication.
No needed

## Solution 3
In this solution we want to report the setUp error. To achieve this we add the setUp status in the report
### Step1: Add a little test.
```python
    def testSetUpError(self):
        test = BrokenSetUpWasRun("testMethod") 
        result = test.run()
        assert("1 run, 1 failed (setUp: ERROR)" == result.summary())
        return result
```
### Step2: Run all tests and fail.
```bash
    testTemplateMethod: 		1 run, 0 failed
    testResult: 			    1 run, 0 failed
    testFailedResultFormatting: 1 run, 0 failed
    testFailedResult: 		    1 run, 0 failed
    testSetUpError: 		    1 run, 1 failed
```
### Step3: Make a change
We have the same BrokenSetUpWasRun class
```python
class BrokenSetUpWasRun(WasRun):      
    def setUp(self):
        self.log = "setUp "
        raise Exception
```
But in this case it is necessary to make a change to the `TestResult` class adding setUpError attribute, `testHaveSetUpError` method and editing the `summary` method.
**TestResult**
```python
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        self.setUpError = False
        
    def testHaveSetUpError(self):
        self.setUpError = True

    def summary(self):
        setUpStatus = "ERROR" if self.setUpError else "OK"
        return "%d run, %d failed (setUp: %s)" % (self.runCount, self.errorCount, setUpStatus)
```

We need also change the how the error is manage when the `setUp` is called. `testHaveSetUpError()` is called to setup setUpError to True and `testFailed` is called to notify that an error occurs during the test.

```python
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
```
### Step4: Run the tests and succeed.
```bash
    testTemplateMethod: 		1 run, 0 failed (setUp: OK)
    testResult: 			    1 run, 0 failed (setUp: OK)
    testFailedResultFormatting: 1 run, 0 failed (setUp: OK)
    testFailedResult: 		    1 run, 0 failed (setUp: OK)
    testSetUpError: 		    1 run, 0 failed (setUp: OK)
```
### Step5: Refactor to remove duplication.
No needed

## Considerations
I do not know what is the best answer of the exercise (solution 1, solution 2 or solution 3). I think the better is the last one because meet all the requirements: **Catch and report setUp errors**. We catch a possible raise exception from the the setUp method and report carefully in the summary.

Open points:
- if `setUp()` failed does it make sense to call `self.tearDown()`?

