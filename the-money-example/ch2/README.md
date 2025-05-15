# Run JUnit tests
Compile&Executes
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch2
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [ ] ~~$5 + $5 = $10~~
- [ ] Make "amount" private
- [x] **~~Dollar side-effects?~~**
- [ ] Money rounding?

# Lessons learned
- TDD's goal: Write clean code that works
- Divide and conquer the problem
  1. First, solve the "that works" part
  2. Second, solve the "clean code" part
- TDD cycle
  1. Write a test. Invent the interface you wish you had.
  2. Make it run. Getting the bar green in seconds (*).
  3. Make it right. Remove the duplication that you have introduced, and get to green quickly.


(*) Three strategies to quickly getting it to run
1. **Fake it** - Return a constant and gradually replace constants with variables until you have the real code.
2. **Use Obvious Implementation** - Type in the real implementation.
3. **Triangulation**  (see ch3)