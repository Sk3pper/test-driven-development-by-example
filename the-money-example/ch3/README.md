# Run JUnit tests
Compile&Execute
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch3
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [ ] ~~$5 + $5 = $10~~
- [ ] Make "amount" private
- [ ] ~~Dollar side-effects?~~
- [ ] Money rounding?
- [x] **~~equals()~~** **
- [ ] hasCode() **
- [ ] Equal null
- [ ] Equal object

** New items

# Lessons learned
- Use Value Object pattern (use objects as values): One of the constraints on Value Objects is that the values of instance variables of the object never change once they have been set in the construct. 
- Value Object should implement *equals()*
- If we use Dollar as the key to a hash table then we need to implement also *hasCode()*


(*) Three strategies to quickly getting it to run
1. **Fake it** - Return a constant and gradually replace constants with variables until you have the real code.
2. **Use Obvious Implementation** - Type in the real implementation.
3. **Triangulation** - When we triangulate, we only generalize code when we have two examples or more. We briefly ignore the duplication between test and model code. When the second example demands a more general solution, **then and only then** do we generalize.
