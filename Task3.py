"""
3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида “10.25%”.

В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']

result = {name: round(sal * float(pr[:-1]) / 100, 2) for name, sal, pr in zip(n, s, a)}
print(result)
