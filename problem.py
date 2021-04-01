from typing import List

from sever import Server
from service import Service


class Problem:
    def __init__(self, input_cvs_path: str) -> None:
        self.servers: List[Server] = Server.create_servers("servers_catalog.csv")

        self.services: List[Service] = []

        with open(input_cvs_path, "r") as f:
            self.duree = int(f.readline())
            lines = f.readlines()
            for line in lines:
                line = line.split(",")
                self.services.append(Service(line[0], int(line[1]), int(line[2]), int(line[3])))


p = Problem("ctstfr0280_input_1.csv")