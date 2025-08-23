#!/usr/bin/env python3
"""
CLI entry point for Agent Builder
"""

from .agent_builder import AgentBuilder, interactive_mode_selection
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
import time

def main():
    """Main CLI entry point for Agent Builder"""
    console = Console()
    
    try:
        # Select mode with enhanced UI
        mode = interactive_mode_selection()
        
        # Create builder
        builder = AgentBuilder(mode=mode)
        
        # Build prompt with progress tracking
        with console.status("[bold green]Initializing Agent Builder...") as status:
            time.sleep(1)  # Brief loading animation
        
        builder.build()
        
        # Display summary with better visuals
        builder.display_summary()
        
        # Clean save dialog
        save_panel = Panel(
            "[bold blue]Save Your Prompt[/bold blue]\n\n"
            "[dim]Would you like to save this prompt to a file for future use?\n"
            "This will create a JSON file with your prompt and performance metrics.[/dim]",
            title="Save Options",
            border_style="blue"
        )
        console.print(save_panel)
        
        if Confirm.ask("[bold blue]Save this prompt to file?[/bold blue]", console=console):
            with console.status("[bold blue]Saving prompt..."):
                filepath = builder.save()
                time.sleep(0.5)  # Brief animation
            console.print(Panel(
                f"[bold green]Success![/bold green]\n\nPrompt saved to: [cyan]{filepath}[/cyan]",
                title="Saved",
                border_style="green"
            ))
        
        # Clean feedback section
        feedback_panel = Panel(
            "[bold magenta]Rate Your Experience[/bold magenta]\n\n"
            "[dim]Your feedback helps us improve the Agent Builder experience![/dim]",
            title="Feedback",
            border_style="magenta"
        )
        console.print(feedback_panel)
        
        if Confirm.ask("[bold magenta]Would you like to rate this experience?[/bold magenta]", console=console):
            rating = Prompt.ask(
                "[bold magenta]Rate your satisfaction (1-10)[/bold magenta]", 
                default="8",
                console=console
            )
            try:
                rating_num = float(rating)
                builder.metrics.user_satisfaction = rating_num
                
                # Visual feedback based on rating
                if rating_num >= 8:
                    console.print(Panel(
                        "[bold green]Thank you for the great rating![/bold green]\n"
                        "[dim]We're glad you had a positive experience with Agent Builder![/dim]",
                        title="Excellent!",
                        border_style="green"
                    ))
                elif rating_num >= 6:
                    console.print(Panel(
                        "[bold yellow]Thanks for your feedback![/bold yellow]\n"
                        "[dim]We're always working to improve the experience![/dim]",
                        title="Good!",
                        border_style="yellow"
                    ))
                else:
                    console.print(Panel(
                        "[bold red]Thank you for the honest feedback![/bold red]\n"
                        "[dim]We'll use this to make Agent Builder better![/dim]",
                        title="Feedback Received",
                        border_style="red"
                    ))
            except ValueError:
                console.print("[yellow]Invalid rating, but thanks anyway![/yellow]")
        
        # Final goodbye message
        console.print(Panel(
            "[bold cyan]Thank you for using Agent Builder![/bold cyan]\n\n"
            "[dim]Visit us at github.com/The-Swarm-Corporation/agents-builder.md for more tools and updates![/dim]",
            title="Goodbye!",
            border_style="cyan"
        ))
    
    except KeyboardInterrupt:
        console.print(Panel(
            "[bold yellow]Process cancelled by user[/bold yellow]\n\n"
            "[dim]No worries! Come back anytime to build amazing AI agents![/dim]",
            title="Until next time!",
            border_style="yellow"
        ))
    except Exception as e:
        console.print(Panel(
            f"[bold red]An error occurred:[/bold red]\n\n[dim]{e}[/dim]",
            title="Error",
            border_style="red"
        ))
        raise

if __name__ == "__main__":
    main()