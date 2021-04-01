from service import Service

class Server:
    def __init__(self, model, co2prod, co2use, disk, ram, cores):
        self.model = model
        self.co2prod = int(co2prod)
        self.co2use = int(co2use)
        self.disk = int(disk)
        self.ram = int(ram)
        self.cores = int(cores)

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

    def compute_cost(self, duree_usage):
        return self.co2prod + duree_usage * self.co2use

    def add_service(self, service: Service) -> bool:
        """
        :param service:
        :return: false if service can't be added
        """
        if not self.ram >= service.ram and self.disk >= service.stockage and self.cores >= service.proc:
            return false
        else:
            self.ram -= service.ram
            self.disk -= service.stockage
            self.cores -= service.proc


