# Run
```
❯ python run_6.py 
```

# To-do list
- [ ] ~~Invoke test method~~
- [x] **~~Invoke setUp first~~**
- [ ] Invoke tearDown afterward
- [ ] Invoke tearDown even if the test method fails
- [ ] Run multiple tests
- [ ] Report collected results

# Lessons learned
### # 1
Writing tests common pattern (from Bill Wake):
1. Arrange: Create some objects
2. Act: Stimulate them
3. Assert: Check the results

The first step is often the same from test to test. The second and third steps are unique.
Example
1. Arrange: Take two numbers 7 and 9
2. Act: Add, subtract and multiply them.
3. Assert: We have different results 16, -2 and 63.

The stimulate and expected results are unique but the picked numbers no.

### #2
How often we want to create new objects to test? Two constraints come into conflict:
- *Performance*: If we use similar objects in several tests, we would like to create them for all tests.
- *Isolation*: If tests share objects and one test changes the objects, following tests are likely to change their results.

In this case we choose to relax the *Performance* constraint and we focus to *Isolation*.