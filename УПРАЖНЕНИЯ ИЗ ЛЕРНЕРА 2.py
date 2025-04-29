def mysum(*numb):
    total = 0
    for number in numb:
        total += number
    return total

print(mysum(78, 54.2, 3))
print(mysum(10, 20.76, 30, 40.006, 50))


def sr(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
print(sr(5, 2, 4, 10))


def l_w(*words):
    if not words:
        return (0, 0, 0)
    lengths = [len(word) for word in words]
    return (min(lengths), max(lengths), sum(lengths) / len(lengths))
print(l_w("воздух", "глагол" , "красота", "ветер"))


def sumint(*objects):
    total = 0
    for obj in objects:
        try:
            total += int(obj)
        except (ValueError, TypeError):
            continue
    return total
print(sumint("хламидомонада", 88.765, 20, 0.8))