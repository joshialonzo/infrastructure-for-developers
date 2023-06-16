from dataclasses import dataclass


@dataclass
class NetworkDevice:
    name: str


class Laptop(NetworkDevice):
    pass


def main():
    laptop_1 = Laptop(name="Laptop 1")
    assert isinstance(laptop_1, Laptop)
    assert isinstance(laptop_1, NetworkDevice)


if __name__ == "__main__":
    main()
