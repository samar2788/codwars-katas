def caffeine_buzz(n):
    if n%3==0 and n%4==0:
        return "CoffeeScript"
    elif n%3==0 and n%2==0:
        return "JavaScript"
    elif n%3==0:
        return 'Java'
    else:
        return "mocha_missing!"


print(caffeine_buzz(1))
print(caffeine_buzz(2),)
print(caffeine_buzz(3), "Java")
print(caffeine_buzz(4), "mocha_missing!")
print(caffeine_buzz(5), "mocha_missing!")
print(caffeine_buzz(6), "JavaScript")
print(caffeine_buzz(7), "mocha_missing!")
print(caffeine_buzz(8), "mocha_missing!")
print(caffeine_buzz(9), "Java")
print(caffeine_buzz(10))
print(caffeine_buzz(11))
print(caffeine_buzz(12))