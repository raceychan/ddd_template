import typing as ty
from argparse import ArgumentParser, Namespace


class Options(ty.TypedDict, total=False):
    option1: str
    option2: bool


def cli(options: ty.Annotated[Namespace, Options]):
    if options.option1:
        print("im a foo")

    if options.option2:
        print("im a bar")


def main():
    parser = ArgumentParser()
    parser.add_argument('--option1', type=str)
    parser.add_argument('--option2', action='store_true')
    options = parser.parse_args()

    cli(options=options)


if __name__ == "__main__":
    main()
