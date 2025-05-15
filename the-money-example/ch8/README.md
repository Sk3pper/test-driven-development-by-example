# Run JUnit tests
Compile&Execute
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch8
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
- [ ] ~~5 CHF * 2 = 10 CHF~~
- [x] **Dollar/Franc duplication**
- [ ] ~~Common equals~~
- [ ] Common times
- [ ] ~~Compare Francs and Dollars~~
- [ ] Currency? 
- [ ] Delete testFrancMultiplication? **

** New item

# Lessons learned
- The two subclasses of Money (Dollar and Francs) are not doing enough work to justify their existence.
- Use factory methods in Money that returns a Dollar and another that returns a Franc

