import click

from {{ cookiecutter.project_slug }}.version import VERSION


@click.group(help="{{ cookiecutter.project_short_description }}")
@click.version_option(version=VERSION)
@click.pass_context
def main(ctx):
    ctx.obj = {}


@main.command(name="a", help="Command A")
@click.pass_obj
def command_a(obj):
    print("Here goes the code for the 'a' command")


@main.command(name="b", help="Command B")
@click.pass_obj
def command_b(obj):
    print("Here goes the code for the 'b' command")


def cli():
    main(auto_envvar_prefix="{{ cookiecutter.project_slug.upper() }}")


if __name__ == "__main__":
    cli()
