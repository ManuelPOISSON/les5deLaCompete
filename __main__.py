from problem import Problem


if __name__ == "__main__":
    p = Problem("csv_files/ctstfr0280_input_1.csv")
    p.servers_used.append(p.servers[0])
    print(p.compute_score())