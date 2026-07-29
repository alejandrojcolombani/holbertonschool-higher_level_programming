# Python 3: Mutable, Immutable... Everything Is an Object!

Python's statement that "everything is an object" explains behavior that can
otherwise feel surprising: two variables can share a value without referring
to the same object, changing a list through one variable can affect another
variable, and changing an integer creates a new object instead of modifying the
old one.

Understanding identity, type, mutability, and assignment makes these behaviors
predictable.

## Identity, type, and value

Every Python object has three important characteristics:

- **Identity** distinguishes the object from every other object during its
  lifetime. `id()` returns an integer representing that identity.
- **Type** determines the operations the object supports. `type()` reports it.
- **Value** is the data represented by the object.

```python
score = 42

print(id(score))
print(type(score))  # <class 'int'>
print(score)        # 42
```

A variable is a name bound to an object. Assignment does not automatically copy
that object:

```python
first = [1, 2, 3]
second = first

print(first is second)  # True
```

Both names refer to one list. The `is` operator tests identity, while `==`
tests value equality:

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)  # True: equal values
print(first is second)  # False: different objects
```

Identity comparisons are appropriate for singletons such as `None`:

```python
if result is None:
    print("No result")
```

Value comparisons should normally use `==`.

## Mutable objects

A mutable object's contents can change without changing its identity. Common
built-in mutable types include:

- lists
- dictionaries
- sets
- byte arrays

```python
numbers = [1, 2, 3]
before = id(numbers)

numbers.append(4)

print(numbers)              # [1, 2, 3, 4]
print(id(numbers) == before)  # True
```

The list was modified in place. This matters when aliases exist:

```python
primary = [1, 2, 3]
alias = primary
alias.append(4)

print(primary)  # [1, 2, 3, 4]
```

Because `primary` and `alias` refer to the same mutable object, the mutation is
visible through both names.

## Immutable objects

An immutable object's value cannot change after the object is created. Common
built-in immutable types include:

- integers and floating-point numbers
- booleans
- strings
- tuples
- bytes
- frozen sets

An operation that appears to "change" an immutable value actually creates or
selects another object and rebinds the variable:

```python
count = 10
before = id(count)

count += 1

print(count)               # 11
print(id(count) == before) # False
```

The integer object representing `10` was not modified. The name `count` was
rebound to an integer object representing `11`.

Strings behave similarly:

```python
message = "Hello"
alias = message
message += ", Python!"

print(message)  # Hello, Python!
print(alias)    # Hello
```

The original string remains unchanged.

## Tuples and contained objects

A tuple is immutable because its references cannot be replaced after creation.
That does not guarantee that every object inside the tuple is immutable:

```python
record = ("items", [1, 2])
record[1].append(3)

print(record)  # ('items', [1, 2, 3])
```

The tuple still refers to the same two objects. Its list element changed
internally, but the tuple itself was not assigned a different element.

## Assignment, copying, and aliasing

Assignment creates another reference, not a copy:

```python
original = [1, 2, 3]
alias = original
```

A shallow copy creates a new outer container:

```python
original = [1, 2, 3]
copied = original[:]

print(copied == original)  # True
print(copied is original)  # False
```

For nested containers, a shallow copy still shares the inner objects:

```python
original = [[1], [2]]
copied = original.copy()
copied[0].append(99)

print(original)  # [[1, 99], [2]]
```

When all nested objects must be independent, `copy.deepcopy()` may be the right
tool. It should be used deliberately because deep copying can be expensive and
not every object should be duplicated.

## Augmented assignment depends on the type

The same syntax can produce different identity behavior:

```python
numbers = [1, 2]
alias = numbers
numbers += [3]

print(numbers is alias)  # True
```

Lists usually implement `+=` as an in-place mutation. Ordinary addition creates
a new list:

```python
numbers = [1, 2]
alias = numbers
numbers = numbers + [3]

print(numbers is alias)  # False
print(alias)             # [1, 2]
```

For an immutable integer, `+=` cannot mutate the integer:

```python
number = 1
alias = number
number += 1

print(number)  # 2
print(alias)   # 1
```

## How Python passes arguments

Python passes object references by assignment. A function receives a local name
bound to the same object supplied by the caller.

Mutating that object can affect the caller:

```python
def add_item(items):
    items.append("new")


values = []
add_item(values)
print(values)  # ['new']
```

Rebinding the local parameter does not rebind the caller's variable:

```python
def increment(number):
    number += 1


value = 10
increment(value)
print(value)  # 10
```

This is not two different argument-passing systems. In both examples, the
parameter is initially bound to the supplied object. The difference is that the
first function mutates a list, while the second rebinds its local name after an
integer operation.

## Why mutability matters

Mutability affects program correctness and API design. Shared mutable objects
can make efficient collaboration possible, but unintended aliases can also
produce difficult bugs. Useful habits include:

- Use `==` for values and `is` for identity, especially `is None`.
- Copy a mutable container when independent state is required.
- Document whether a function mutates arguments.
- Avoid mutable default arguments such as `def add(value, items=[])`.
- Remember that immutable containers can contain mutable objects.
- Do not depend on implementation details such as small-integer caching or
  string interning when deciding whether values are equal.

Once variables are understood as names bound to objects, Python's behavior
becomes consistent: assignment shares references, mutation changes an existing
object, and operations on immutable values produce new bindings.
