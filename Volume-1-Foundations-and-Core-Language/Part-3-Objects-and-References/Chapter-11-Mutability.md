# Chapter 11 — Mutability

# Learning Objectives

By the end of this chapter, the reader should be able to explain:

* What mutability means.
* Why some objects can change in place and others cannot.
* How aliasing makes mutation visible through multiple names.

---

# Concept Overview

This chapter builds on names and references. Mutability only becomes clear once the reader understands that names point to objects.

---

# Mental Model

```text
name_a ─┐
        ├──▶ mutable object
name_b ─┘
```

---

# Why It Exists

Mutable objects allow efficient in-place updates. Immutable objects provide stability, hashability, and safer reasoning.

---

# Internal Mechanics

Cover:

* Mutable objects
* Immutable objects
* In-place change
* Rebinding versus mutation
* Aliasing effects

---

# Examples

Use lists and integers first, then strings and dictionaries.

---

# Common Mistakes

Address the misconception that `x = x + ...` always mutates the original object.

---

# Real-world Usage

Explain how mutability affects function arguments, default values, caches, dictionaries, and shared state.

---

# Concept Connections

Connect this chapter back to:

* Chapter 09: object identity and value
* Chapter 10: names and aliases

---

# Active Recall

## Easy Recall Questions

1. What is a mutable object?
2. What is an immutable object?

## Deep Understanding Questions

1. Why does aliasing make mutation more important to understand?

## Explain In Your Own Words

1. Explain rebinding versus mutation.

## Predict-the-Output Questions

Add list and integer examples when drafting the full chapter.

## Mental Model Questions

1. Draw what happens when two names refer to the same list and one name mutates it.

---

# Practical Exercises

1. Compare mutation of a list with rebinding of an integer.
2. Draw before-and-after diagrams for each example.

---

# Summary

This chapter explains why some Python values can change in place and why that matters when names share references.

---

# Preview of Chapter 12

Next we study identity, equality, and memory diagrams as a complete object-reference reasoning toolkit.
