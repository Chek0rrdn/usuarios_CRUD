from os import name
import click
from tabulate import tabulate

from users.services import UserService
from users.models import User


##COMANDOS BASICOS
@click.group()
def users():
    """    Administra el ciclo de vida de los Usuarios    """
    pass


@users.command()
@click.option(
    '-n', '--name',
    type=str,
    prompt = True,
    help='El nombre del Nuevo Usuario'
)
@click.option(
    '-c', '--company',
    type=str,
    prompt = True,
    help='La Compania del Nuevo Usuario'
)
@click.option(
    '-e', '--email',
    type=str,
    prompt = True,
    help='El email del Nuevo Usuario'
)
@click.option(
    '-p', '--position',
    type=str,
    prompt = True,
    help='La Posicion de cargo del Nuevo Usuario'
)
@click.pass_context
def create(ctx, name, company, email, position):
    """     Crea un Nuevo Usuario    """
    user = User(name, company, email, position)
    user_service = UserService(ctx.obj['users_table'])

    user_service.create_user(user)


@users.command()
@click.pass_context
def list(ctx):
    """    Lista todos usuarios    """
    user_service = UserService(ctx.obj['users_table'])
    users_list = user_service.list_users()

    click.echo(tabulate(users_list, headers='keys', tablefmt='fancy_grid'))


@users.command()
@click.argument('user_uid', type=str)
@click.pass_context
def update(ctx, user_uid):
    """    Actualiza un Usuario    """
    user_service = UserService(ctx.obj['users_table'])
    users_list = user_service.list_users()

    user = [user for user in users_list if user['uid'] == user_uid]

    if user:
        user = _update_client_flow(User(**user[0]))
        user_service.update_user(user)

        click.echo('Usuario Actualizado')
    else:
        click.echo('Usuario NO encontrado')


def _update_client_flow(user):
    click.echo('Deje vacio si usted no desea modificar el valor')

    user.name = click.prompt('Nuevo Nombre', type=str, default=user.name)
    user.company = click.prompt('Nueva Compania', type=str, default=user.company)
    user.email = click.prompt('Nuevo Email', type=str, default=user.email)
    user.position = click.prompt('Nueva Posicion', type=str, default=user.position)

    return user


@users.command()
@click.argument('user_uid', type=str)
@click.pass_context
def delete(ctx, user_uid):
    """    Elimina a un Usuario    """
    user_service = UserService(ctx.obj['users_table'])
    users_lists = user_service.list_users()

    user = [user for user in users_lists if user['uid'] == user_uid]

    if user:
        user_service.delete_user(user)

        click.echo('Usuario Eliminado')
    else:
        click.echo('Usuario NO encontrado')


all = users
