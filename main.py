import os

import click


@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--count', help='Number of greetings.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    os.environ["DEBUSSY"] = "1"
    hello()
