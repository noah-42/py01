class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int, growth_rate: float) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height_cm, 1)}cm, {self.age_days} days old")

    def grow(self):
        self.height_cm += self.growth_rate

    def age_one_day_older(self):
        self.age_days += 1


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25.0, 30, 0.3),
        Plant("Oak", 200.0, 365, 0.1),
        Plant("Cactus", 5.0, 90, 0.1),
        Plant("Sunflower", 80.0, 45, 0.4),
        Plant("Fern", 15.0, 120, 0.4),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
