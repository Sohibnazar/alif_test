import sys
from products import ProductList

def main():
    if len(sys.argv) < 3:
        print("Неверное количество аргументов")
        return

    filename = sys.argv[1]
    action = sys.argv[2]
    product_list = ProductList(filename)

    if action == "add" and len(sys.argv) == 5:
        product_name = sys.argv[3]
        product_price = sys.argv[4]
        product_list.add_product(product_name, product_price)
        print(f"Товар {product_name} добавлен.")

    elif action == "update" and len(sys.argv) == 5:
        product_name = sys.argv[3]
        new_price = sys.argv[4]
        product_list.update_product(product_name, new_price)
        print(f"Товар {product_name} обновлен.")

    elif action == "delete" and len(sys.argv) == 4:
        product_name = sys.argv[3]
        product_list.delete_product(product_name)
        print(f"Товар {product_name} удален.")

    elif action == "subtract":
        total = product_list.subtract_total()
        print(f"Общая сумма: {total}")

    else:
        print("Неверное действие или недостаточно аргументов.")

if __name__ == "__main__":
    main()
