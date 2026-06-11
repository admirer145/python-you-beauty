# Chapter 10 — Names and References

# Learning Objectives

By the end of this chapter, the reader should be able to explain:

* Why Python variables are names, not boxes.
* How assignment binds names to objects.
* How references connect code to objects in memory.

---

# Concept Overview

This chapter builds directly on Chapter 09. Once values are understood as objects, variables can be explained as names that refer to those objects.

---

# Mental Model

```text
name ─────▶ object
```

---

# Why It Exists

Names let Python programs refer to objects and reuse them without manually managing memory addresses.

---

# Internal Mechanics

Cover:

* Name binding
* Assignment
* Rebinding
* Multiple names referencing the same object
* Local and global namespaces at a high level

---

# Examples

Use assignment and rebinding examples before introducing mutation.

---

# Common Mistakes

Address the misconception that assignment copies objects by default.

---

# Real-world Usage

Explain how references affect function arguments, aliases, debugging, and object lifetime.

---

# Concept Connections

Connect this chapter back to:

* Chapter 02: memory addresses
* Chapter 09: objects, type, value, and identity

---

# Active Recall

## Easy Recall Questions

1. What does assignment do in Python?
2. Can two names refer to the same object?

## Deep Understanding Questions

1. Why is the "variable as box" model misleading in Python?

## Explain In Your Own Words

1. Explain name binding using a diagram.

## Predict-the-Output Questions

Add assignment and aliasing examples when drafting the full chapter.

## Mental Model Questions

1. Draw two names pointing to one object.

---

# Practical Exercises

1. Create two names that refer to the same object and explain the relationship.
2. Rebind one name and draw what changed.

---

# Summary

This chapter replaces the variable-as-box model with Python's name-and-reference model.

---

# Preview of Chapter 11

Next we study mutability: what can change, what cannot, and why aliases matter.
