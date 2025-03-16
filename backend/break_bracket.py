import csv


def read_prelims(filename):
    results_dict = dict()
    prelim_population_dict = dict()

    with open(filename, "r") as prelims_file:
        csvreader = csv.reader(prelims_file)
        header = next(csvreader)

        for row in csvreader:
            record = int(row[0])
            code = row[2]
            results_dict[code] = record

            if record not in prelim_population_dict:
                prelim_population_dict[record] = 0
            prelim_population_dict[record] += 1

    return results_dict, prelim_population_dict


def read_byes(byes_list, max_prelims, results_dict, prelim_population_dict):
    seeding = []
    people_read = set()
    curr_seed = 0
    curr_prelim = max_prelims
    num_in_current_prelim = 0

    while len(people_read) < len(byes_list):
        for debater in byes_list:
            debater_result = results_dict[debater]
            if debater_result == curr_prelim and debater not in people_read:
                people_read.add(debater)
                seeding.append(debater)
                curr_seed += 1
                num_in_current_prelim += 1
            if num_in_current_prelim >= prelim_population_dict[curr_prelim]:
                curr_prelim -= 1
                num_in_current_prelim = 0
    return seeding


def read_results(results):
    byes_list = []
    debated_list = []
    with open(results, "r") as results_file:
        csvreader = csv.reader(results_file)
        header = next(csvreader)

        for row in csvreader:
            if row[1] == "":
                byes_list.append(row[0])
            else:
                debated_list.append((row[0], row[1]))
    return byes_list, debated_list


def bracketfy(seeding1, seeding2):
    seednum = 1
    for debater in seeding1:
        print(f"{seednum}: {debater}")
        seednum += 1
    for pair in seeding2:
        print(f"{seednum}: {pair}")
        seednum += 1


if __name__ == "__main__":
    results_dict, prelim_population_dict = read_prelims("PrelimRecords.csv")
    byes_list, debated_list = read_results("Results.csv")
    byes_seed = read_byes(byes_list, 6, results_dict, prelim_population_dict)

    bracketfy(byes_seed, debated_list)
