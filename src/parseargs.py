from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def parse_args(args=None):
    argument_parser = ArgumentParser(
        description="Command line arguments for reading a configuration file",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    argument_parser.add_argument(
        "--config_file_path", type=str, help="Configuration file path"
    )
    argument_parser.add_argument(
        "--regtest-reset",
        action="store_true",
        help="do not run regtest but record current output",
    )
    return argument_parser.parse_args(args)
