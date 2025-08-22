"""
Simple AGENTS.md Builder - Create AI agent instructions in minutes
"""

import json
import os
from typing import Dict, List, Optional, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown
from rich.table import Table
from rich.syntax import Syntax
from pathlib import Path

console = Console()

# ============= SIMPLE 5-PART STRUCTURE =============

class SimpleAgent:
    """Simple 5-part agent structure"""
    
    EXAMPLES = {
        "WHO": {
            "Coding": "Senior Python developer with API expertise",
            "Writing": "Technical writer specializing in documentation",
            "Analysis": "Data analyst focused on business insights",
            "Testing": "QA engineer with automation experience"
        },
        "WHAT": {
            "main_task": {
                "Coding": "Write clean, efficient Python code",
                "Writing": "Create clear technical documentation",
                "Analysis": "Analyze data and provide insights",
                "Testing": "Test code and find bugs"
            },
            "can_do": [
                "Write new features",
                "Debug existing code", 
                "Create documentation",
                "Review code quality",
                "Suggest improvements"
            ],
            "cannot_do": [
                "Modify core architecture without approval",
                "Access production databases directly",
                "Make breaking changes"
            ]
        },
        "HOW": {
            "styles": ["Professional", "Casual", "Technical", "Educational"],
            "approaches": ["Fast", "Careful", "Creative", "By-the-book"]
        },
        "OUTPUT": {
            "formats": ["Text", "Code", "List", "Report", "JSON", "Markdown"],
            "examples": {
                "Code": "```python\ndef example():\n    return 'clean code'\n```",
                "List": "✅ Task completed\n⚠️ Warning found\n❌ Error detected",
                "Report": "## Summary\n- Finding 1\n- Finding 2\n## Details...",
            }
        },
        "TEST": {
            "prompts": {
                "Coding": "Write a function to calculate fibonacci",
                "Writing": "Document this function: def add(a,b): return a+b",
                "Analysis": "Analyze this data: [1,2,3,4,5]",
                "Testing": "Test this code: print('hello')"
            },
            "success": {
                "Coding": "Function handles edge cases and has docstring",
                "Writing": "Includes parameters, return value, and example",
                "Analysis": "Shows mean, median, and trend",
                "Testing": "Mentions no errors but suggests improvements"
            }
        }
    }
    
    def __init__(self):
        self.data = {
            "WHO": {"role": ""},
            "WHAT": {"main_task": "", "can_do": [], "cannot_do": []},
            "HOW": {"style": "", "approach": ""},
            "OUTPUT": {"format": "", "example": ""},
            "TEST": {"prompt": "", "success": ""}
        }
        
    def collect_input(self, step: str) -> None:
        """Collect input for a specific step with examples"""
        
        console.print(f"\n[bold cyan]Step {step}[/bold cyan]")
        
        if step == "1":
            self._collect_who()
        elif step == "2":
            self._collect_what()
        elif step == "3":
            self._collect_how()
        elif step == "4":
            self._collect_output()
        elif step == "5":
            self._collect_test()
            
    def _collect_who(self):
        """WHO - Agent Identity"""
        console.print("\n[bold]WHO is this agent?[/bold]")
        console.print("[dim]Define the agent's role and expertise[/dim]")
        
        # Show examples
        console.print("\n[yellow]Examples:[/yellow]")
        for type, example in self.EXAMPLES["WHO"].items():
            console.print(f"  • {type}: {example}")
            
        self.data["WHO"]["role"] = Prompt.ask(
            "\n[bold green]Enter agent role[/bold green]",
            default="Python developer"
        )
        
    def _collect_what(self):
        """WHAT - Agent Job"""
        console.print("\n[bold]WHAT does this agent do?[/bold]")
        
        # Main task
        console.print("\n[yellow]Example main tasks:[/yellow]")
        for type, task in self.EXAMPLES["WHAT"]["main_task"].items():
            console.print(f"  • {type}: {task}")
            
        self.data["WHAT"]["main_task"] = Prompt.ask(
            "\n[bold green]Main task[/bold green]",
            default="Write and review code"
        )
        
        # Can do
        console.print("\n[yellow]What CAN this agent do? (3-5 items)[/yellow]")
        console.print("[dim]Examples: Write code, Debug, Test, Document, Review[/dim]")
        
        for i in range(3):
            item = Prompt.ask(f"  Can do #{i+1}")
            if item:
                self.data["WHAT"]["can_do"].append(item)
                
        # Cannot do (optional)
        if Confirm.ask("\n[yellow]Add restrictions?[/yellow]", default=False):
            console.print("[dim]Examples: Cannot access production, Cannot delete data[/dim]")
            for i in range(2):
                item = Prompt.ask(f"  Cannot do #{i+1}", default="")
                if item:
                    self.data["WHAT"]["cannot_do"].append(item)
                    
    def _collect_how(self):
        """HOW - Working Style"""
        console.print("\n[bold]HOW should the agent work?[/bold]")
        
        # Style
        styles = self.EXAMPLES["HOW"]["styles"]
        console.print("\n[yellow]Communication style:[/yellow]")
        for i, style in enumerate(styles, 1):
            console.print(f"  {i}. {style}")
            
        choice = Prompt.ask("Choose style", choices=["1","2","3","4"], default="3")
        self.data["HOW"]["style"] = styles[int(choice)-1]
        
        # Approach
        approaches = self.EXAMPLES["HOW"]["approaches"]
        console.print("\n[yellow]Work approach:[/yellow]")
        for i, approach in enumerate(approaches, 1):
            console.print(f"  {i}. {approach}")
            
        choice = Prompt.ask("Choose approach", choices=["1","2","3","4"], default="2")
        self.data["HOW"]["approach"] = approaches[int(choice)-1]
        
    def _collect_output(self):
        """OUTPUT - Result Format"""
        console.print("\n[bold]OUTPUT format?[/bold]")
        
        formats = self.EXAMPLES["OUTPUT"]["formats"]
        console.print("\n[yellow]Output formats:[/yellow]")
        for i, fmt in enumerate(formats, 1):
            console.print(f"  {i}. {fmt}")
            
        choice = Prompt.ask("Choose format", choices=[str(i) for i in range(1,7)], default="2")
        selected_format = formats[int(choice)-1]
        self.data["OUTPUT"]["format"] = selected_format
        
        # Show example for selected format
        if selected_format in self.EXAMPLES["OUTPUT"]["examples"]:
            console.print(f"\n[dim]Example {selected_format} output:[/dim]")
            console.print(Panel(self.EXAMPLES["OUTPUT"]["examples"][selected_format]))
            
        # Custom example
        console.print("\n[yellow]Provide a short example of desired output:[/yellow]")
        self.data["OUTPUT"]["example"] = Prompt.ask("Example", default="Clear and concise output")
        
    def _collect_test(self):
        """TEST - Validation"""
        console.print("\n[bold]TEST your agent[/bold]")
        console.print("[dim]Provide a test to validate the agent works correctly[/dim]")
        
        # Show test examples
        console.print("\n[yellow]Example test prompts:[/yellow]")
        for type, prompt in self.EXAMPLES["TEST"]["prompts"].items():
            console.print(f"  • {type}: {prompt}")
            
        self.data["TEST"]["prompt"] = Prompt.ask(
            "\n[bold green]Test prompt[/bold green]",
            default="Write a hello world function"
        )
        
        console.print("\n[yellow]What would success look like?[/yellow]")
        for type, success in self.EXAMPLES["TEST"]["success"].items():
            console.print(f"  • {type}: {success}")
            
        self.data["TEST"]["success"] = Prompt.ask(
            "\n[bold green]Success criteria[/bold green]",
            default="Function works and has proper documentation"
        )
        
    def to_markdown(self) -> str:
        """Convert to markdown format"""
        md = []
        md.append("# AGENTS.md\n")
        md.append("> AI Agent Instructions - Simple 5-Part Structure\n")
        
        # WHO
        md.append("## WHO")
        md.append(f"**Role:** {self.data['WHO']['role']}\n")
        
        # WHAT
        md.append("## WHAT")
        md.append(f"**Main Task:** {self.data['WHAT']['main_task']}\n")
        
        if self.data['WHAT']['can_do']:
            md.append("**Can Do:**")
            for item in self.data['WHAT']['can_do']:
                md.append(f"- {item}")
            md.append("")
            
        if self.data['WHAT']['cannot_do']:
            md.append("**Cannot Do:**")
            for item in self.data['WHAT']['cannot_do']:
                md.append(f"- {item}")
            md.append("")
            
        # HOW
        md.append("## HOW")
        md.append(f"**Style:** {self.data['HOW']['style']}")
        md.append(f"**Approach:** {self.data['HOW']['approach']}\n")
        
        # OUTPUT
        md.append("## OUTPUT")
        md.append(f"**Format:** {self.data['OUTPUT']['format']}")
        md.append(f"**Example:** {self.data['OUTPUT']['example']}\n")
        
        # TEST
        md.append("## TEST")
        md.append(f"**Test Prompt:** {self.data['TEST']['prompt']}")
        md.append(f"**Success Looks Like:** {self.data['TEST']['success']}\n")
        
        return "\n".join(md)

