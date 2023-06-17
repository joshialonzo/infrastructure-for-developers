from dataclasses import dataclass


@dataclass
class NetworkDevice:
    name: str


@dataclass
class Server:
    name: str


@dataclass
class Connection:
    name: str


@dataclass
class Cable:
    name: str


class Laptop(NetworkDevice):
    pass


class EmailServer(Server):
    pass


@dataclass
class Wired(Connection):
    cable: Cable


def main():
    laptop_1 = Laptop(name="Laptop 1")
    assert isinstance(laptop_1, Laptop)
    assert isinstance(laptop_1, NetworkDevice)

    server_1 = EmailServer(name="Gmail")
    assert isinstance(server_1, Server)
    assert isinstance(server_1, EmailServer)

    ethernet_cable = Cable(name="Ethernet")
    wired_connection = Wired(
        name="Wired Connection",
        cable=ethernet_cable,
    )
    assert isinstance(ethernet_cable, Cable)
    assert isinstance(wired_connection, Connection)
    assert isinstance(wired_connection, Wired)


if __name__ == "__main__":
    main()
