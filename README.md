# 🧪 Test-Driven Development by Example
Welcome to the repository for the book Test-Driven Development by Example by Kent Beck.
This repo contains a step-by-step walkthrough of the concepts, exercises, and code examples presented in the book.

# 🔄 Process to keep in mind
The TDD cycle is as follows:
1. Add a little test.
2. Run all tests and fail.
3. Make a change.
4. Run the tests and succeed.
5. Refactor to remove duplication.

<img src="https://sk3pper.github.io//posts/software-development/test-driven-development/images/tdd-icon-hero.png" width="300">

# What You'll Find Here

## 🔧 setup-environment/
A minimal, terminal-based setup guide to help you follow along with the book.
This guide walks you through creating a clean and distraction-free development environment to fully focus on TDD fundamentals.

## 👨‍💻 in-the-money-example/ and xUnit/
These directories contain step-by-step coding examples inspired by the book’s exercises, organized chapter by chapter. Each folder includes:

- ✅ The final version of the code for that chapter
- 🧪 Tests you can run yourself
- 🔍 A clear progression between chapters to observe what changed and why

This structure helps you compare versions and understand the evolution of the code, providing insight into the TDD thought process.

*Note*: The xUnit/ directory additionally contains an example solution for the **“Catch and report setUp errors”** task, showing how to properly handle exceptions raised during the setUp phase of testing.