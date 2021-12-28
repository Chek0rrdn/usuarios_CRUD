import click

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

    click.echo('\tID\t|\tNAME\t|\tCOMPANY\t|\tEMAIL\t|\tPOSITION')
    click.echo('*'*90)
    for client in clients_list:
        click.echo('{uid}|{name}|{company}|{email}|{position}'.format(
            uid = client['uid'],
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


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
