# Run JUnit tests
Compile&Execute
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch13
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [x] **$5 + $5 = $10**
- [ ] Return Money from $5 + $5
- [ ] ~~Bank.reduce(Money)~~
- [ ] Reduce Money with conversion
- [ ] Reduce(Bank, String)

** New item

# Lessons learned
- Any time we are checking classes explicitly, we should be using polymorphism instead.