from problem import Problem
import check_csv

if __name__ == "__main__":
    p = Problem("csv_files/ctstfr0280_input_6.csv")
    # p.servers_used.append(p.servers[0])

    p.solve()

    p.print_to_csv("solution6_1.csv")

    check_csv.check(p.services, "solution6_1.csv")
