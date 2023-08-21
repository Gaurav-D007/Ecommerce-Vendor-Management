from abc import ABC, abstractmethod

class Products(ABC):


    @abstractmethod
    def add_product(self, product_name, product_type, available_quantity, unit_price):
        pass

    @abstractmethod
    def search_product_by_name(self, product_name):
        pass

    @abstractmethod
    def get_all_products(self):
        pass


