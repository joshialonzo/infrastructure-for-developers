from dataclasses import dataclass


@dataclass
class NetworkDevice:
    name: str


@dataclass
class Server:
    name: str


class Laptop(NetworkDevice):
    pass


class EmailServer(Server):
    pass



def main():
    laptop_1 = Laptop(name="Laptop 1")
    assert isinstance(laptop_1, Laptop)
    assert isinstance(laptop_1, NetworkDevice)

    server_1 = EmailServer(name="Gmail")
    assert isinstance(server_1, Server)
    assert isinstance(server_1, EmailServer)


if __name__ == "__main__":
    main()
