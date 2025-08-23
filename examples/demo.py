"""Simple demo script showing Agent Builder basics"""

from agent_builder import AgentBuilder
from rich.console import Console

def simple_demo():
    """Show the simplest way to use Agent Builder"""
    console = Console()
    
    console.print("\n[bold cyan]Agent Builder - Simple Demo[/bold cyan]")
    console.print("[dim]Generate professional AI agent prompts in minutes[/dim]\n")
    
    # Simple usage example
    console.print("[bold]Simple Usage:[/bold]")
    console.print("```python")
    console.print("from agent_builder import AgentBuilder")
    console.print("")
    console.print("# Create and run agent builder")
    console.print("builder = AgentBuilder()")
    console.print("builder.build()")
    console.print("")
    console.print("# Your professional prompt is ready!")
    console.print("print(builder.generate_prompt())")
    console.print("```\n")
    # Actually run the simple demo
    console.print("[bold]Live Demo:[/bold]")
    console.print("Creating a simple agent...\n")
    
    # Create a basic example programmatically
    builder = AgentBuilder(interactive=False)
    builder.components.update({
        "role": "helpful Python developer",
        "task": "review code for bugs and best practices",
        "constraints": ["Be constructive", "Focus on security"]
    })
    
    # Generate and show result
    prompt = builder.generate_prompt()
    console.print("[green]Generated prompt successfully![/green]")
    console.print(f"[dim]Length: {len(prompt)} characters[/dim]\n")
    
    # Show preview
    console.print("[bold]Prompt Preview:[/bold]")
    preview = prompt[:150] + "..." if len(prompt) > 150 else prompt
    console.print(f"[italic]{preview}[/italic]\n")
    
    console.print("[green]That's it! Your professional agent prompt is ready to use.[/green]")

if __name__ == "__main__":
    simple_demo()