# Run
```
❯ python exercise_23A.py
```

# To-do list
- [ ] ~~Invoke test method~~
- [ ] ~~Invoke setUp first~~**
- [ ] ~~Invoke tearDown afterward~~
- [x] **~~Invoke tearDown even if the test method fails~~**
- [ ] ~~Run multiple tests~~
- [ ] ~~Report collected results~~
- [ ] ~~Log string in WasRun~~
- [ ] ~~Report failed tests~~
- [ ] ~~Catch and report setUp errors~~
- [ ] Create TestSuite from a TestCase class **

** New item

# Exercise: 
Implement the last two items
1. [ ] Create TestSuite from a TestCase class 
2. [x] **~~Invoke tearDown even if the test method fails~~**

### Step 0: Remove setUp OK prints
After some usage I convinced myself that the `(setUp: OK)` is not necessary. So i remove it leaving only the exception handler in the `TestCase` class during the `self.setUp()` call.

### Step1: Add a little test.
We start from the last one: **Invoke tearDown even if the test method fails**. From what I see in the code:
```python
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
```

When the test method fails the `tearDown()` method is called in any case. Create a test to check it.

```python
def testTearDownWithTestMethodError(self):
    test = WasRun("testBrokenMethod") 
    test.run(self.result)
    assert("setUp tearDown " == test.log)
```

The test checks what happens when `testBrokenMethod` is called. If we see the string `"setUp tearDown "` in the log, it means that both the `setUp` and `tearDown` methods were called correctly.

### Step2: Run all tests and fail + Step3: Make a change + Step4: Run the tests and succeed
In this case the tests do not fail because the current item is already implemented.

```bash
testTemplateMethod: 		        1 run, 0 failed
testResult: 			            1 run, 0 failed
testFailedResultFormatting: 	    1 run, 0 failed
testFailedResult: 		            1 run, 0 failed
testSetUpError: 		            1 run, 0 failed
testTearDownWithTestMethodError: 	1 run, 0 failed
```