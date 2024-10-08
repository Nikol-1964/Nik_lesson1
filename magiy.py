def create_magic_square(n):
    # Инициализация пустой матрицы n x n
    magic_square = [[0] * n for _ in range(n)]

    # Начальная позиция для 1
    num = 1
    i, j = 0, n // 2

    while num <= n**2:
        magic_square[i][j] = num  # Помещаем число в матрицу
        num += 1

        # Запоминаем текущие индексы для проверки
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j]:  # Если ячейка уже занята
            i += 1  # Перемещаемся вниз
        else:
            i, j = new_i, new_j  # Перемещаемся по диагонали

    return magic_square


def print_magic_square(magic_square):
    n = len(magic_square)
    for row in magic_square:
        print(' '.join(f'{x:2}' for x in row))


def main():
    print("Программа для создания магического квадрата.")
    while True:
        try:
            n = int(input("Введите размер стороны квадрата (нечетное число): "))
            if n % 2 == 0:
                print("Размер должен быть нечетным. Попробуйте снова.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # Создаем магический квадрат
    magic_square = create_magic_square(n)
    
    # Печатаем результат
    print(f"Магический квадрат размером {n}x{n}:")
    print_magic_square(magic_square)


if __name__ == "__main__":
    main()
