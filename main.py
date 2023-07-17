from util.generate_docs import generate_docs
from argparse import ArgumentParser

OPTIONS = [("d", "docs", "create docs for the project")]

parser = ArgumentParser()

for flag, name, description in OPTIONS:
    parser.add_argument(
        f"-{flag}",
        f"--{name}",
        dest="options",
        action="append_const",
        const=name,
        help=description,
    )

if __name__ == "__main__":
    options = vars(parser.parse_args()).get("options")

    if options is None:
        options = [option for _, option, _ in OPTIONS]

    for option in options:
        match option:
            case "docs":
                print("Generating the docs...")
                generate_docs()
                print("Created a README.md file.")
            case _:
                raise ValueError(f"Invalid option: {option}.")
