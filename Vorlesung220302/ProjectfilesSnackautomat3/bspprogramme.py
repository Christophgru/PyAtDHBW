# Gründe für Klassen: Kapselung, Sicherheit
# Vererbung: Ähnliche Eigenschaften kapseln


class Product:
    def __init__(self, name="name"):
        print("Create new Product: ", name)
        if name == "test":
            raise NotImplementedError
        self.name = name
        self.__amount = 0  # alles mit zwei unterstrichen wird von python durch Klassennamen ersetzt
        self._privateamount = 0

    def print_name(self):
        print(self.name)
        print(self.__dict__)


class Product2(Product):
    static_attribute_xy = 5

    def __init__(self, name: str, amount: int):
        # super(Product, self).__init__(name)
        self.name = name
        self.__amount = amount


# Python ist eine script language

mars = Product("Mars")
print(mars.name)
cola = Product2("Cola", 5)
print(cola.name)
print(mars._Product__amount)

x = 5
y = 6
print(f"Produkt: {x} kostet{y}€")
