# Chapter 18 — Control Flow

---

# Learning Objectives

By the end of this chapter, you should understand:

* What control flow means.
* Why programs need branching and repetition.
* How `if`, `elif`, and `else` work.
* How condition expressions use truthiness.
* How indentation defines blocks.
* How nested branches work.
* How `while` loops work.
* How `for` loops work.
* How `range()` works in loops.
* How `break` exits a loop.
* How `continue` skips to the next iteration.
* How loop `else` works.
* How to avoid infinite loops.
* How to reason about execution paths.
* Common mistakes with conditions, indentation, mutation during loops, and loop control.

Control flow is how a program stops being a straight list of instructions and starts making decisions.

---

# Concept Overview

By default, Python executes statements from top to bottom.

Example:

```python
print("first")
print("second")
print("third")
```

Output:

```text
first
second
third
```

Control flow changes this.

It lets Python:

* Choose between branches.
* Repeat work.
* Stop loops early.
* Skip an iteration.
* Execute code only when conditions are satisfied.

Examples:

```python
if age >= 18:
    print("adult")
else:
    print("minor")
```

```python
while count < 3:
    print(count)
    count += 1
```

```python
for item in items:
    print(item)
```

Control flow uses expressions to decide execution.

Core model:

```text
condition expression
    |
    v
truthiness
    |
    v
which block runs?
```

---

# Why Control Flow Exists

Programs need to respond to different situations.

Examples:

```text
If password is correct, allow login.
If file exists, read it.
If user is admin, show admin tools.
While there are tasks, process them.
For each record, validate it.
Stop when the target is found.
Skip invalid entries.
```

Without control flow, every program would execute the same instructions in the same order every time.

Control flow gives programs:

* Decisions
* Repetition
* Searching
* Filtering
* Validation
* Error handling paths
* Workflow logic

---

# Blocks and Indentation

Python uses indentation to define blocks.

Example:

```python
if True:
    print("inside")
    print("also inside")

print("outside")
```

Output:

```text
inside
also inside
outside
```

The indented lines belong to the `if` block.

The unindented line is outside the block.

Indentation is syntax, not decoration.

Incorrect indentation changes meaning or raises an error.

---

# The if Statement

The `if` statement runs a block only if a condition is truthy.

Syntax:

```python
if condition:
    block
```

Example:

```python
age = 20

if age >= 18:
    print("adult")
```

Output:

```text
adult
```

The condition:

```python
age >= 18
```

is an expression.

It evaluates to a boolean object.

Python checks its truthiness.

If truthy, the block runs.

---

# if With Falsy Values

Conditions do not have to be exactly `True` or `False`.

Example:

```python
name = "Ada"

if name:
    print("name provided")
```

Output:

```text
name provided
```

Non-empty strings are truthy.

Example:

```python
items = []

if items:
    print("items exist")
```

The block does not run.

Empty lists are falsy.

This uses truthiness from Chapter 15.

---

# else

`else` runs when the `if` condition is falsy.

Example:

```python
age = 16

if age >= 18:
    print("adult")
else:
    print("minor")
```

Output:

```text
minor
```

Exactly one of these blocks runs:

```text
if block
else block
```

The `else` block has no condition.

It means:

```text
otherwise
```

---

# elif

`elif` means "else if".

It checks another condition only if previous conditions were falsy.

Example:

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(grade)
```

Output:

```text
B
```

Python checks conditions from top to bottom.

The first truthy branch runs.

The rest are skipped.

---

# Branch Order Matters

Order matters in `if`/`elif` chains.

Problem:

```python
score = 95

if score >= 70:
    grade = "C or better"
elif score >= 90:
    grade = "A"
```

The `score >= 70` condition is true for `95`, so the first branch runs.

The `score >= 90` branch is never reached.

Better:

```python
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "C or better"
```

Put more specific or stricter conditions before broader ones.

---

# Nested if Statements

Branches can contain branches.

Example:

```python
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("admin dashboard")
    else:
        print("user dashboard")
else:
    print("login required")
```

Output:

```text
user dashboard
```

Nested branches are sometimes necessary.

But deeply nested code becomes hard to read.

When nesting grows, consider:

* Combining conditions.
* Returning early from functions.
* Extracting helper functions.
* Simplifying the decision model.

---

# Combining Conditions

Use boolean operators to combine conditions.

Example:

```python
if is_logged_in and is_admin:
    print("admin dashboard")
