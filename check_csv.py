from typing import List

from problem import Problem
from service import Service


def check(services: List[Service], csv_file):
    with open(csv_file, "r") as f:
        lines = f.read()
    # print("len", len(lines), lines)
    for service in services:
        if lines.count(service.name) < 1:
            print("miss", service.name)


l = "1,234, 23,34,25,44,663"
print(l.count("234"))
