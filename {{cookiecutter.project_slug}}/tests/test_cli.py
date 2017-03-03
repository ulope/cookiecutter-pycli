from {{ cookiecutter.project_slug }}.cli import main
from {{ cookiecutter.project_slug }}.version import VERSION


def test_cli_main_version(cli_runner):
    result = cli_runner.invoke(main, ['--version'])

    assert result.exit_code == 0
    assert "version {}".format(VERSION) in result.output


def test_cli_cmd_a(cli_runner):
    result = cli_runner.invoke(main, ['a'])

    assert result.exit_code == 0
    assert result.output.strip() == "Here goes the code for the 'a' command"


def test_cli_cmd_b(cli_runner):
    result = cli_runner.invoke(main, ['b'])

    assert result.exit_code == 0
    assert result.output.strip() == "Here goes the code for the 'b' command"
