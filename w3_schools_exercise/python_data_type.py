# Text Type
text_var = str("Hello, world!")
print(type(text_var))

# Numeric Types
int_var = int(42)
print(type(int_var))

float_var = float(3.14)
print(type(float_var))

complex_var = complex(2, 3)
print(type(complex_var))

# Sequence Types
list_var = list([1, 2, 3])
print(type(list_var))

tuple_var = tuple((4, 5, 6))
print(type(tuple_var))

range_var = range(3)
print(type(range_var))

# Mapping Type
dict_var = dict({'a': 1, 'b': 2})
print(type(dict_var))

# Set Types
set_var = set([1, 2, 3])
print(type(set_var))

frozenset_var = frozenset([4, 5, 6])
print(type(frozenset_var))

# Boolean Type
bool_var = bool(True)
print(type(bool_var))

# Binary Types
bytes_var = bytes("hello", "utf-8")
print(type(bytes_var))

bytearray_var = bytearray(b"world")
print(type(bytearray_var))

memoryview_var = memoryview(b"abc")
print(type(memoryview_var))

# None Type
none_var = None
print(type(none_var))
