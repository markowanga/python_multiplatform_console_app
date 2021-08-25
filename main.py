import os

import click


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--count',  prompt='Number of greetings', help='Number of greetings.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(int(count)):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    hello()
