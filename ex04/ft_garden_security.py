class Plant:
    def __init__(self, name, height=0.0, age=0):
        self._name = name
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Using default height: 0.0cm")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Using default age: 0 days")
        else:
            self._age = age

        print(f"Plant created: {self}")


    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        print(f"Height updated: {round(self._height)}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"


def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-5)
    print()

    print(f"Current state: {rose}")


if __name__ == "__main__":
    main()
