from __future__ import annotations
import click
from . import __version__, ping


@click.command()
@click.option("--version", is_flag=True, help="Show version and exit.")
def main(version: bool) -> None:
    if version:
        click.echo(__version__)
        raise SystemExit(0)
    click.echo(ping())
    raise SystemExit(0)


if __name__ == "__main__":
    main()
