import click

##COMANDOS BASICOS
@click.group()
def clients():
    """    Manages the Clients Lifecycle    """
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """    Creates a New Client    """
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """    List all clients    """
    pass


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
