import click
from tabulate import tabulate

from clients.services import ClientService
from clients.models import Client

##COMANDOS BASICOS
@click.group()
def clients():
    """    Manages the Clients Lifecycle    """
    pass


@clients.command()
@click.option(
    '-n', '--name',
    type=str,
    prompt = True,
    help='El nombre del Nuevo Cliente'
)
@click.option(
    '-c', '--company',
    type=str,
    prompt = True,
    help='La Compania del Nuevo Cliente'
)
@click.option(
    '-e', '--email',
    type=str,
    prompt = True,
    help='El email del Nuevo Cliente'
)
@click.option(
    '-p', '--position',
    type=str,
    prompt = True,
    help='La Posicion de cargo del Nuevo Cliente'
)
@click.pass_context
def create(ctx, name, company, email, position):
    """     Creates a New Client    """
    cliente = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(cliente)


@clients.command()
@click.pass_context
def list(ctx):
    """    List all clients    """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    headers = [field.capitalize() for field in Client.schema()]
    table = []

    for client in clients_list:
        table.append([
            client['name'],
            client['company'],
            client['email'],
            client['position'],
            client['uid']
        ])
    
    click.echo(tabulate(table, headers=headers))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """    update a client    """
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """    deletes a client    """
    pass


all = clients
