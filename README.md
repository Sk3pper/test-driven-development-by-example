# 🧪 Test-Driven Development by Example
Welcome to the repository for the book Test-Driven Development by Example by Kent Beck.
This repo contains a step-by-step walkthrough of the concepts, exercises, and code examples presented in the book.

# 📝 Related Article
Read article for further details [here](https://sk3pper.github.io/posts/software-development/test-driven-development/test-driven-development-by-example-init/).

# 🔄 Process to keep in mind
The TDD cycle is

<table>
    <tr>
        <td>
            <table>
                <tr><td> 1. Add a little test.             </td> </tr>
                <tr><td> 2. Run all tests and fail.        </td></tr>
                <tr><td> 3. Make a change.                 </td></tr>
                <tr><td> 4. Run the tests and succeed.     </td></tr>
                <tr><td> 5. Refactor to remove duplication.</td></tr>
            </table>
        </td>
        <td>
            <img src="https://sk3pper.github.io/posts/software-development/test-driven-development/test-driven-development-by-example-init/images/tdd-icon.png" width="300">
        </td>
    </tr>
</table>

# What You'll Find Here

## 🔧 setup-environment/
A minimal, terminal-based setup guide to help you follow along with the book.
This guide walks you through creating a clean development environment to fully focus on TDD fundamentals.

## 👨‍💻 in-the-money-example/ and xUnit/
These directories contain step-by-step coding examples inspired by the book’s exercises, organized chapter by chapter. Each folder includes:

- ✅ The final version of the code for that chapter
- 🧪 Tests you can run yourself
- 🔍 A clear progression between chapters to observe what changed and why

This structure helps you compare versions and understand the evolution of the code, providing insight into the TDD thought process.

*Note*: The `xUnit/` directory also includes solutions for the following tasks:

- **Catch and report setUp errors** [[source code]](https://github.com/Sk3pper/test-driven-development-by-example/tree/main/xUnit/ch22_exercise) [[article]](https://sk3pper.github.io/posts/software-development/test-driven-development/exercise-1/)
- **Invoke tearDown even if the test method fails** [[source code]](https://github.com/Sk3pper/test-driven-development-by-example/tree/main/xUnit/ch23_exerciseA) [[article]](https://sk3pper.github.io/posts/software-development/test-driven-development/exercise-2/)
- **Create TestSuite from a TestCase class** [[source code]](https://github.com/Sk3pper/test-driven-development-by-example/tree/main/xUnit/ch23_exerciseB) [[article]](https://sk3pper.github.io/posts/software-development/test-driven-development/exercise-3/)

 
These examples demonstrate how to apply *Test-Driven Development (TDD) principles* in practice—step by step. They also served as a way for me to better understand the entire process and train myself through hands-on exercises.