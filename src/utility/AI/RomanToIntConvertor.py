import re
import math

# Regular expression used to validate and parse Roman numbers
roman_re = re.compile("""^
   ([M]{0,9})   # thousands
   ([DCM]*)     # hundreds
   ([XLC]*)     # tens
   ([IVX]*)     # units
   $""", re.VERBOSE)

# This array contains valid groups of digits and encodes their values.
# The first row is for units, the second for tens and the third for
# hundreds. For example, the sixth element of the tens row yields the
# value 50, as the first is 0.
d2r_table = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']]


def roman2dec(roman):
    """Converts a roman number, encoded in a string, to a decimal number."""
    roman = roman.upper()
    match = roman_re.match(roman)

    if not match:
        raise ValueError

    thousands, hundreds, tens, units = match.groups()
    result = 1000 * len(thousands)
    result += d2r_table[2].index(hundreds) * 100
    result += d2r_table[1].index(tens) * 10
    result += d2r_table[0].index(units)

    return result
