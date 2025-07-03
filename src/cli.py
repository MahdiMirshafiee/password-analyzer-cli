import click

@click.command()
@click.option('--password', '-p', required=True, help='Password to analyze')
def analyze_password(password: str):
    """
    Analyze a given password (placeholder).
    """
    click.secho(f"🔍 Password entered: {password}", fg="cyan")