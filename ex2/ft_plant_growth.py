class Plant:
    def __init__(self, name: str, height_cm: float, 
                 age_days: int, growth_rate: float) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self):
        print(
            f"{self.name}: {round(self.height_cm, 1)}cm, "
            f"{self.age_days} days old"
        )

    def grow(self):
        self.height_cm += self.growth_rate

    def age_one_day_older(self):
        self.age_days += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    rose.show()

    starting_height = rose.height_cm

    for day in range(1, 8):
        rose.grow()
        rose.age_one_day_older()
        print(f"=== Day {day} ===")
        rose.show()

    total_growth = rose.height_cm - starting_height
    print(f"Growth this week: {round(total_growth, 1)}cm")

if __name__ == "__main__":
    ft_plant_growth()
