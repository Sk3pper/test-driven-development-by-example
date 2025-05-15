# Run JUnit tests
Compile&Execute
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch4
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [ ] ~~$5 + $5 = $10~~
- [x] **~~Make "amount" private~~**
- [ ] ~~Dollar side-effects?~~
- [ ] Money rounding?
- [ ] ~~equals()~~ 
- [ ] hasCode() 
- [ ] Equal null
- [ ] Equal object

# Lessons learned
Be aware that we've introduced a potential risk. If our equality test isn't reliable - if it doesn't truly verify that equality behaves correctly - then our multiplication test might also be flawed, since it depends on equality working properly. This is a known trade-off in Test-Driven Development (TDD), and we manage it intentionally. Our goal isn't to achieve perfection, but to make steady progress with confidence. By expressing our understanding twice - once in the code itself, and once in the tests - we aim to catch enough issues to move forward effectively. Still, there will be times when our reasoning fails and a bug makes it through. When that happens, we learn from it, recognize the test we should have written, and keep improving.