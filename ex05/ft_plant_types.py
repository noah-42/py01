class Plant:
    def __init__(self, name, height=0.0, age=0):
        self._name = name
        self._height = 0.0
        self._age = 0
        if self._validate_non_negative(height, "height"):
            self._height = float(height)
        if self._validate_non_negative(age, "age"):
            self._age = age

    def _validate_non_negative(self, value, field_name):
        if value < 0:
            print(f"{self._name}: Error, {field_name} can't be negative")
            return False
        return True


    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if not self._validate_non_negative(height, "height"):
            return
        self._height = float(height)

    def set_age(self, age):
        if not self._validate_non_negative(age, "age"):
            return
        self._age = age

    def grow(self, amount=1.0):
        if not self._validate_non_negative(amount, "growth amount"):
            return
        self._height += amount

    def age(self, days=1):
        if not self._validate_non_negative(days, "days"):
            return
        self._age += days

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height=0.0, age=0, color="unknown"):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height=0.0, age=0, trunk_diameter=0.0):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self._name} now produces a shade of "
            f" {self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height=0.0, age=0, harvest_season="unknown"):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount=1.0):
        super().grow(amount)

    def age(self, days=1):
        super().age(days)
        if days > 0:
            self._nutritional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
