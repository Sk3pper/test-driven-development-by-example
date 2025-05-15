# Run JUnit tests
Compile&Execute
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch5
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [ ] ~~$5 + $5 = $10~~
- [ ] ~~Make "amount" private~~
- [ ] ~~Dollar side-effects?~~
- [ ] Money rounding?
- [ ] ~~equals()~~ 
- [ ] hasCode() 
- [ ] Equal null
- [ ] Equal object
- [x] **~~5 CHF * 2 = 10 CHF~~** **
- [ ] Dollar/Franc duplication **
- [ ] Common equals **
- [ ] Commont times **

** New items

# Lessons learned
*Strategy adopted*: Got a new test case working in the direction of the final test to implement.

The "**$5 + 10 CHF = $10 if rate is 2:1**" test it still seems to be a big leap. A prerequisite seems to be having an object like *Dollar*, but to represent *franc*. If we can get the object Franc to work the way that the object Dollar works now (**5 CHF * 2 = 10 CHF**) , we'll be closer to being able to write and run the mixed addition test.


