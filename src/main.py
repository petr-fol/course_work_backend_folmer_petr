from utils import *


def main():
    """
    Основная функция программы.
    """
    operations = get_operations()  # Получение операций

    operations_objects_list = operations_as_objects(operations)  # Преобразование операций в объекты

    # Получение пяти операций для выполнения
    five_execute_operations = get_five_execute_operations(operations_objects_list)

    print("\n")
    for operation in five_execute_operations:
        if print_receipt(operation) is not None:
            print(print_receipt(operation))


if __name__ == '__main__':
    main()