```

Use `or`:

```python
if is_owner or is_admin:
    print("can edit")
```

Use `not`:

```python
if not is_active:
    print("inactive")
```

Keep conditions readable.

If a condition becomes complex, name it:

```python
can_edit = is_owner or is_admin

if can_edit:
    print("can edit")
```

---

# Guard Conditions Preview

Inside functions, guard conditions can reduce nesting.

Example:

```python
def process(user):
    if user is None:
        return

    if not user.is_active:
        return

    send_email(user)
```

This will be more important after we study functions.

For now, recognize the idea:

```text
handle invalid or stopping cases early
then continue with the main path
```

---

# The pass Statement

`pass` does nothing.

It is a placeholder statement.

Example:

```python
if condition:
    pass
```

Why does it exist?

Python requires a block after `if`, `for`, `while`, `def`, and similar statements.

If you have not written the block yet, `pass` keeps the syntax valid.

Example:

```python
def future_feature():
    pass
```

Use `pass` deliberately.

Do not leave placeholder logic in production code without reason.

---

# while Loops

A `while` loop repeats while a condition is truthy.

Syntax:

```python
while condition:
    block
```

Example:

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

Output:

```text
0
1
2
```

Evaluation:

```text
check count < 3
if truthy, run block
check again
repeat until falsy
```

---

# Avoiding Infinite while Loops

A `while` loop must eventually make its condition falsy, unless it is intentionally infinite.

Problem:

```python
count = 0

while count < 3:
    print(count)
```

`count` never changes.

The condition remains true forever.

Correct:

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

When writing `while`, ask:

```text
What changes so this loop can stop?
```

---

# Intentional Infinite Loops

Some loops are intentionally infinite and use `break`.

Example:

```python
while True:
    command = input("> ")

    if command == "quit":
        break

    print("You typed:", command)
```

This loop runs until the user enters `"quit"`.

Use intentional infinite loops only when there is a clear exit condition inside the loop.

---

# for Loops

A `for` loop iterates over an iterable.

Example:

```python
items = ["a", "b", "c"]

for item in items:
    print(item)
```

Output:

```text
a
b
c
```

The loop variable `item` is bound to each object from the iterable, one at a time.

Conceptually:

```text
item -> "a"
run block
item -> "b"
run block
item -> "c"
run block
```

---

# Loop Variables Are Names

The loop variable is a name.

Example:

```python
for item in ["a", "b", "c"]:
    print(item)
```

Each iteration rebinds `item`.

After the loop, `item` still exists in the surrounding scope:

```python
for item in ["a", "b", "c"]:
    pass

print(item)
```

Output:

```text
c
```

This surprises some learners.

Python `for` loops do not create a new block scope.

Function scope will be studied later.

---

# Iterating Over Strings

Strings are iterable.

Example:

```python
for char in "abc":
    print(char)
```

Output:

```text
a
b
c
```

Each `char` is a one-character string.

This connects to Chapter 14.

---

# Iterating Over Dictionaries

Iterating over a dictionary directly gives keys.

Example:

```python
user = {"name": "Ada", "role": "admin"}

for key in user:
    print(key)
```

Output:

```text
name
role
```

To iterate values:

```python
for value in user.values():
    print(value)
```

To iterate key-value pairs:

```python
for key, value in user.items():
    print(key, value)
```

This will be studied deeply in the dictionaries chapter.

---

# range()

`range()` represents a sequence of integers.

Example:

```python
for number in range(3):
    print(number)
```

Output:

```text
0
1
2
```

`range(3)` produces values:

```text
0, 1, 2
```

Stop is excluded.

This matches slicing.

---

# range(start, stop)

Example:

```python
for number in range(2, 5):
    print(number)
