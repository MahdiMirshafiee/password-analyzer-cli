import click
from rich import print
from getpass import getpass
from strength import score_password
from breach import check_breach

@click.command()
@click.option('--password', '-p', required=False, help='Password to analyze')
def analyze_password(password: str):
    if not password:
        password = getpass("🔑 Enter password (input hidden): ")

    strength, score = score_password(password)

    if strength == "Weak":
        color = "bold red"
    elif strength == "Medium":
        color = "bold yellow"
    else:
        color = "bold green"

    print(f"[bold cyan]🔍 Password:[/bold cyan] {password}")
    print(f"[{color}]💪 Strength: {strength} (score: {score})[/{color}]")

    breach_count = check_breach(password)
    if breach_count is None:
        print("[bold red]❌  Breach check failed (network error)[/bold red]")
    elif breach_count == 0:
        print("[bold green]✅ Password not found in known breaches[/bold green]")
    else:
        print(f"[bold red]🚨 Password found in {breach_count} data breaches![/bold red]")