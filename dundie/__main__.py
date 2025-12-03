import argparse


def load(filepath_):
    """Load data from filepath to the database"""
    try:
        with open(filepath_) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f'File not found {e}')


def main():

    parser = argparse.ArgumentParser(
    description="Dunder Mifflin Rewards",
    epilog="Enjoy and use with cautious.",
)
    parser.add_argument(
        "subcommand",
        type=str,
        help='The subcommand to execute.',
        choices=['load', 'show', 'send'],
        default="help"
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
    )

    args = parser.parse_args()
    globals()[args.subcommand](args.filepath)

    



if __name__ == "__main":
    main()