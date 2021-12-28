import click

from users import commands as clients_commands


CLIENTS_TABLE = '.users.csv'

#PUNTO DE ENTRADA
@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['users_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)