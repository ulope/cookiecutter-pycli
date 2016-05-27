import click

@click.group()
@click.pass_context
def main(ctx):
    print("Here goes your code")
    ctx.obj = {}


@main.command(name="sub", help="A subcommand")
@click.pass_obj
def sub(obj):
    print("Here goes the code for the 'sub' command")


def cli():
    main(auto_envvar_prefix="{{ cookiecutter.project_slug.upper() }}")


if __name__ == "__main__":
    cli()
