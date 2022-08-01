#!/usr/bin/python3
""" Converts roman numbers between 1 and 3999 to int """

to_10 = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
    'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
to_20 = {
    'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
    'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX':20
}
to_30 = {
    'XXI': 21, 'XXII': 22, 'XXIII': 23, 'XXIV': 24, 'XXV': 25,
    'XXVI': 26, 'XXVII': 27, 'XXVIII': 28, 'XXIX': 29, 'XXX': 30
}
to_40 = {
    'XXXI': 31, 'XXXII': 32, 'XXXIII': 33, 'XXXIV': 34, 'XXXV': 35,
    'XXXVI': 36, 'XXXVII': 37, 'XXXVIII': 38, 'XXXIX': 39, 'XL': 40
}
to_50 = {
    'XLI': 41, 'XLII': 42, 'XLIII': 43, 'XLIV': 44, 'XLV': 45,
    'XLVI': 46, 'XLVII': 47, 'XLVIII': 48, 'XLIX': 49, 'L': 50
}
to_60 = {
    'LI': 51, 'LII': 52, 'LIII': 53, 'LIV': 54, 'LV': 55,
    'LVI': 56, 'LVII': 57, 'LVIII': 58, 'LIX': 59, 'LX': 60
}
to_70 = {
    'LXI': 61, 'LXII': 62, 'LXIII': 63, 'LXIV': 64, 'LXV': 65,
    'LXVI': 66, 'LXVII': 67, 'LXVIII': 68, 'LXIX': 69, 'LXX': 70
}
to_80 = {
    'LXXI': 71, 'LXXII': 72, 'LXXIII': 73, 'LXXIV': 74, 'LXXV': 75,
    'LXXVI': 76, 'LXXVII': 77, 'LXXVIII': 78, 'LXXIX': 79, 'LXXX': 80
}
to_90 = {
    'LXXXI': 81, 'LXXXII': 82, 'LXXXIII': 83, 'LXXIV': 84, 'LXXXV': 85,
    'LXXXVI': 86, 'LXXXVII': 87, 'LXXXVIII': 88, 'LXXXIX': 89, 'XC': 90
}
to_100 = {
    'XCI': 91, 'XCII': 92, 'XCIII': 93, 'XCIV': 94, 'XCV': 95,
    'XCVI': 96, 'XCVII': 97, 'LXXVIII': 98, 'XCIX': 99, 'C': 100
}

def one_to_hundred(roman_string):
    if roman_string in to_10:
            return to_10.get(roman_string)
    elif roman_string in to_20:
        return to_20.get(roman_string)
    elif roman_string in to_30:
        return to_30.get(roman_string)
    elif roman_string in to_40:
        return to_40.get(roman_string)
    elif roman_string in to_50:
        return to_50.get(roman_string)
    elif roman_string in to_60:
        return to_60.get(roman_string)
    elif roman_string in to_70:
        return to_70.get(roman_string)
    elif roman_string in to_80:
        return to_80.get(roman_string)
    elif roman_string in to_90:
        return to_90.get(roman_string)
    elif roman_string in to_100:
        return to_100.get(roman_string)

def roman_to_int(roman_string):
    """ Validate input """
    if roman_string is not None and type(roman_string) is str:
        
        return one_to_hundred(roman_string)
    else:
        return 0

while True:
    result = roman_to_int(input("Enter roman: ").upper())
    print(result)