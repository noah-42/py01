class Plant:
    def __init__(self, name: str, height=0.0, age=0):
        self.name = name
        self._height = 0.0
        self._age = 0
        self._stats = self._create_stats()
        if self._validate_non_negative(height, "height"):
            self._height = float(height)
        if self._validate_non_negative(age, "age"):
            self._age = age

    def _create_stats(self):
        return Plant.Stats()

    def _validate_non_negative(self, value, field_name):
        if value < 0:
            print(f"{self.name}: Error, {field_name} can't be negative")
            return False
        return True

    def get_name(self):
        return self.name

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
        self._stats.record_grow()

    def age(self, days=1):
        if not self._validate_non_negative(days, "days"):
            return
        self._age += days
        self._stats.record_age()

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.record_show()

    def show_stats(self):
        self._stats.display()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self):
            self._grow_count += 1

        def record_age(self):
            self._age_count += 1

        def record_show(self):
            self._show_count += 1

        def display(self):
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )


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
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_count = 0

        def record_shade(self):
            self._shade_count += 1

        def display(self):
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(self, name, height=0.0, age=0, trunk_diameter=0.0):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def _create_stats(self):
        return Tree.Stats()

    def produce_shade(self):
        print(
            f" Tree {self.name} now produces a shade of "
            f" {self._height}cm long and {self._trunk_diameter}cm wide."
        )
        self._stats.record_shade()

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height=0.0, age=0, harvest_season="unknown"):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self, days=1):
        super().age(days)
        if days > 0:
            self._nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    """A Flower that also tracks how many seeds it produces once it blooms."""

    def __init__(self, name, height=0.0, age=0, color="unknown", seeds=0):
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def bloom(self):
        super().bloom()
        self._seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant):
    """Statistics for plant:"""
    print(f"[statistics for {plant.get_name()}]")
    plant.show_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print(" [asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print(" [asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print(" [make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_statistics(anon)


if __name__ == "__main__":
    ft_garden_analytics()
