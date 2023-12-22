import csv
import sys
from typing import List, Dict

def main():
    # TODO: Check for command-line usage
    if len(sys.argv) <3:
        sys.exit("Error: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    filename = sys.argv[1]
    with open(filename) as dna_DataBase:
        reader = csv.DictReader(dna_DataBase)

        table: List[Dict[str, str]] = []

        for row in reader:
            dna_patterns: Dict[str, str] = {}

            for column in row:
                dna_patterns[column] = str(row[column])
            table.append(dna_patterns)



    # TODO: Read DNA sequence file into a variable
    filename_2 = sys.argv[2]
    with open(filename_2) as dna_Sequence:
        DNA = csv.reader(dna_Sequence)
        dna = ','.join(str(d) for d in DNA)


    # TODO: Find longest match of each STR in DNA sequence
    profile = {}
    question_acces = table[0]
    x = list(question_acces.keys())
    y = int(len(x))
    for i in range(y):
        STRs = longest_match(dna, str(x[i]))
        STRs = str(STRs)
        profile.update({str(x[i]) : STRs})


    match_person = list(profile.values()) #list of possible matching STRs

    # TODO: Check database for matching profiles
    num_tot_ite = int(len(table))

    for i in range(num_tot_ite):
        database_list = list(table[i].values())
        if match_person[1:] == database_list[1:]:
            print(database_list[0])
            bol = 0
            break
        else:
            bol = 1
            continue

    if bol == 1:
        print("No match")






    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def dict_filter(it, *keys):
    for d in it:
        yield dict((k, d[k]) for k in keys)


main()




