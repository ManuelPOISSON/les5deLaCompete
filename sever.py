


class Server:
    def __init__(self, model, co2prod, co2use, disk, ram, cores):
        self.model = model
        self.co2prod = co2prod
        self.co2se = co2use
        self.disk = disk
        self.ram = ram
        self.cores = cores

    def __str__(self) -> str:
        return super().__str__()

    @staticmethod
    def create_servers(servers_catalog_path: str):
        servers_list = []
        with open(servers_catalog_path, "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                content = line.split(",")
                servers_list.append(Server(content[0], content[1], content[2], content[3], content[4], content[5]))

        return servers_list


print(Server.create_servers("servers_catalog.csv"))

