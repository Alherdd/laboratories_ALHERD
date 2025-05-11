# РОМЕНКО ЯН 48 ГРУППА 1 КУРС
# VAR1

def reccurent_rel(n, k):
      if n < 1 or k < 0:
        raise ValueError("Некорректные входные данные: n ≥ 1, k ≥ 0")
    
   
      if n == 1 or n == 2:
            return 1

      F = [0] * (n + 1)

      F[1] = 1
      F[2] = 1
       
      for i in range(3, n + 1):
            F[i] = F[i - 1] + (k * F[i - 2])

      return F[n]

while True:
        try:
            n = int(input("Введите количество месяцев: "))
            k = int(input("Введите начальное количество пар кроликов: "))
            if n < 1 or k < 0:
                print("Ошибка: значения должны быть ≥1 и ≥0!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целые числа!")

result = reccurent_rel(n, k)
print(f"Общее число кроличьих пар на {n} месяц: {result}")
