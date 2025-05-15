# Run JUnit tests
Compile&Execute
```
❯ ./compile_and_run_tests.sh TestDollar.java the-money-example/ch12
```

# To-do list
- [ ] $5 + 10 CHF = $10 if rate is 2:1
- [x] **$5 + $5 = $10**

** New item

# Lessons learned
- We would like a solution that lets us conveniently represent multiple exchange rates, and still allows most arithmetic-like expressions to look like, well, arithmetic. 
- **Objects to the rescue**. When the object we have doesn't behave the way we want it to, we make another object with the same external protocol (an imposter) but a different implementation. This probably sounds a bit like magic. How do we know to think of creating an imposter here? I won't kid you there is no formula for flashes of design insight. Ward Cunningham came up with the "trick" a decade ago, and I haven't seen it independently duplicated yet, so it must be a pretty tricky trick. TDD can't guarantee that we will have flashes of insight at the right moment. However, confidence-giving tests and carefully factored code give us preparation for insight, and preparation for applying that insight when it comes. The solution is to create an object that acts like a Money but represents the sum of two Moneys.
- *metaphor*: Treat the sum like a wallet: you can have several different notes of different denominations and currencies in the same wallet.
- *metaphor*: Another metaphor is expression, as in "(2+3)* 5", or in our case "($2 + 3 CHF) 5". A Money is the atomic form of an expression. Operations result in Expressions, one of which will be a Sum. Once the operation (such as adding up the value of a portfolio) is complete, the resulting Expression can be reduced back to a single currency given a set of exchange rates.
