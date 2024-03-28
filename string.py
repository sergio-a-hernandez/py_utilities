import re

class String:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, String):
            return String(self.value + other.value)
        elif isinstance(other, str):
            return String(self.value + other)
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, String):
            return String(self.value.replace(other.value, ""))
        if isinstance(other, str):
            return String(self.value.replace(other, ""))
        else:
            raise TypeError("Unsupported operand type for -: {}".format(type(other)))

    def __ne__(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))
        if isinstance(other, String):
            return self.value != other.value
        if isinstance(other, str):
            return self.value != other


    def __lt__(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))
        if isinstance(other, String):
            return self.value < other.value
        if isinstance(other, str):
            return self.value < other

    def __le__(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))
        if isinstance(other, String):
            return self.value <= other.value
        if isinstance(other, str):
            return self.value <= other

    def __eq__(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))
        if isinstance(other, String):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other

    def __ge__(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))
        if isinstance(other, String):
            return self.value >= other.value
        if isinstance(other, str):
            return self.value >= other

    def __gt__(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))
        if isinstance(other, String):
            return self.value > other.value
        if isinstance(other, str):
            return self.value > other

    def __str__(self):
        return self.value

    def __repr__(self):
        return "String('{}')".format(self.value)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.value):
            result = self.value[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, sub_str):
        return sub_str in self.value

    def __len__(self):
        return len(self.value)

    def __getitem__(self, index):
        return self.value[index]

    def __setitem__(self, index, value):
        # Permitir asignación de elementos por índice
        self.value = self.value[:index] + str(value) + self.value[index+1:]

    def __delitem__(self, index):
        # Permitir eliminación de elementos por índice
        self.value = self.value[:index] + self.value[index+1:]

    def __reversed__(self):
        return String(self.value[::-1])

    def __hash__(self):
        return hash(self.value)
    
    def append(self, *args):
        for arg in args:
            self.value += arg.value if isinstance(arg, String) else str(arg)
        return self.value

    def capitalize(self):
        return self.value.capitalize()

    def center_pad(self, chars, char):
        return self.value.center(chars, char)
    
    def clone(self):
        return self.value[:]

    def compare_to(self, other):
        if not isinstance(other, String) and not isinstance(other, str):
            raise TypeError("Unsupported operand type for comparison: {}".format(type(other)))

        if isinstance(other, String):
            if self.value < other.value:
                return -1
            elif self.value == other.value:
                return 0
            else:
                return 1
        if isinstance(other, str):
            if self.value < other:
                return -1
            elif self.value == other:
                return 0
            else:
                return 1

    def contains(self, sub_str):
        return sub_str in self.value

    def count(self, sub_str):
        return self.value.count(sub_str)

    def ends_with(self, end_str):
        return self.value.endswith(end_str)

    def equals(self, other):
        return self.value == other.value

    def get_hash_code(self):
        return hash(self.value)

    def get_type(self):
        return type(self.value)

    def index_of(self, char):
        return self.value.find(char)

    def to_lower(self):
        return self.value.lower()

    def to_upper(self):
        return self.value.upper()

    def insert(self, index, insert_str):
        return self.value[:index] + insert_str + self.value[index:]

    def is_alpha(self):
        return self.value.isalpha()

    def is_alphanumeric(self):
        return self.value.isalnum()

    def is_ascii(self):
        return self.value.isascii()

    def is_decimal(self):
        return self.value.isdecimal()

    def is_digit(self):
        return self.value.isdigit()

    def is_identifier(self):
        return self.value.isidentifier()

    def is_lower(self):
        return self.value.islower()

    def is_numeric(self):
        return self.value.isnumeric()

    def is_printable(self):
        return self.value.isprintable()

    def last_index_of(self, char):
        return self.value.rindex(char)

    def left_strip(self):
        return self.value.lstrip()

    def length(self):
        return len(self.value)

    def pad(self, length, pad_string=' ', pad_type='right'):
        if pad_type == 'right':
            return String(self.value.ljust(length, pad_string))
        elif pad_type == 'left':
            return String(self.value.rjust(length, pad_string))
        elif pad_type == 'both':
            return String(self.value.center(length, pad_string))
        else:
            raise ValueError("Invalid pad_type. Use 'right', 'left', or 'both'.")

    def right_strip(self):
        return self.value.rstrip()

    def remove(self, index):
        return self.value[:index]

    def replace(self, old_char, new_char):
        return self.value.replace(old_char, new_char)

    def split(self, delimiter):
        return self.value.split(delimiter)

    def starts_with(self, char):
        return self.value.startswith(char)

    def strip(self):
        return self.value.strip()

    def substring(self, start, end):
        return self.value[start:end]

    def swap_case(self):
        return self.value.swapcase()

    def to_char_array(self):
        return list(self.value)

    def to_title(self):
        return self.value.title()

    def trim(self):
        return self.value.strip()

    def to_value(self):
        # Octal
        octal_match = re.match(r'^0[0-7]+$', self.value)
        if octal_match:
            return int(self.value, 8)

        # Decimal
        decimal_match = re.match(r'^-?\d*\.?\d+$', self.value)
        if decimal_match:
            return float(self.value)

        # Hexadecimal
        hex_match = re.match(r'^0x[0-9a-fA-F]+$', self.value)
        if hex_match:
            return int(self.value, 16)

        # Si no es posible convertir, devolver None
        return None