```

Output:

```text
2
3
4
```

Meaning:

```text
start at 2
stop before 5
```

Again, the stop value is excluded.

---

# range(start, stop, step)

Example:

```python
for number in range(0, 10, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
```

Negative steps count down:

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

The stop is still excluded.

---

# range Is Not a List

In modern Python, `range()` returns a range object, not a list.

Example:

```python
numbers = range(3)

print(numbers)
print(type(numbers))
```

Output:

```text
range(0, 3)
<class 'range'>
```

If you need a list:

```python
print(list(range(3)))
```

Output:

```text
[0, 1, 2]
```

`range` is memory-efficient because it represents the sequence without storing every integer as a list.

---

# break

`break` exits the nearest enclosing loop immediately.

Example:

```python
for number in range(10):
    if number == 3:
        break
    print(number)
```

Output:

```text
0
1
2
```

When `number == 3`, the loop stops.

The `print(number)` after the `if` does not run for `3`.

Use `break` when the loop's purpose has been completed or continuing is unnecessary.

---

# continue

`continue` skips the rest of the current iteration and moves to the next one.

Example:

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

Output:

```text
0
1
3
4
```

When `number == 2`, Python skips `print(number)` and proceeds to the next iteration.

Use `continue` for skip conditions.

---

# break vs continue

`break` exits the loop.

`continue` exits only the current iteration.

Example:

```python
for number in range(5):
    if number == 2:
        break
    print(number)
```

Output:

```text
0
1
```

Example:

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

Output:

```text
0
1
3
4
```

These are different control-flow operations.

---

# Loop else

Python loops can have an `else` block.

The loop `else` runs if the loop finishes normally without `break`.

Example:

```python
target = 3

for number in [1, 2, 3, 4]:
    if number == target:
        print("found")
        break
else:
    print("not found")
```

Output:

```text
found
```

The `else` block does not run because `break` occurred.

If target is missing:

```python
target = 9

for number in [1, 2, 3, 4]:
    if number == target:
        print("found")
        break
else:
    print("not found")
```

Output:

```text
not found
```

Loop `else` means:

```text
no break occurred
```

---

# Why Loop else Exists

Loop `else` is useful for search patterns.

Without loop `else`:

```python
found = False

for item in items:
    if item == target:
        found = True
        break

if not found:
    print("not found")
```

With loop `else`:

```python
for item in items:
    if item == target:
        break
else:
    print("not found")
```

Some teams avoid loop `else` because it is less familiar.

It is valid Python.

Use it when it improves clarity for readers who understand the idiom.

---

# Nested Loops

Loops can be nested.

Example:

```python
for row in range(2):
    for col in range(3):
        print(row, col)
```

Output:

```text
0 0
0 1
0 2
1 0
1 1
1 2
```

Nested loops are common for grids, tables, matrices, and combinations.

Be careful with complexity.

If one loop runs `n` times and the inner loop runs `m` times, the body runs `n * m` times.

---

# break in Nested Loops

`break` exits only the nearest loop.

Example:

```python
for row in range(3):
    for col in range(3):
        if col == 1:
            break
        print(row, col)
```

Output:

```text
0 0
1 0
2 0
```

The `break` exits the inner loop only.

The outer loop continues.

If you need to exit multiple levels, consider:

* Returning from a function.
* Using a flag.
* Refactoring into a helper function.

---

# Mutating While Iterating

Be careful when mutating a collection while iterating over it.

Problem:

```python
items = [1, 2, 3, 4]

for item in items:
    if item % 2 == 0:
        items.remove(item)

print(items)
```

This can skip elements because the list changes while the loop is using it.

Safer pattern:

```python
items = [1, 2, 3, 4]
filtered = []

for item in items:
    if item % 2 != 0:
        filtered.append(item)

items = filtered
```

Or use a comprehension later:

```python
items = [item for item in items if item % 2 != 0]
```

---

# Enumerating Indexes and Values

Use `enumerate()` when you need both index and value.

Example:

```python
items = ["a", "b", "c"]

for index, item in enumerate(items):
    print(index, item)
```

Output:

```text
0 a
1 b
2 c
```

This is usually better than:

```python
for index in range(len(items)):
    item = items[index]
```

Use direct iteration unless you truly need the index.

---

# Parallel Iteration With zip

Use `zip()` to iterate over multiple iterables together.

Example:

```python
names = ["Ada", "Grace"]
scores = [95, 98]

for name, score in zip(names, scores):
    print(name, score)
```

Output:

```text
Ada 95
Grace 98
```

`zip()` stops when the shortest iterable is exhausted.

This is useful, but if unequal lengths are a bug, validate lengths explicitly.

---

# Control Flow and Readability

Control flow can become hard to read when:

* Conditions are too complex.
* Nesting is too deep.
* Loops do too many things.
* Variables change in too many places.
* `break` and `continue` are scattered.

Improve readability by:

* Naming conditions.
* Extracting functions.
* Reducing nesting.
* Keeping loop bodies focused.
* Handling special cases early.

Control flow should make program paths explicit.

---

# Common Mistakes

## Misconception 1

### Indentation is style only.

In Python, indentation defines blocks.

Changing indentation changes the program.

---

## Misconception 2

### Conditions must be exactly True or False.

Conditions use truthiness.

Objects can be truthy or falsy.

---

## Misconception 3

### elif branches are all checked.

Python stops at the first truthy branch.

Remaining `elif` and `else` blocks are skipped.

---

## Misconception 4

### while loops stop automatically.

A `while` loop stops only when the condition becomes falsy or control exits with `break`, `return`, or an exception.

---

## Misconception 5

### break exits all nested loops.

`break` exits only the nearest enclosing loop.

---

## Misconception 6

### loop else means the loop condition was false initially.

Loop `else` means the loop completed without `break`.

---

## Misconception 7

### range() creates a list.

`range()` creates a range object.

Convert with `list(range(...))` only when a list is needed.

---

# Real-world Usage

## Validation Paths

```python
if not email:
    error = "email required"
elif "@" not in email:
    error = "invalid email"
else:
    error = None
```

Branch order matters.

Check required presence before format details.

---

## Search

```python
for user in users:
    if user.id == target_id:
        found_user = user
        break
else:
    found_user = None
```

This is a search pattern.

No `break` means no matching user was found.

---

## Processing Queues

```python
while queue:
    task = queue.pop(0)
    process(task)
```

The loop continues while the queue is non-empty.

For production queues, specialized data structures are often better than list `pop(0)`.

The control-flow idea remains the same.

---

## Filtering

```python
valid_items = []

for item in items:
    if item.is_valid:
        valid_items.append(item)
```

This builds a new list rather than mutating while iterating.

Comprehensions will later provide a compact form.

---

## Retry Loops

```python
attempt = 0

while attempt < max_attempts:
    attempt += 1

    if try_operation():
        break
else:
    raise RuntimeError("operation failed")
```

The `else` block runs only if all attempts finish without `break`.

---

# Concept Connections

This chapter builds on:

```text
Chapter 15:
Conditions use truthiness.

Chapter 16:
Comparison and boolean operators build conditions.

Chapter 17:
Condition expressions evaluate to objects.
```

It prepares:

```text
Functions:
    control flow inside reusable blocks

Scope:
    names inside functions and loops

Call Stack:
    returning from functions changes control flow

Data Structures:
    loops process lists, dictionaries, sets, and iterables
```

Core model:

```text
statement
    |
    v
condition expression
    |
    v
truthiness
    |
    v
which block executes?
```

---

# Internal Mechanics Summary

Important terms:

| Term | Meaning |
| --- | --- |
| Control flow | Order in which code executes |
| Branch | One possible execution path |
| Block | Group of statements defined by indentation |
| Condition | Expression used to decide control flow |
| `if` | Run block if condition is truthy |
| `elif` | Additional conditional branch |
| `else` | Fallback branch |
| `while` | Repeat while condition is truthy |
| `for` | Iterate over an iterable |
| `range` | Range object representing integer sequence |
| `break` | Exit nearest loop |
| `continue` | Skip rest of current iteration |
| Loop `else` | Run if loop completes without `break` |

Core rules:

```text
Indentation defines blocks.
if chooses branches using truthiness.
elif checks happen top to bottom.
while must have a path to stop.
for loops bind the loop variable each iteration.
break exits the nearest loop.
continue skips to the next iteration.
loop else means no break occurred.
```

---

# Active Recall

## Easy Recall Questions

1. What is control flow?
2. What defines a block in Python?
3. What does `if` do?
4. What does `elif` mean?
5. When does `else` run in an `if` statement?
6. What does a `while` loop do?
7. What does a `for` loop do?
8. What does `break` do?
9. What does `continue` do?
10. What does loop `else` mean?

---

## Deep Understanding Questions

1. Why does branch order matter in an `if`/`elif` chain?
2. Why can deeply nested conditionals become hard to maintain?
3. Why must a `while` loop change something related to its condition?
4. Why does `break` only exit the nearest loop?
5. Why is mutating a list while iterating over it risky?
6. Why is direct iteration usually better than `range(len(items))`?
7. Why is `enumerate()` useful?
8. Why does `range()` exclude the stop value?
9. Why can loop `else` be useful for search?
10. Why does control flow depend on expression evaluation?

---

## Explain In Your Own Words

1. Explain how an `if` statement decides whether to run.
2. Explain the difference between `elif` and multiple separate `if` statements.
3. Explain `while` loop execution.
4. Explain `for item in items`.
5. Explain `break` versus `continue`.
6. Explain loop `else`.
7. Explain why indentation is syntax.

---

## Predict-the-Output Questions

### Question 1

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

Answer:

```text
B
```

Reason:

The first condition is false. The second is true, so that branch runs.

---

### Question 2

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

Answer:

```text
0
1
2
```

Reason:

The loop stops when `count` becomes `3`.

---

### Question 3

```python
for number in range(3):
    print(number)
```

Answer:

```text
0
1
2
```

Reason:

`range(3)` produces `0`, `1`, and `2`.

---

### Question 4

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

Answer:

```text
0
1
3
4
```

Reason:

`continue` skips the print for `2`.

---

### Question 5

```python
for number in range(5):
    if number == 2:
        break
    print(number)
```

Answer:

```text
0
1
```

Reason:

`break` exits the loop when `number` is `2`.

---

### Question 6

```python
for item in [1, 2, 3]:
    if item == 4:
        break
else:
    print("not found")
```

Answer:

```text
not found
```

Reason:

The loop completed without `break`, so the loop `else` ran.

---

# Mental Model Questions

1. Draw the execution path of an `if`/`else`.
2. Draw an `if`/`elif`/`else` chain checking conditions top to bottom.
3. Draw a `while` loop condition being checked repeatedly.
4. Draw a `for` loop rebinding its loop variable each iteration.
5. Draw how `break` exits a loop.
6. Draw how `continue` skips to the next iteration.
7. Draw when loop `else` runs.

---

# Practical Exercises

## Exercise 1

Write an `if`/`elif`/`else` grade classifier:

```text
90 and above -> A
80-89 -> B
70-79 -> C
below 70 -> D
```

Test boundary values such as `90`, `89`, `80`, `79`, and `70`.

---

## Exercise 2

Write a `while` loop that counts down from `5` to `1`.

Then explain what changes each iteration to make the loop stop.

---

## Exercise 3

Use a `for` loop and `range()` to print even numbers from `0` to `10`, excluding `10`.

Explain the `start`, `stop`, and `step`.

---

## Exercise 4

Given:

```python
items = ["a", "", "b", "", "c"]
```

Print only non-empty strings using `continue`.

---

## Exercise 5

Search for a target:

```python
numbers = [4, 8, 15, 16, 23, 42]
target = 15
```

Use `for`, `break`, and loop `else` to print whether the target was found.

---

## Exercise 6

Use `enumerate()`:

```python
items = ["red", "green", "blue"]
```

Print:

```text
0 red
1 green
2 blue
```

---

## Exercise 7

Avoid mutation while iterating.

Start with:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Build a new list containing only odd numbers.

Explain why this is safer than removing items from the original list during iteration.

---

# Summary

In this chapter we learned:

* Control flow determines which code runs and how often.
* Python normally executes statements top to bottom.
* `if` runs a block when its condition is truthy.
* `elif` checks additional conditions in order.
* `else` runs when no previous branch was selected.
* Indentation defines blocks.
* Branch order matters.
* `while` repeats while a condition is truthy.
* `while` loops need a path to stop.
* `for` loops iterate over iterables.
* Loop variables are names rebound each iteration.
* `range()` represents integer sequences and excludes the stop value.
* `break` exits the nearest loop.
* `continue` skips the rest of the current iteration.
* Loop `else` runs only if no `break` occurred.
* Mutating collections while iterating can cause bugs.
* `enumerate()` provides index and value.
* `zip()` iterates multiple iterables together.

The core model is:

```text
condition expression
    |
    v
truthiness
    |
    v
execution path
```

Control flow turns expressions into decisions and repetition.

---

# Preview of Chapter 19

Next we study functions.

Control flow lets us decide what code runs.

Functions let us package code into reusable units.

We will study:

* Function definition
* Function calls
* Parameters
* Arguments
* Return values
* Local names
* Function design
* Side effects
* Call frames

Functions combine everything so far:

```text
objects
names
expressions
operators
control flow
```

into reusable behavior.
