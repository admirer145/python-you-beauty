# Curriculum Principles

## 1. Dependency Order

Never teach advanced concepts before prerequisites.

Correct flow:

Computer
↓
CPU, Memory, and Storage
↓
Program Execution
↓
Process
↓
Operating System
↓
Interpreter
↓
Bytecode
↓
Objects
↓
Type, Value, and Identity
↓
Names and References
↓
Assignment
↓
Mutability
↓
Equality and Memory Diagrams
↓
Numbers
↓
Strings
↓
Booleans
↓
Operators
↓
Expressions
↓
Conditionals
↓
Loops
↓
Function Objects
↓
Parameters and Arguments
↓
Scope and Namespaces
↓
Closures
↓
Call Stack and Stack Frames
↓
Recursion
↓
Functional Programming
↓
Built-in Data Structures
↓
Comprehensions
↓
Specialized Data Structures
↓
Custom Data Structures
↓
Stack vs Heap
↓
Reference Counting
↓
Garbage Collection
↓
Object Lifecycle
↓
Weak References
↓
Modules and Imports
↓
Virtual Environments
↓
Classes and Instances
↓
Attributes and Methods
↓
Encapsulation and Managed Attributes
↓
Composition
↓
Inheritance and Method Overriding
↓
MRO and `super()`
↓
Polymorphism
↓
Duck Typing
↓
ABCs and Mixins
↓
Dataclasses
↓
Dunder Methods
↓
Operator Overloading
↓
Descriptors
↓
Properties, Static Methods, and Class Methods
↓
`__slots__`
↓
Metaclasses
↓
Iterators
↓
Generators
↓
Context Managers
↓
Decorators
↓
Exceptions
↓
Files and Serialization
↓
Standard Library
↓
Concurrency Foundations
↓
Threads, Processes, and the GIL
↓
Asyncio and Event Loops
↓
Runtime Type System
↓
Bytecode Internals
↓
CPython Architecture
↓
C Extensions
↓
Testing
↓
Mocking and Monkey Patching
↓
Debugging
↓
Logging
↓
Packaging
↓
Type Hints
↓
Static Type Checking
↓
Profiling
↓
Design Patterns
↓
SOLID Principles
↓
Architecture
↓
APIs
↓
Microservices
↓
Ecosystem Frameworks and Libraries
↓
Career Specialization
↓
Capstone Projects

---

## 2. Every Chapter Must Contain

* Concept Overview
* Mental Model
* Why It Exists
* Internal Mechanics
* Examples
* Common Mistakes
* Real-world Usage
* Concept Connections
* Active Recall Questions
* Practical Exercises

---

## 3. Teaching Philosophy

Never teach:

"What"

without teaching:

"Why"

and

"How"

Avoid magic explanations.

---

## 4. Progression

Beginner
↓
Understanding
↓
Mental Models
↓
Implementation Details
↓
Engineering
↓
Internals
↓
Mastery

---

## 5. Volume Order

Volume I
Foundations and Core Language

Volume II
Advanced Python and Internals

Volume III
Software Engineering

Volume IV
Ecosystem and Career Paths

Capstone Projects
Applied synthesis after the required foundations are in place.

---

## 6. Structural Decision

Use the four-volume structure as the primary book structure.

Volume I should be part-wise because it has the densest dependency chain and the highest risk of confusing learners if topics are grouped too broadly.

Volume II should group advanced Python by conceptual mechanism:

* Object-oriented Python
* Python data model
* Pythonic abstractions
* Robust programs and I/O
* Concurrency and parallelism
* Type system and internals

Volume III should focus on production engineering practice.

Volume IV should focus on ecosystems, domains, and career paths.

---

## 7. Rule Against Deflection

Do not skip chapters.

Do not merge chapters unless explicitly planned.

Do not leave zero-length chapter placeholders in the manuscript.

Maintain strict dependency order.

---

## 8. Final Objective

A learner completing the curriculum should understand:

* Python
* CPython
* Software engineering
* Computer science fundamentals
* Real-world usage

well enough that only official documentation and domain-specific specialization resources remain necessary.
