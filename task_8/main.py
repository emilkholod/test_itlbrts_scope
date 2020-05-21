def check_bank_args(money, percent, years):
    if not money > 0:
        raise Exception('Вклад должен быть положительным')
    if not percent > 0:
        raise Exception('Проценты должны быть положительными')
    if not years > 0:
        raise Exception('Срок вклада должен быть положительным')


def bank(money, percent, years):
    check_bank_args(money, percent, years)
    return round(money * (1 + percent / 100)**years, 2)


if __name__ == '__main__':
    new_money = bank(100, 10, 1.5)
    print(new_money)
