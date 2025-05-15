# Project Setup
This is a very simple project created for educational purposes. To keep things straightforward, we are not using build tools like Maven or Gradle, as they add unnecessary layers of abstraction and complexity for our needs.

This guide will help you set up a minimal, terminal-based environment that allows you to follow along with the exercises in the book and clearly see each step of the process.

## Install JDK
Download [x64 DMG Installer](https://www.oracle.com/java/technologies/downloads/#jdk24-mac), clink install and test it

```
❯ java --version
java 24.0.1 2025-04-15
Java(TM) SE Runtime Environment (build 24.0.1+9-30)
Java HotSpot(TM) 64-Bit Server VM (build 24.0.1+9-30, mixed mode, sharing)
```

```
❯ javac --version
javac 24.0.1
```

## Compile and run HelloWorld.java
```
export COMPILE_DIR="../build-output"
❯ javac HelloWorld.java -d $COMPILE_DIR
❯ java -cp $COMPILE_DIR HelloWorld
Hello World!!
```

## Setup JUnit
### I way
- Install '**Test Runner for Java**' VSCode extension
- Setup Testing>Enable Java Tests>JUnit
- A lib directory popped up, rename do libs

### II way
- Use libs file from this repository
  
### Test JUnit
Compile
```
❯ export COMPILE_DIR="../build-output"
❯ export JUNIT_LIB_PATH="../libs/junit-4.13.2.jar"
❯ export CORE_LIB_PATH="../libs/hamcrest-core-1.3.jar"
❯ javac -cp $JUNIT_LIB_PATH:$CORE_LIB_PATH:. JUnitTest.java -d $COMPILE_DIR
```

Execute
```
❯ export COMPILE_DIR="../build-output"
❯ export JUNIT_LIB_PATH="../libs/junit-4.13.2.jar"
❯ export CORE_LIB_PATH="../libs/hamcrest-core-1.3.jar"
❯ java -cp $JUNIT_LIB_PATH:$CORE_LIB_PATH:$COMPILE_DIR. org.junit.runner.JUnitCore JUnitTest
```

