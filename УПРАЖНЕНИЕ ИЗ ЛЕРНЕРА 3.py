#задание 3
def run_timeeee():
    times = []
    while True:
        one_run = input("введите время пробега 10 км в минутах: ")
        if not one_run:
            break
        try:
            time = float(one_run)
            times.append(time)
        except ValueError:
            print("недопустимое значение")

    if times:
        average_time = sum(times) / len(times)
        print(f"средний показатель {average_time:.1f}, {len(times)} пробежек")
    else:
        print("не было введено ни одной пробежки. пробеги")

# Вызов функции
run_timeeee()