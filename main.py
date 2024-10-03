# input_func == get_sum
def decorator(input_func):
    # new_func == "новый функционал get_sum"
    def new_func(a, b):
        result = input_func(a, b)
        return f"Сумма чисел {a} и {b} равна {result}"
    return new_func


# название декоратора
@decorator
def get_sum(a, b):
    return a + b


if __name__ == "__main__":
    f = 5
    s = 6
    res = get_sum(f, s)
    print(res)