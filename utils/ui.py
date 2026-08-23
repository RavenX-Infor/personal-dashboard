from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def titre(texte):
    console.print(
        Panel(
            Text(texte, justify="center", style="bold cyan"),
            border_style="cyan"
        )
    )


def menu_options(options, retour="Retour"):
    for cle, texte in options.items():
        console.print(f"[bold cyan][{cle}][/bold cyan] {texte}")

    console.print()
    console.print(f"[bold cyan][0][/bold cyan] {retour}")


def succes(message):
    console.print(f"[bold green]✓[/bold green] {message}")


def erreur(message):
    console.print(f"[bold red]✗[/bold red] {message}")


def avertissement(message):
    console.print(f"[bold yellow]⚠[/bold yellow] {message}")


def info(message):
    console.print(f"[bold blue]ℹ[/bold blue] {message}")


def pause(message="Appuyez sur Entrée pour continuer..."):
    console.input(f"\n[dim]{message}[/dim]")