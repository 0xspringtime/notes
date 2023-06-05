# Object-Oriented Programming

## Primitives, Composition, Abstraction, and Patterns (PCAP)

- Data: primitives like integers, floating points, strings combined into data structures like lists, arrays, dictionaries

- Abstract Data Type: high-level conceptual model that defines a set of operations or behaviors on a particular data type, without specifying the implementation details. It describes what operations can be performed on the data and what behavior is expected from those operations

- Procedures: things like built-in numeric ooperations and basic list operations, combined by things like if/while

- Objects: Combine primitive data elements

- Simple Expressions: consist of a seques of tokens (words, special symbols, numerals) that represent the application of operators to data elements

- Variables: name that we can bind to have a balue later used in an expression, kept track of in binding environment

- Structured Data: Type of data stricture, a list in python, struct in C; ordered sequence of memory locations containing values

- Mutable: data structures where we can change values stored in their elements

- deep copy: creates a new object and recursively copies all the nested objects within it, including any mutable objects contained within the original object. This ensures that changes made to the copied object do not affect the original object, and vice versa.

- Tuple: Structure like a list but not mutable

- String: Type of tuple made up of characters

- Procedures: constructs capturing common computation patterns by gathering sequences of statements and abstracting away particular data items, def in python

### Python Binding Environments

- __builtin__: the mother of all environments: it contains the definitions of all sorts of basic
symbols, like list and sum. It is the parent of all module environments

- Module: each separate file that contains Python code is called a module and establishes its
own environment, whose parent is __builtin__

- Procedure calls: A procedure that is defined at the ’top level’ of a module (that is, not nested in the definition of another procedure) has the module’s environment as its parent, and has its name defined in the module’s environment. Procedures that are defined inside other procedures have the procedure-call environment of the containing procedure as their parent

## OOP

- Instance: collection of data that sescribe a single entity in our domain of interest

- Class: Colletion of instance members with some shared data values or similar operations we want to perform with

- classes and instances are environments

- Method: procedure associated with a particular class

- Inheritance: allows class to inherit properties (instances and methods) of another class

- Subclass: derived/child class; inherits properties from superclass/parent class

- 
