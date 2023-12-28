words = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']


def say_digit(number):
    if not number:
        return
    digit = number % 10
    number //= 10
    say_digit(number)
    print(words[digit], end=' ')


say_digit(6969)
