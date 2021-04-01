from problem import Problem


if __name__ == "__main__":
    p = Problem("csv_files/ctstfr0280_input_1.csv")
    # p.servers_used.append(p.servers[0])
    # for serv in p.servers:
    #     print(serv.compute_cost(2))
    # print("====")
    # p.sort_servers()
    # for serv in p.servers:
    #     print(serv.model, serv.compute_cost(2))
    p.solve()
    print("=======")
    for server in p.servers_used:
        print(server.model)
        for s in server.services_running:
            print("\t", s)

    print(p.compute_score())
    p.print_to_csv("file.csv")
