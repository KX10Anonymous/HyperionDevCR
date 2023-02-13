def say_num(number):
    ones = ["", "one", "two", "three", "four", "five", "six", " seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if number < 20:
        return ones[number]
    if number < 100:
        return tens[number // 10] + (ones[number % 10] if number % 10 != 0 else " ")
    if number < 1000:
        return ones[number // 100] + " hundred " + (say_num(number % 100) if number % 100 != 0 else " ")
    if number < 1000000:
        return say_num(number // 1000) + " thousand " + (say_num(number % 1000) if number % 1000 != 0 else " ")
    if number < 1000000000:
        return say_num(number // 1000000) + " million " + (say_num(number % 1000000) if number % 1000000 != 0 else " ")
    if number < 1000000000000:
        return say_num(number // 1000000000) + " billion " + (
            say_num(number % 1000000000) if number % 1000000000 != 0 else " ")
    if number < 1000000000000000:
        return say_num(number // 1000000000000) + " trillion " + (
            say_num(number % 1000000000000) if number % 1000000000000 != 0 else " ")
    return say_num(number // 1000000000000000) + " quadrillion " + (
        say_num(number % 1000000000000000) if number % 1000000000000000 != 0 else " ")




