# 08_regex.py

import re


pattern = r'^(\+420\s?)(\d{3}\s?\d{3}\s?\d{3})|(\d{3}\s?\d{3}\s?\d{3})(?=$|\s)'
pattern_compile = re.compile(pattern)

def check_phone_number(text: str) -> bool:

    if pattern_compile.search(text):
        return True
    return False

print(check_phone_number('test'))  # -> False
print(check_phone_number('608 192 292'))  # -> True
print(check_phone_number('608 192 292...'))  # -> False
print(check_phone_number('+420 777 777 777'))  # -> True
print(check_phone_number('777 777 777'))  # -> True
print(check_phone_number('+420777777777'))  # -> True
print(check_phone_number('777777777'))  # -> True
print(check_phone_number('sad +420 777 777 777 dada')) # -> True
print(check_phone_number('+420 777 777 777abc'))  # False  xxx
print(check_phone_number('00420777777777'))  # False  xxx
print(check_phone_number('++420777777777'))  # False  xxx
print(check_phone_number('+420   777 777 777'))  # True
print(check_phone_number('abc +420 777 777 777'))  # False  xxxx
print(check_phone_number('+420777777777'))  # True 
print(check_phone_number('777 777 777'))  # True
print(check_phone_number('777777777'))  # True
