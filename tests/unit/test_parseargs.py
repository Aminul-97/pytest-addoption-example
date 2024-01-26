from src.parseargs import parse_args


def test_parse_args():
    test_args = ["--config_file_path", "HERE", "--regtest-reset"]
    args = parse_args(test_args)
    assert args.config_file_path == "HERE"
    assert args.regtest_reset is True
