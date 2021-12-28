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
    """     Crea un Nuevo Cliente    """
    cliente = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(cliente)


@clients.command()
@click.pass_context
def list(ctx):
    """    Lista todos clientes    """
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
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """    Actualiza un cliente    """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    client = [client for client in clients_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Cliente Actualizado')
    else:
        click.echo('Cliente no Encontrado')


def _update_client_flow(client):
    click.echo('Deje vacio si usted no desea modificar el valor')

    client.name = click.prompt('Nuevo Nombre', type=str, default=client.name)
    client.company = click.prompt('Nueva Compania', type=str, default=client.company)
    client.email = click.prompt('Nuevo Email', type=str, default=client.email)
    client.position = click.prompt('Nueva Posicion', type=str, default=client.position)

    return client


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """    deletes a client    """
    pass


all = clients
