import click
from rich import print
from getpass import getpass
from strength import score_password
from breach import check_breach

@click.command(
    name="paz",
    help=(
    """
This CLI tool evaluates the strength of your password and checks whether it has been
found in any known data breaches using the Have I Been Pwned API.

Usage examples:

paz -p ""   # Direct password input

paz           # Prompts you to enter password securely
    """
    )
)
@click.option('--password', '-p', required=False, help='Password to analyze.If not provided, you will be prompted securely (hidden input).')
def analyze_password(password: str):
    flagp=0
    if not password:
        flagp=1
        password = getpass("🔑 Enter password (input hidden): ")

    strength, score = score_password(password)

    if strength == "Weak":
        color = "bold red"
    elif strength == "Medium":
        color = "bold yellow"
    else:
        color = "bold green"
    if flagp == 0:
        print(f"[bold cyan]🔍 Password:[/bold cyan] {password}")
    else:
        print("[bold cyan]🔍 Password: hidden input received[/bold cyan]")
    print(f"[{color}]💪 Strength: {strength} (score: {score})[/{color}]")

    breach_count = check_breach(password)
    if breach_count is None:
        print("[bold red]❌  Breach check failed (network error)[/bold red]")
    elif breach_count == 0:
        print("[bold green]✅ Password not found in known breaches[/bold green]")
    else:
        print(f"[bold red]🚨 Password found in {breach_count} data breaches![/bold red]")