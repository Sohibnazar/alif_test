class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f"{self.name} — {self.price}"

class ProductList:
        def __init__(self, filename):
            self.filename = filename
            self.products = self.load_products()

        def load_products(self):
            """Загружает товары из файла."""
            products = []
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        name, price = line.strip().split(' — ')
                        products.append(Product(name, price))
            except FileNotFoundError:
                pass
            return products

        def save_products(self):
            """Сохраняет товары в файл."""
            with open(self.filename, 'w', encoding='utf-8') as file:
                for product in self.products:
                    file.write(f"{product.name} — {product.price}\n")

        def add_product(self, name, price):
            """Добавляет новый товар в список."""
            self.products.append(Product(name, price))
            self.save_products()

        def update_product(self, name, new_price):
            """Обновляет цену товара по имени."""
            for product in self.products:
                if product.name == name:
                    product.price = float(new_price)
                    self.save_products()
                    break

        def delete_product(self, name):
            """Удаляет товар по имени. """
            self.products = [product for product in self.products if product.name != name]
            self.save_products()

        def subtract_total(self):
            """Вычисляет общую сумму цен всех товаров."""
            return sum(product.price for product in self.products)

