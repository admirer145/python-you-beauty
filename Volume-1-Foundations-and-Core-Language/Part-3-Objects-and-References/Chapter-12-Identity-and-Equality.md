# Chapter 12 — Identity, Equality, and Memory Diagrams

# Learning Objectives

By the end of this chapter, the reader should be able to explain:

* The difference between identity and equality.
* How `is` differs from `==`.
* How to draw memory diagrams for objects, names, aliases, and mutation.

---

# Concept Overview

This chapter completes the initial object-reference mental model by combining identity, equality, and memory diagrams.

---

# Mental Model

```text
name ─────▶ object
             ├── identity
             ├── type
             └── value
```

---

# Why It Exists

Identity and equality answer different questions. Memory diagrams make those differences visible.

---

# Internal Mechanics

Cover:

* `id()`
* `is`
* `==`
* Equality methods at a high level
* Memory diagrams for immutable and mutable objects
* Object relationships

---

# Examples

Use small examples that compare identity, equality, aliasing, and mutation.

---

# Common Mistakes

Address the misconception that `is` and `==` are interchangeable.

---

# Real-world Usage

Explain how identity and equality affect debugging, sentinel values, containers, APIs, and object comparisons.

---

# Concept Connections

Connect this chapter back to:

* Chapter 09: object identity, type, and value
* Chapter 10: names and references
* Chapter 11: mutability and aliasing

---

# Active Recall

## Easy Recall Questions

1. What question does `is` answer?
2. What question does `==` answer?

## Deep Understanding Questions

1. Why can two different objects be equal?
2. Why can one object be visible through multiple names?

## Explain In Your Own Words

1. Explain identity versus equality using a memory diagram.

## Predict-the-Output Questions

Add `is`, `==`, and mutation examples when drafting the full chapter.

## Mental Model Questions

1. Draw two equal objects with different identities.
2. Draw two names pointing to the same object.

---

# Practical Exercises

1. Write examples where `==` is true but `is` is false.
2. Draw memory diagrams for list aliasing and integer rebinding.

---

# Summary

This chapter gives the reader the core diagrams and vocabulary needed to reason correctly about Python objects.

---

# Preview of Volume II

Next the curriculum moves into basic language constructs: numbers, strings, booleans, operators, and expressions.