if __name__ == "__main__":
    firstname = String("Steven Clark")
    lastname = String("Clark")
    new_firstname = String("Steven")
    new_firstname.append(" Clark", " Kent")
    print(repr(new_firstname)) 
    print("Append: ", new_firstname)

    fn = "Steven Clark"
    ln = "Clark"

    print (firstname + lastname)
    print (firstname + ln)
    print (firstname - lastname)
    print (firstname - ln)

    print(firstname.capitalize())
    print(firstname.center_pad(16,"#"))
    print(firstname.pad(16,"#"))
    print(firstname.pad(16,"#", "left"))
    print(firstname.clone())
    print("Compare: ", firstname.compare_to(lastname))
    print("Compare: ", firstname.compare_to(fn))
    print(firstname.contains("ven"))
    print(firstname.count("e"))
    print(firstname.ends_with("n"))
    print(firstname.equals(lastname))
    print(firstname.get_hash_code())
    print(firstname.get_type())
    print(firstname.index_of("e"))
    print(firstname.to_lower())
    print(firstname.to_upper())
    print(firstname.insert(0, "Hello"))
    print(firstname.last_index_of("e"))
    print(firstname.length())
    print(firstname.remove(5))
    print(firstname.replace('e', 'i'))
    
    split = firstname.split('e')
    for part in split:
        print(part)

    print(firstname.starts_with("S"))
    print(firstname.substring(2, 7))
    print(firstname.swap_case())
    print(firstname.to_char_array())
    print(firstname.to_title())
    print(firstname.trim())

    numero_decimal = String("1234.55")
    numero_octal = String("01234")
    numero_hexadecimal = String("0x1234")
    texto_no_numerico1 = String("abc123")
    texto_no_numerico2 = String("0abc123")
    texto_no_numerico3 = String("0xgbc123")

    print(numero_decimal.value.isalnum())

    print("Convertir a valor:")
    print("Decimal:", numero_decimal.to_value())
    print("Octal:", numero_octal.to_value())
    print("Hexadecimal:", numero_hexadecimal.to_value())
    print("Texto no numérico:", texto_no_numerico1.to_value())
    print("Texto no numérico:", texto_no_numerico2.to_value())
    print("Texto no numérico:", texto_no_numerico3.to_value())

    my_string = String("Hello")

    # Recorrer cada caracter del string
    for char in my_string:
        print(char)

    reversed_string = reversed(my_string)

    # Imprimir la cadena inversa
    for char in reversed_string:
        print(char)

    my_string = String("Hello, World!")
    print("World" in my_string)
    print("Python" in my_string)
    print(len(my_string))
    print(my_string[2])
    my_string[1] = "i"
    print(my_string)
    del my_string[3]
    print(my_string)
    my_string = String("example")
    hash_value = hash(my_string)
    print(hash_value)
