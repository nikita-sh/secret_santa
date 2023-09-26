import argparse, os
from MatchGenerator import MatchGenerator


def parse_exceptions(exception_path):
    exceptions = {}
    with open(exception_path, 'r') as f:
        for line in f:
            data = line.split(',')
            if len(data) != 2:
                raise Exception("malformed exceptions file")
            email1, email2 = data[0], data[1].strip()
            if email1 in exceptions:
                exceptions[email1].append(email2)
            else:
                exceptions[email1] = [email2]

            if email2 in exceptions:
                exceptions[email2].append(email1)
            else:
                exceptions[email2] = [email1]
    return exceptions


def parse_source_file(source_path):
    participants = []
    with open(source_path, 'r') as f:
        for line in f:
            data = line.split(',')
            if len(data) != 2:
               raise Exception("malformed input file")
            name, email = data[0], data[1].strip()
            participants.append({
                "name": name,
                "email": email
            })
    return participants


def main():
    # parse arguments
    parser = argparse.ArgumentParser(
        prog="Secret Santa",
        description="Assigns Secret Santa pairs given a list of emails"
    )
    parser.add_argument(
        "-s", "--source", 
        required=True, 
        help="Path to file containing emails to match.",
        type=os.path.abspath
    )
    parser.add_argument(
        "-e", "--exceptions", 
        required=False, 
        help="Path to file containing forbidden pairings.",
        type=os.path.abspath
    )
    args = parser.parse_args()

    # parse input file
    source_list = parse_source_file(args.source)
    name_map = {}
    emails = []
    for user in source_list:
        emails.append(user['email'])
        name_map[user['email']] = user['name']

    forbidden = {}
    if args.exceptions is not None:
        forbidden = parse_exceptions(args.exceptions)
    
    mg = MatchGenerator(source_list=emails, forbidden_pairs=forbidden)
    pairs = mg.generate_matches()

    for key, value in pairs.items():
        print(f'Notifying {key} that they are assigned to get a gift for {name_map[value]}')


if __name__ == "__main__":
    main()
