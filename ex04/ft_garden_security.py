class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int, growth_rate: float) -> None:
        self._name = name
        self._height_cm = height_cm
        self._age_days = age_days
        self._growth_rate = growth_rate

        if height_cm < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Using default height: 0.0cm")
        else:
            self._height_cm = float(height_cm)

        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Using default age: 0 days")
        else:
            self._age_days = age_days

        print(f"Plant created: {self}")

    def get_height(self):
        return self._height_cm

    def get_age(self):
        return self._age_days

    def set_height(self, height_cm):
        if height_cm < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height_cm = float(height_cm)
        print(f"Height updated: {round(self._height_cm)}cm")

    def set_age(self, age_days):
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days")

    def __str__(self):
        return f"{self._name}: {self._height_cm}cm, {self._age_days} days old"


def ft_plant_security():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.1)
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-5)
    print()

    print(f"Current state: {rose}")


if __name__ == "__main__":
    ft_plant_security()
