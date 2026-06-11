# Chapter 09 — Everything Is an Object

# Learning Objectives

By the end of this chapter, the reader should be able to explain:

* What an object is in Python.
* Why Python models values as objects.
* How type, value, and identity begin the object mental model.

---

# Concept Overview

This chapter starts Phase 2: Objects and References. It introduces Python's object model before names, assignment, mutability, and memory diagrams.

---

# Mental Model

```text
object
├── type
├── value
└── identity
```

---

# Why It Exists

Python uses objects to give every value consistent behavior, metadata, and operations.

---

# Internal Mechanics

Cover:

* Object identity
* Object type
* Object value
* Attributes and behavior at a high level
* Why even integers and strings are objects

---

# Examples

Use `type()`, `id()`, and simple literals to show that visible values have object structure.

---

# Common Mistakes

Address the misconception that only class instances are objects.

---

# Real-world Usage

Explain how the object model affects debugging, APIs, equality, mutation, and data structures.

---

# Concept Connections

Connect this chapter back to:

* Chapter 02: memory and addresses
* Chapter 07: runtime execution
* Chapter 08: bytecode creating and using runtime values

---

# Active Recall

## Easy Recall Questions

1. What does it mean to say everything is an object?
2. Name three properties every Python object has.

## Deep Understanding Questions

1. Why does Python use one object model for many kinds of values?

## Explain In Your Own Words

1. Explain type, value, and identity without using code first.

## Predict-the-Output Questions

Add examples using `type()` and `id()` when drafting the full chapter.

## Mental Model Questions

1. Draw an object with type, value, and identity.

---

# Practical Exercises

1. Inspect several values with `type()` and describe what each result means.
2. Compare two values and identify what is value-level behavior and what is identity-level behavior.

---

# Summary

This chapter establishes the object model required for names, references, assignment, mutability, and equality.

---

# Preview of Chapter 10

Next we study names and references: what Python variables really are.
