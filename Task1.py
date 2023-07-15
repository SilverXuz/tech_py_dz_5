"""
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»без перехода на новую строку.
 (расположение)
 1 2 3 4
 5 6 7 8
"""

def main():
    min_val = 2
    max_val = 10
    one_row(min_val, max_val)


def one_row(min_val, max_val):
    for i in range(min_val, max_val):
        for j in range(min_val, min_val + 4):
            z = j * i
            print(f"{j} * {i} = {z}", end="\t")
        print()
    print()

    for i in range(min_val, max_val):
        for j in range(min_val + 4, max_val):
            z = j * i
            print(f"{j} * {i} = {z}", end="\t")
        print()


if __name__ == '__main__':
    main()
