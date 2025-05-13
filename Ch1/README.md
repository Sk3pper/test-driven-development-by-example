# Test JUnit
Compile&Executes
```
❯ export COMPILE_DIR="../build-output"
❯ export JUNIT_LIB_PATH="../libs/junit-4.13.2.jar"
❯ export CORE_LIB_PATH="../libs/hamcrest-core-1.3.jar"

❯ javac -cp $JUNIT_LIB_PATH:$CORE_LIB_PATH:. TestDollar.java -d $COMPILE_DIR
❯ java -cp $JUNIT_LIB_PATH:$CORE_LIB_PATH:$COMPILE_DIR. org.junit.runner.JUnitCore TestDollar
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [x] ~~$5 + $5 = $10~~
- [ ] Make "amount" private
- [ ] Dollar side-effects?
- [ ] Money rounding?