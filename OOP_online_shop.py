# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Список требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# 2) Добавить товар на склад
# 3) Удалить товар со склада
# 4) Распечатать остаток товара по его имени
# 5) Распечатать остаток всех товаров
# 6) Товар может принадлежать к категории
# 7) Распечатать список товаров с заданной категорией

# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой

# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.

# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС


class Item:
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.availability = False

    @property
    def quantity(self):
        """Calculate quantity from all warehouses"""
        return


class Warehouse:
    warehouse_count = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.warehouse = []
        self.availability = False
        self.warehouse_count += 1

    def add_item(self, item: Item, quantity=1):
        """Add item to warehouse with quantity"""
        for elem in range(quantity):
            self.warehouse.append(item)

    def remove_item(self, item: Item):
        """Remove item from warehouse"""

    def get_quantity_by_item_name(self, item_name):
        """Get quantity by Item name"""

    def get_quantity_item(self):
        """Get quantity Item"""

    def get_items_by_category(self, category_name):
        """Get items list by category name"""


class Cart:
    def __init__(self):
        self.id = self._get_cart_id()
        self.cart = {'id': list()}

    @property
    def total_price(self):
        """Calculated field for all items in cart"""
        total_price = 0
        for cart_id, items in self.cart.items():
            # calculate price for each item
            for item in items:
                total_price += item.price
        return total_price

    @staticmethod
    def _get_cart_id():
        """Generate id for cart"""
        return hash(1)

    def add_item(self, item: Item, quantity=1):
        """Add item to cart with quantity"""

    def remove_item(self, item: Item, quantity=1):
        """Remove item to cart with quantity"""

    def __str__(self):
        return f"Item: {self}Total price: {self.total_price}"


class Order:
    def __init__(self, cart: Cart, warehouse: Warehouse):
        self.cart = cart
        self.id = self._generate_id()
        self.priority = ('Low', 'Medium', 'High')
        self.warehouse = warehouse
        self.date_purchased = self._current_date_time()
        self._order_processed()

    @staticmethod
    def _generate_id():
        """Generate order id during initialization"""
        return 100

    @staticmethod
    def _current_date_time():
        """Generate timestamp for order during innitialization"""
        return

    def _order_processed(self):
        """Precessed flow for create order"""
        for items in self.cart.cart.values():
            for item in items:
                self.warehouse.remove_item(item)

    def __str__(self):
        return f'Id: {self.id}, Cart: {self.cart.cart}'


item = Item(
    name='Iphone',
    description='BlaBla desscription',
    price=100,
    category='Phones'
)

warehouse1 = Warehouse(name='warehouse1', location='Kiev')
warehouse1.add_item(item=item, quantity=100)

warehouse2 = Warehouse(name='warehouse2', location='Kiev')
warehouse2.add_item(item=item, quantity=100)

cart1 = Cart()
cart1.add_item(item=item, quantity=2)
print(cart1)

order = Order(cart=cart1, warehouse=warehouse1)
