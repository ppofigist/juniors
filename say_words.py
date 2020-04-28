def number_in_inglish(number):
    list_units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    list_teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                'seventeen', 'eighteen', 'nineteen']
    list_tens = ['twenty', 'twenty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if number == 0:
        return 'zero'
    elif 0 < number < 10:
        return list_units[number - 1]
    elif 10 <= number < 20:
        return list_teen[number - 10]
    elif 20 <= number < 100 and number % 10 == 0:
        return list_tens[number // 10 - 2]
    elif 20 <= number < 100 and number % 10 != 0:
        return list_tens[number // 10 - 2] + ' ' + list_units[number % 10 - 1]
    return number_in_inglish(number // 100) + ' hundred ' + number_in_inglish(number % 100)

print(number_in_inglish(999))