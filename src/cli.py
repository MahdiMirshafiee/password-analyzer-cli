import click
from rich import print
from strength import score_password

@click.command()
@click.option('--password', '-p', required=True, help='Password to analyze')
def analyze_password(password: str):
    """
    Analyze a given password (placeholder).
    """
    strength, score = score_password(password)

    if strength == "Weak":
        color = "bold red"
    elif strength == "Medium":
        color = "bold yellow"
    else:
        color = "bold green"

    print(f"[bold cyan]🔍 Password:[/bold cyan] {password}")
    print(f"[{color}]💪 Strength: {strength} (score: {score})[/{color}]")