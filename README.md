# Python: From First Principles to Professional Engineering

> A complete first-principles journey into Python, CPython internals, software engineering, and the Python ecosystem.

## Philosophy

This project aims to be the definitive Python curriculum.

The objective is not merely learning syntax.

The objective is mastery.

Every concept answers:

* What is it?
* Why does it exist?
* What problem does it solve?
* How does it work?
* How is it implemented?
* What are the tradeoffs?
* How does it connect to previous concepts?

The curriculum follows strict dependency order and avoids unexplained magic.

---

# Target Audience

* Beginners seeking deep understanding.
* Intermediate developers wanting solid foundations.
* Professional engineers transitioning into Python.
* Interview preparation.
* Open-source contributors.
* Engineers interested in CPython internals.

---

# Book Structure

## Volume I — Foundations and Core Language

Volume I builds the complete mental model required before advanced Python feels natural. It starts below Python, moves through execution, objects, references, primitive types, control flow, functions, data structures, memory behavior, and finally modules/imports.

### Part I — Foundations of Computing

1. What Is Software?
2. Computer Architecture
3. Processes and Execution
4. Operating Systems

### Part II — Understanding Python

5. History and Philosophy of Python
6. Python Implementations
7. How Python Runs: Source Code to Bytecode
8. Bytecode and the Python Virtual Machine

### Part III — Objects and References

9. Everything Is an Object
10. Names and References
11. Mutability
12. Identity, Equality, and Memory Diagrams

### Part IV — Primitive Types and Expressions

13. Numbers
14. Strings
15. Booleans
16. Operators
17. Expressions

### Part V — Control Flow

18. Conditionals
19. Loops

### Part VI — Functions

20. Functions, Parameters, and Return Values
21. Scope and Namespaces
22. Closures
23. Call Stack and Stack Frames
24. Recursion
25. Functional Programming

### Part VII — Data Structures

26. Lists
27. Tuples
28. Dictionaries
29. Sets
30. Comprehension Patterns
31. Specialized Collections: `deque`, `Counter`, `defaultdict`, `heapq`, and `bisect`
32. Custom Data Structures

### Part VIII — Memory Management

33. Stack vs Heap
34. Reference Counting
35. Garbage Collection
36. Object Lifecycle
37. Weak References

### Part IX — Modules and Imports

38. Modules
39. Packages
40. Import System
41. Namespaces
42. Virtual Environments

---

## Volume II — Advanced Python and Internals

Volume II moves from using Python correctly to understanding Python's advanced protocols, object model, runtime behavior, and implementation mechanics.

### Part I — Object-Oriented Python

43. Classes and Instances
44. Attributes and Methods
45. Encapsulation and Managed Attributes
46. Composition
47. Inheritance and Method Overriding
48. MRO and `super()`
49. Polymorphism and Duck Typing
50. ABCs and Mixins
51. Dataclasses

### Part II — The Python Data Model

52. Dunder Methods
53. Operator Overloading
54. Descriptors
55. Properties, Static Methods, and Class Methods
56. `__slots__`
57. Metaclasses

### Part III — Pythonic Abstractions

58. Iterators
59. Generators
60. Context Managers
61. Decorators

### Part IV — Robust Programs and I/O

62. Exceptions
63. Files and Serialization
64. Standard Library Deep Dive

### Part V — Concurrency and Parallelism

65. Concurrency Foundations
66. Threads, Processes, and the GIL
67. Asyncio and Event Loops

### Part VI — Type System and Internals

68. Runtime Type System
69. Bytecode Internals
70. CPython Architecture
71. C Extensions

---

## Volume III — Software Engineering

Volume III turns Python knowledge into production engineering practice.

72. Testing
73. Mocking and Monkey Patching
74. Debugging
75. Logging
76. Packaging
77. Type Hints
78. Static Type Checking
79. Profiling
80. Design Patterns
81. SOLID Principles
82. Architecture
83. APIs
84. Microservices

---

## Volume IV — Ecosystem and Career Paths

Volume IV connects Python mastery to real-world domains, frameworks, libraries, and professional specialization paths.

### Part I — Web Development

85. Flask
86. Django
87. FastAPI

### Part II — Data and Scientific Computing

88. NumPy
89. Pandas
90. Polars
91. SciPy

### Part III — Machine Learning and AI Engineering

92. scikit-learn
93. PyTorch
94. TensorFlow
95. AI Engineering
96. RAG Systems
97. Agents

### Part IV — Automation and Integration

98. APIs and Automation
99. Scripting for Real Workflows

### Part V — Career Paths

100. Backend Engineering
101. Data Engineering
102. Machine Learning Engineering
103. AI Engineering
104. DevOps
105. Cybersecurity

---

# Capstone Projects

Capstones are placed after the learner has the prerequisites needed to build them properly. They should reinforce the book instead of acting as disconnected exercises.

* Todo CLI
* File Organizer
* REST API
* URL Shortener
* ORM
* Task Queue
* Mini Redis
* Mini Web Framework
* Mini Event Loop
* Toy Python Interpreter
* Distributed Scheduler

---

# Goal

After completing this curriculum, the learner should need only:

* Official documentation.
* Domain-specific resources.

No general Python tutorial should be necessary.