# ============= AI REFINER (OPTIONAL) =============

class AIRefiner:
    """Optional AI refinement using swarms"""
    
    def __init__(self):
        self.enabled = False
        self.agent = None
        
    def setup(self) -> bool:
        """Setup AI refinement if available"""
        try:
            from swarms import Agent
            from dotenv import load_dotenv
            
            load_dotenv()
            
            # Load metaprompt
            metaprompt_path = Path("agent-builder/metaprompt.md")
            if not metaprompt_path.exists():
                return False
                
            with open(metaprompt_path, "r") as f:
                system_prompt = f.read()
                
            self.agent = Agent(
                name="AgentRefiner",
                description="Refines agent prompts for clarity and completeness",
                model_name="claude-opus-4-20250514",
                system_prompt=system_prompt
            )
            
            self.enabled = True
            return True
            
        except Exception as e:
            console.print(f"[yellow]AI refinement not available: {e}[/yellow]")
            return False
            
    def refine(self, original: str) -> str:
        """Refine the agent prompt using AI"""
        if not self.enabled or not self.agent:
            return original
            
        console.print("\n[yellow]🤖 Refining with AI...[/yellow]")
        
        task = f"Improve this agent instruction:\n\n{original}"
        
        try:
            refined = self.agent.run(task)
            return refined
        except Exception as e:
            console.print(f"[red]Refinement failed: {e}[/red]")
            return original

