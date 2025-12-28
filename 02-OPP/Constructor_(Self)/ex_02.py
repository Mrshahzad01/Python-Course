# Example 02

class Laptop:
    def __init__(self, brand, model, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage

laptop_01 = Laptop("Dell", "XPS 13", "Intel i7", "16GB", "512GB SSD")
laptop_02 = Laptop("Apple", "MacBook Pro", "M1", "16GB", "1TB SSD")
print("Laptop_01 Details:")
print("Brand:", laptop_01.brand),
print("Model:", laptop_01.model),
print("Processor:", laptop_01.processor),
print("RAM:", laptop_01.ram),
print("Storage:", laptop_01.storage)
print("\nLaptop_02 Details:")
print("Brand:", laptop_02.brand),
print("Model:", laptop_02.model),
print("Processor:", laptop_02.processor),
print("RAM:", laptop_02.ram),
print("Storage:", laptop_02.storage)