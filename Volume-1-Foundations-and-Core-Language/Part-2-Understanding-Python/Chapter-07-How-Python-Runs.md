# Chapter 07 — How Python Runs

# Learning Objectives

By the end of this chapter, the reader should be able to explain:

* What happens when a Python file is executed.
* How source code moves through tokenizing, parsing, AST generation, and compilation.
* Why bytecode exists before runtime execution.
* How this flow prepares the reader for the Python Virtual Machine.

---

# Concept Overview

This chapter traces the journey from a `.py` file to compiled bytecode. It should stop before deeply explaining bytecode execution; that belongs to Chapter 08.

---

# Mental Model

```text
source.py
     ↓
Tokenizer
     ↓
Parser
     ↓
AST
     ↓
Compiler
     ↓
Bytecode
```

---

# Why It Exists

Python source code is written for humans. CPython must transform that text into a structured form it can analyze, compile, and later execute.

---

# Internal Mechanics

Cover:

* Source text
* Tokens
* Parser
* Abstract Syntax Tree
* Compilation
* Code objects

---

# Examples

Use small source snippets to show how readable Python becomes structured execution input.

---

# Common Mistakes

Address the misconception that CPython reads and directly executes each source-code line as plain text.

---

# Real-world Usage

Explain how this model helps with syntax errors, tracebacks, import behavior, and tooling.

---

# Concept Connections

Connect this chapter back to:

* Chapter 01: source code and programs
* Chapter 02: instructions and execution
* Chapter 06: CPython as the reference implementation

---

# Active Recall

## Easy Recall Questions

1. What is the first input CPython receives when running a `.py` file?
2. What is an AST?

## Deep Understanding Questions

1. Why does CPython need parsing before execution?
2. Why is bytecode a useful intermediate form?

## Explain In Your Own Words

1. Explain the path from source text to bytecode.

## Predict-the-Output Questions

Add examples after the full chapter draft is written.

## Mental Model Questions

1. Draw the source-to-bytecode pipeline.

---

# Practical Exercises

1. Run a small Python file and identify which part is source text, which part is syntax, and which part becomes runtime behavior.
2. Use `ast.parse()` on a small expression and inspect the result.

---

# Summary

This chapter explains how CPython turns human-readable Python into bytecode-ready program structure.

---

# Preview of Chapter 08

Next we study what bytecode is and how the Python Virtual Machine executes it.