# ============= MAIN BUILDER =============

class AgentsBuilder:
    """Main builder orchestrator"""
    
    def __init__(self):
        self.agent = SimpleAgent()
        self.refiner = AIRefiner()
        self.content = ""
        
    def run(self):
        """Run the builder process"""
        self._welcome()
        self._collect_inputs()
        self._generate()
        self._optional_refine()
        self._save()
        
    def _welcome(self):
        """Show welcome message"""
        console.clear()
        
        welcome = """
# 🚀 Simple AGENTS.md Builder

Create AI agent instructions in **3 minutes** using our **5-part structure**:

1️⃣  **WHO** - Agent role
2️⃣  **WHAT** - Main task & capabilities  
3️⃣  **HOW** - Style & approach
4️⃣  **OUTPUT** - Format & examples
5️⃣  **TEST** - Validation

Each step includes **examples** to guide you!
        """
        
        console.print(Markdown(welcome))
        
        if not Confirm.ask("\n[bold green]Ready to start?[/bold green]", default=True):
            exit()
            
    def _collect_inputs(self):
        """Collect all inputs step by step"""
        steps = ["1", "2", "3", "4", "5"]
        
        for step in steps:
            self.agent.collect_input(step)
            
        console.print("\n[bold green]✅ All information collected![/bold green]")
        
    def _generate(self):
        """Generate AGENTS.md content"""
        console.print("\n[yellow]Generating AGENTS.md...[/yellow]")
        self.content = self.agent.to_markdown()
        
        # Preview
        console.print("\n[bold cyan]Preview:[/bold cyan]")
        console.print(Panel(Markdown(self.content), title="AGENTS.md", border_style="green"))
        
    def _optional_refine(self):
        """Optional AI refinement"""
        if Confirm.ask("\n[yellow]Use AI to enhance this?[/yellow]", default=False):
            if self.refiner.setup():
                refined = self.refiner.refine(self.content)
                
                # Show comparison
                console.print("\n[bold]Original vs Refined:[/bold]")
                console.print(Panel(self.content[:300] + "...", title="Original", border_style="blue"))
                console.print(Panel(refined[:300] + "...", title="AI Enhanced", border_style="green"))
                
                if Confirm.ask("\n[yellow]Use refined version?[/yellow]", default=True):
                    self.content = refined
                    
    def _save(self):
        """Save the final result"""
        if Confirm.ask("\n[bold green]Save AGENTS.md?[/bold green]", default=True):
            filename = Prompt.ask("Filename", default="AGENTS.md")
            
            if not filename.endswith(".md"):
                filename += ".md"
                
            with open(filename, "w") as f:
                f.write(self.content)
                
            console.print(f"\n[bold green]✅ Saved to {filename}[/bold green]")
            
            # Also save JSON config
            config_file = filename.replace(".md", "_config.json")
            with open(config_file, "w") as f:
                json.dump(self.agent.data, f, indent=2)
                
            console.print(f"[green]📝 Config saved to {config_file}[/green]")
            
            # Usage instructions
            console.print("\n[bold]Next steps:[/bold]")
            console.print("1. Copy AGENTS.md to your repository root")
            console.print("2. AI agents will automatically use it")
            console.print("3. Test with your agent's TEST prompt")
            console.print("\n[dim]Tip: For monorepos, add AGENTS.md to each subproject[/dim]")

# ============= ENTRY POINT =============

def main():
    """Main entry point"""
    try:
        builder = AgentsBuilder()
        builder.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        
if __name__ == "__main__":
    main()