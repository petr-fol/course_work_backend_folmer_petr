from utils import *


def main():

    operations = get_operations()
    print(operations)
    operations_objects_list = operations_as_objects(operations)

    five_execute_operations = get_five_execute_operations(operations_objects_list)

    for operation in five_execute_operations:
        print(print_receipt(operation))


if __name__ == '__main__':
    main()
