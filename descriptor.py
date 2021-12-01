import datetime
from email_validator import validate_email, EmailNotValidError
import re


# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить


class EmailDescriptor:
    """A simple example of a descriptor.
    The check is extremely imperfect, but the very principle of operation of the descriptor is shown."""

    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        try:
            valid = validate_email(value)
            instance._email = valid.email
            print(f'Email: {value} - is valid')
        except EmailNotValidError as e:
            print(str(e))
        # index = value.find('@')
        # if index != -1:
        #     if value.endswith('gmail.com', index):
        #         instance._email = value
        #     else:
        #         raise ValueError
        # else:
        #     raise ValueError


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()


# my_class.email = "validemail@gmail.com"
# my_class.email = "novalidemail@dsfsd"
# print(my_class.email)
# Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    """I read the article and took an example from here:
     https://webdevblog.ru/realizaciya-shablona-singleton-v-python/"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        # your code here
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


# c = MyClass()
# b = MyClass()
# assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:
    """This solution has already been implemented in the lecture:
    https://docs.google.com/presentation/d/1BKTXac09H5QJB7ihOMSkrpQS8gS906EoBy7pQRNOzJU/edit#slide=id.p20"""

    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return instance.__dict__[self.label]


class Data:
    number = IngegerField('first')


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

# assert data_row.number != new_data_row.number


# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
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


class Price:

    def __get__(self, instance, owner):
        return instance._price * 1.2

    def __set__(self, instance, value):
        instance._price = value


class Product:
    """class product, takes values for initialization."""

    storage = {}
    price = Price()

    def __init__(self, name, description, quantity, availability, _price, category):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.availability = availability
        self.price = _price
        self.category = category



    # def product_info(self):   #used to display product properties
    #     print(f'Product name: {self.name}; Product description: {self.description}; Product quantity: {self.quantity};'
    #           f'Product availability: {self.availability}; Product price: {self.price}; Product category: {self.category}')

    def __str__(self):
        return f'Product name: {self.name}; Product description: {self.description}; Product quantity: {self.quantity}; Product availability: {self.availability}; Product price: {self.price}; Product category: {self.category}'


class Storage:
    """Storage class. Takes a product and creates a dictionary with the required key: value.
Methods:add_to_store - adding to storage
;del_from_store - deletion from storage;one_balance - balance of 1 product;
all_balance - balance of all products;get_prod_category - balance of all products by category"""

    def __init__(self):
        self.store = {}

    def add_to_store(self, product):
        self.store[product.name] = {}
        self.store[product.name]['description'] = product.description
        self.store[product.name]['quantity'] = product.quantity
        self.store[product.name]['availability'] = product.availability
        self.store[product.name]['price'] = product.price
        self.store[product.name]['category'] = product.category
        return self.store

    def del_from_store(self, product):
        del self.store[product.name]

    def one_balance(self, product):
        if not product.name in self.store:
            print('This item is out of stock.')
        else:
            print(f'Balance of {product.name} on storage: {self.store[product.name]["availability"]}')

    def all_balance(self):
        all_prod = {}
        for prod in self.store:
            for qa in self.store[prod]:
                if qa == 'quantity':
                    all_prod[prod] = self.store[prod][qa]
        print(f'The rest of all goods: {all_prod}')

    def get_prod_category(self, category):
        category_list = []
        for prod in self.store:
            for cate in self.store[prod]:
                if cate == 'category' and self.store[prod][cate] == category:
                    category_list.append(prod)
        print(f'List products by category "{category}": {category_list}')


class ShoppingBasket:
    """class Basket. Accepts product, storage and quantity of product required.
    is a nested dictionary, where the first key is the order number, whose value is a dictionary
    After adding, the quantity of available product changes in the storage.
    Method:add_to_basket - adds order;; get_track_your_order - detailed information on the order.
    """

    def __init__(self, product, need, storage):
        self.basket = {}
        self.order_id = 1
        if need <= product.availability:
            self.basket[self.order_id] = {}
            self.basket[self.order_id]['name'] = product.name
            self.basket[self.order_id]['need'] = need
            self.basket[self.order_id]['total_price_with_NDS'] = product.price * need
            print(f'Your order number: {self.order_id}')
            self.order_id += 1
            self.date_purchased = datetime.datetime.now()
            # self.date_purchased = self.date_purchased.strftime("%d-%m-%Y %H:%M")
            self.change_count = storage.store[product.name]['availability'] - need
            storage.store[product.name]['availability'] = self.change_count
        else:
            print('The required quantity of goods is not in stock.')

    def add_to_basket(self, order_id, product, need, storage):
        if need <= product.availability:
            if self.basket[order_id]['name'] == product.name:
                self.basket[order_id]['need'] += need
                self.basket[order_id]['total_price_with_NDS'] = self.basket[order_id]['need'] * product.price
            else:
                self.basket[self.order_id] = {}
                self.basket[self.order_id]['name'] = product.name
                self.basket[self.order_id]['need'] = need
                self.basket[self.order_id]['total_price_with_NDS'] = product.price * need
                print(f'Your order number: {self.order_id}')
                self.order_id += 1
                self.date_purchased = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                self.change_count = storage.store[product.name]['availability'] - need
                storage.store[product.name]['availability'] = self.change_count
        else:
            print('The required quantity of goods is not in stock.')

    def get_track_your_order(self, order_id):
        if order_id == self.order_id:
            print('There is no such order.')
        else:
            print(f'Order number - #{order_id}. Order date: {self.date_purchased}. Detailed ordering information: {self.basket[order_id]}')

# product_banana = Product('Banana', 'Yummy', 10, 10, 20, 'fruit')
# print(product_banana)
# product_banana.product_info()
# product_apple = Product('Apple', 'Yummy', 20, 20, 5, 'fruit')
# product_potato = Product('Potato', 'Best food', 35, 35, 15, 'vegetable')

# storage1 = Storage()
# storage1.add_to_store(product_banana)
# storage1.add_to_store(product_apple)
# storage1.add_to_store(product_potato)
# storage1.one_balance(product_banana)
# storage1.all_balance()
# storage1.get_prod_category('fruit')
#
# shopping_basket = ShoppingBasket(product_banana, 2, storage1)
# shopping_basket.add_to_basket(1, product_apple, 2, storage1)
# shopping_basket.get_track_your_order(1)
# shopping_basket.get_track_your_order(2)
# storage1.one_balance(product_banana)
# storage1.one_balance(product_apple)