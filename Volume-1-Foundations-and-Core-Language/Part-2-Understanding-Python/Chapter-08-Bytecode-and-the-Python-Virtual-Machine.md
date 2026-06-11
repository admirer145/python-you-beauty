# Chapter 08 — Bytecode and the Python Virtual Machine

# Learning Objectives

By the end of this chapter, the reader should be able to explain:

* What Python bytecode represents.
* Why CPython uses bytecode.
* What the Python Virtual Machine does.
* How bytecode execution connects source code to runtime behavior.

---

# Concept Overview

This chapter continues from Chapter 07. Chapter 07 traces how source code becomes bytecode. This chapter explains how CPython executes that bytecode.

---

# Mental Model

```text
source.py
     ↓
Compiler
     ↓
Bytecode
     ↓
Python Virtual Machine
     ↓
Runtime behavior
```

---

# Why It Exists

Bytecode gives CPython an intermediate representation that is easier for the interpreter to execute than raw source code.

---

# Internal Mechanics

Cover:

* Code objects
* Bytecode instructions
* Stack-based execution
* Frame objects
* The evaluation loop

---

# Examples

Use small Python snippets and `dis` output to connect source code to bytecode instructions.

---

# Common Mistakes

Address the misconception that bytecode is native machine code or that the CPU executes Python bytecode directly.

---

# Real-world Usage

Explain why bytecode matters for debugging, performance intuition, tooling, and CPython internals.

---

# Concept Connections

Connect this chapter back to:

* Chapter 02: CPU instructions and memory
* Chapter 03: execution and stack frames
* Chapter 06: CPython as an implementation
* Chapter 07: compilation from source code

---

# Active Recall

## Easy Recall Questions

1. What is Python bytecode?
2. What executes Python bytecode in CPython?

## Deep Understanding Questions

1. Why does CPython compile source code before executing it?
2. Why is Python bytecode not the same thing as machine code?

## Explain In Your Own Words

1. Explain the role of the Python Virtual Machine.

## Predict-the-Output Questions

Add bytecode-backed examples after Chapter 07 is fully drafted.

## Mental Model Questions

1. Draw the path from source code to runtime behavior.

---

# Practical Exercises

1. Use `dis.dis()` on a simple function and identify at least three instructions.
2. Explain how one bytecode instruction relates to a visible Python behavior.

---

# Summary

This chapter should remove the remaining magic between compiled Python bytecode and actual program execution.

---

# Preview of Chapter 09

Next we begin Python's object model: everything in Python is an object.
