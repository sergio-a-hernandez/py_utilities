# Custom `String` Class for Python

This project defines a custom `String` class that extends the capabilities of Python's built-in `str` type. It offers a wide range of string manipulation methods, operator overloading, and utility functions. The class is designed to behave like native strings while allowing intuitive operations such as string subtraction, comparison with both strings and `String` objects, and iteration.

## Features

* ✅ Operator overloading for `+`, `-`, comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`)
* ✅ Support for slicing, indexing, and iteration
* ✅ Built-in string utility methods like `capitalize`, `to_upper`, `strip`, etc.
* ✅ Additional methods like `pad`, `insert`, `compare_to`, and `to_value`
* ✅ Works seamlessly with Python strings

---

## Getting Started

No installation is required. Simply include the `String` class in your project.

```python
from your_module import String

s1 = String("Hello")
s2 = String("World")

# Concatenation
result = s1 + " " + s2
print(result)  # Output: Hello World

# Subtraction
result = result - "World"
print(result)  # Output: Hello 

# Comparison
print(s1 < s2)  # True
```

---

## Operator Overloading

| Operator                         | Behavior                                  |
| -------------------------------- | ----------------------------------------- |
| `+`                              | Concatenates `String` or native `str`     |
| `-`                              | Removes substring if found                |
| `==`, `!=`, `<`, `<=`, `>`, `>=` | Lexical comparison with `String` or `str` |
| `in`                             | Check substring presence                  |
| `[]`                             | Indexing and assignment                   |
| `len()`                          | Returns the length of the string          |
| `iter()`                         | Iterate over characters                   |
| `reversed()`                     | Returns reversed string                   |
| `hash()`                         | Hash of the internal value                |

---

## Methods Overview

### Basic Manipulation

* `append(*args)`
* `capitalize()`
* `to_upper()`, `to_lower()`, `swap_case()`, `to_title()`
* `strip()`, `left_strip()`, `right_strip()`, `trim()`
* `replace(old, new)`, `insert(index, value)`, `remove(index)`
* `split(delimiter)`, `substring(start, end)`
* `pad(length, pad_string=' ', pad_type='right')`

### Query and Comparison

* `contains(sub_str)`
* `count(sub_str)`
* `starts_with(prefix)`, `ends_with(suffix)`
* `index_of(char)`, `last_index_of(char)`
* `compare_to(other)` - Returns -1, 0, or 1

### Type and Conversion

* `equals(other)`
* `clone()`
* `get_type()`, `get_hash_code()`
* `to_char_array()`
* `to_value()` — Detects and converts numeric strings (decimal, hex, octal) to `int` or `float`

### Type Checking

* `is_alpha()`, `is_alphanumeric()`, `is_ascii()`, `is_decimal()`, `is_digit()`
* `is_identifier()`, `is_lower()`, `is_numeric()`, `is_printable()`

---

## Example

```python
s = String("123")
print(s.to_value())  # Output: 123.0

s2 = String("0xFF")
print(s2.to_value())  # Output: 255

s3 = String("abc")
print(s3.is_alpha())  # Output: True

s4 = String("Aptiv")
s4[0] = "O"
print(s4)  # Output: Optiv
```

---

## Notes

* Compatible with both Python 3.x strings and the custom `String` class.
* Improves readability and provides Java-like string handling for Python developers.
* Useful for educational purposes, DSLs, or experimenting with operator overloading.

---

## License

This project is released under the MIT License.

---

## Summary

This Python module defines an enhanced `String` class that provides extended string handling capabilities such as operator overloading, type conversions, and utility methods. It's a handy tool for developers who want more expressive string operations in Python.
