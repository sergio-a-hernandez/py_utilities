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

    def __str__(self):
        return self.value

    def __repr__(self):
        return repr(self.value)

    def clone(self):
        return self.value[:]

    def compare_to(self, other):
        return 0 if self.value == other else 1

    def contains(self, sub_str):
        return sub_str in self.value

    def ends_with(self, end_str):
        return self.value.endswith(end_str)

    def equals(self, other):
        return self.value == other

    def get_hash_code(self):
        return hash(self.value)

    def get_type(self):
        return type(self.value)

    def index_of(self, char):
        return self.value.index(char)

    def to_lower(self):
        return self.value.lower()

    def to_upper(self):
        return self.value.upper()

    def insert(self, index, insert_str):
        return self.value[:index] + insert_str + self.value[index:]

    def last_index_of(self, char):
        return self.value.rindex(char)

    def length_of(self):
        return len(self.value)

    def remove(self, index):
        return self.value[:index]

    def replace(self, old_char, new_char):
        return self.value.replace(old_char, new_char)

    def split(self, delimiter):
        return self.value.split(delimiter)

    def starts_with(self, char):
        return self.value.startswith(char)

    def substring(self, start, end):
        return self.value[start:end]

    def to_char_array(self):
        return list(self.value)

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

    fn = "Steven Clark"
    ln = "Clark"

    print (firstname + lastname)
    print (firstname + ln)
    print (firstname - lastname)
    print (firstname - ln)

    print(firstname.clone())
    print(firstname.compare_to(lastname))
    print(firstname.contains("ven"))
    print(firstname.ends_with("n"))
    print(firstname.equals(lastname))
    print(firstname.get_hash_code())
    print(firstname.get_type())
    print(firstname.index_of("e"))
    print(firstname.to_lower())
    print(firstname.to_upper())
    print(firstname.insert(0, "Hello"))
    print(firstname.last_index_of("e"))
    print(firstname.length_of())
    print(firstname.remove(5))
    print(firstname.replace('e', 'i'))
    
    split = firstname.split('e')
    for part in split:
        print(part)

    print(firstname.starts_with("S"))
    print(firstname.substring(2, 7))
    print(firstname.to_char_array())
    print(firstname.trim())

    numero_decimal = String("1234")
    numero_octal = String("01234")
    numero_hexadecimal = String("0x1234")
    texto_no_numerico1 = String("abc123")
    texto_no_numerico2 = String("0abc123")
    texto_no_numerico3 = String("0xgbc123")

    print("Convertir a valor:")
    print("Decimal:", numero_decimal.to_value())
    print("Octal:", numero_octal.to_value())
    print("Hexadecimal:", numero_hexadecimal.to_value())
    print("Texto no numérico:", texto_no_numerico1.to_value())
    print("Texto no numérico:", texto_no_numerico2.to_value())
    print("Texto no numérico:", texto_no_numerico3.to_value())
