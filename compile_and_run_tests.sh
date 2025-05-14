#!/bin/bash

if [ $# -lt 1 ]; then
  echo "Usage: $0 <test_file_path> [source_code_dir]"
  echo "Example: $0 TestDollar.java"
  echo "         $0 TestDollar.java /path/to/source/code"
  exit 1
fi

TEST_FILE=$1
CLASS_NAME=$(basename "$TEST_FILE" .java)

if [ $# -ge 2 ]; then
  SRC_DIR=$2
  if [ ! -d "$SRC_DIR" ]; then
    echo "Error: Source directory '$SRC_DIR' does not exist."
    exit 1
  fi
else
  SRC_DIR="."
fi

# Directory paths
COMPILE_DIR="build-output"
JUNIT_LIB_PATH="libs/junit-4.13.2.jar"
CORE_LIB_PATH="libs/hamcrest-core-1.3.jar"

mkdir -p $COMPILE_DIR
FULL_TEST_PATH="$SRC_DIR/$TEST_FILE"

if [ ! -f "$FULL_TEST_PATH" ]; then
  echo "Error: Test file '$FULL_TEST_PATH' does not exist."
  exit 1
fi

# Compile the test class
echo "Compiling $FULL_TEST_PATH..."
javac -cp $JUNIT_LIB_PATH:$CORE_LIB_PATH:$SRC_DIR:. "$FULL_TEST_PATH" -d $COMPILE_DIR

if [ $? -eq 0 ]; then
  echo "Compilation successful."
  
  # Run the tests
  echo "Running JUnit tests for $CLASS_NAME..."
  java -cp $JUNIT_LIB_PATH:$CORE_LIB_PATH:$COMPILE_DIR:$SRC_DIR:. org.junit.runner.JUnitCore "$CLASS_NAME"
else
  echo "Compilation failed."
  exit 1
fi