from typing import List
import copy
from itertools import repeat

from server import Server
from service import Service


class Problem:
    def __init__(self, input_cvs_path: str) -> None:
        self.servers: List[Server] = Server.create_servers("csv_files/servers_catalog.csv")

        self.services: List[Service] = []

        with open(input_cvs_path, "r") as f:
            self.duree = int(f.readline())
            lines = f.readlines()
            for line in lines:
                line = line.split(",")
                self.services.append(Service(line[0], int(line[1]), int(line[2]), int(line[3])))
        self.servers_used = []
        self.sort_servers()
        self.duplicate()


    def duplicate(self, dup = 100):
        self.servers = [copy.deepcopy(x) for item in self.servers for x in repeat(item, dup)]

    def solve(self):

        for service in self.services:

            for server in self.servers:
                if server.add_service(service):
                    if server not in self.servers_used:
                        self.servers_used.append(server)
                    break

    def sort_servers(self):
        self.servers.sort(key=lambda serv: serv.co2prod + self.duree * serv.co2use)

    def compute_score(self):
        score = 0
        for serv in self.servers_used:
            score += serv.co2prod + self.duree * serv.co2use
            # print(score)
        return score

    def __str__(self):
        ret = ''
        for server in self.servers_used:
            ret += server.model + ","
            for service_name in server.services_running:
                ret += service_name + ","
            ret = ret[:-1]
            ret += "\n"
        return ret

    def print_to_csv(self, filename):
        with open(filename, "w") as f:
            f.write(self.__str__())





p = Problem("csv_files/ctstfr0280_input_1.csv")
