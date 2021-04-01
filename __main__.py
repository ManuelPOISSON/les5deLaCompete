from problem import Problem


if __name__ == "__main__":
    p = Problem("csv_files/ctstfr0280_input_6.csv")
    # p.servers_used.append(p.servers[0])

    p.solve()
    # print("=======")
    # for server in p.servers_used:
    #     print(server.model)
    #     for s in server.services_running:
    #         print("\t", s)
    #
    # print(p.compute_score())
    # print(p)
    # for s in p.servers:
    #     print(s)
    p.print_to_csv("solution6.csv")
