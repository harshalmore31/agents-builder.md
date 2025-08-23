"""
Agent Builder Implementation with Three-Tier Architecture
Progressive disclosure system for agent prompt engineering
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime
import time
import json
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.tree import Tree
from rich.columns import Columns
from rich.layout import Layout
from rich.syntax import Syntax
from rich.text import Text
from rich import print as rprint

# Optional AI integration
try:
    from swarms import Agent
    from dotenv import load_dotenv
    import os
    SWARMS_AVAILABLE = True
    load_dotenv()
except ImportError:
    SWARMS_AVAILABLE = False
    Agent = None


class AgentBuilderMode(Enum):
    """Agent Builder complexity modes"""
    BASIC = "basic"           # 3 components: Role, Task, Constraints
    AI_ASSISTED = "ai_assisted"  # Basic + AI suggestions
    EXPERT = "expert"          # Full control with all parameters


@dataclass
class AgentBuilderMetrics:
    """Track performance and quality metrics"""
    mode: AgentBuilderMode
    start_time: float = field(default_factory=time.time)
    end_time: Optional[float] = None
    components_filled: int = 0
    total_components: int = 0
    ai_suggestions_used: int = 0
    ai_suggestions_offered: int = 0
    validation_score: float = 0.0
    user_satisfaction: Optional[float] = None
    
    @property
    def time_to_create(self) -> float:
        """Calculate time spent creating prompt"""
        if self.end_time:
            return self.end_time - self.start_time
        return time.time() - self.start_time
    
    @property
    def success_rate(self) -> float:
        """Calculate estimated success rate based on mode and completeness"""
        base_rates = {
            AgentBuilderMode.BASIC: 0.85,
            AgentBuilderMode.AI_ASSISTED: 0.92,
            AgentBuilderMode.EXPERT: 0.98
        }
        
        base_rate = base_rates[self.mode]
        completeness_factor = self.components_filled / max(self.total_components, 1)
        
        return base_rate * completeness_factor
    
    def to_dict(self) -> Dict:
        """Convert metrics to dictionary"""
        return {
            "mode": self.mode.value,
            "time_to_create_seconds": self.time_to_create,
            "components_filled": self.components_filled,
            "total_components": self.total_components,
            "ai_suggestions_used": self.ai_suggestions_used,
            "ai_suggestions_offered": self.ai_suggestions_offered,
            "validation_score": self.validation_score,
            "estimated_success_rate": self.success_rate,
            "user_satisfaction": self.user_satisfaction
        }


@dataclass
class ValidationResult:
    """Validation result for prompt quality"""
    is_valid: bool
    clarity_score: float  # 1-10
    completeness_score: float  # 0-1
    issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    
    @property
    def overall_score(self) -> float:
        """Calculate overall quality score"""
        return (self.clarity_score / 10 * 0.5) + (self.completeness_score * 0.5)


class AgentBuilder:
    """Base class for Agent Builder prompt building with progressive disclosure"""
    
    def __init__(self, mode: AgentBuilderMode = AgentBuilderMode.BASIC, interactive: bool = True):
        self.mode = mode
        self.interactive = interactive
        self.console = Console()
        self.metrics = AgentBuilderMetrics(mode=mode)
        self.components = self._initialize_components()
        self.ai_assistant = None
        
        if SWARMS_AVAILABLE and mode in [AgentBuilderMode.AI_ASSISTED, AgentBuilderMode.EXPERT]:
            self._initialize_ai_assistant()
    
    def _initialize_components(self) -> Dict[str, Any]:
        """Initialize components based on mode"""
        if self.mode == AgentBuilderMode.BASIC:
            components = {
                "role": None,
                "task": None,
                "constraints": []
            }
            self.metrics.total_components = 3
        elif self.mode == AgentBuilderMode.AI_ASSISTED:
            components = {
                "role": None,
                "task": None,
                "constraints": [],
                "context": None,
                "examples": [],
                "output_format": None
            }
            self.metrics.total_components = 6
        else:  # EXPERT mode
            components = {
                "role": None,
                "task": None,
                "constraints": [],
                "context": None,
                "examples": [],
                "output_format": None,
                "reasoning_pattern": None,
                "success_criteria": [],
                "edge_cases": [],
                "performance_requirements": None,
                "custom_instructions": []
            }
            self.metrics.total_components = 11
        
        return components
    
    def _initialize_ai_assistant(self):
        """Initialize AI assistant for suggestions"""
        if not SWARMS_AVAILABLE:
            return
        
        try:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                self.console.print("[yellow]Warning: ANTHROPIC_API_KEY not found. AI assistance disabled.[/yellow]")
                return
            
            # Load metaprompt from file
            metaprompt_path = Path(__file__).parent / "metaprompt.md"
            if metaprompt_path.exists():
                with open(metaprompt_path, 'r', encoding='utf-8') as f:
                    metaprompt = f.read()
            else:
                # Fallback metaprompt if file not found
                metaprompt = """You are an expert prompt engineering assistant specialized in creating high-quality prompts.
                
                Your role is to:
                1. Analyze user inputs and suggest improvements
                2. Identify missing components that would enhance prompt quality
                3. Provide specific, actionable suggestions
                4. Ensure clarity and completeness
                
                When given a prompt component, suggest improvements that:
                - Make instructions clearer and more specific
                - Add relevant constraints or guidelines
                - Include helpful examples when appropriate
                - Optimize for the intended use case
                
                Keep suggestions concise and actionable. Focus on quality over quantity."""
            
            self.ai_assistant = Agent(
                name="AgentBuilderAssistant",
                description="Agent Builder prompt engineering assistant",
                model_name="claude-sonnet-4-20250514",
                system_prompt=metaprompt,
                max_tokens=500
            )
        except Exception as e:
            self.console.print(f"[yellow]Warning: Could not initialize AI assistant: {e}[/yellow]")
            self.ai_assistant = None
    
    def _get_ai_suggestion(self, component: str, current_value: Any) -> Optional[str]:
        """Get AI suggestion for a component"""
        if not self.ai_assistant:
            return None
        
        try:
            prompt = f"""
            Component: {component}
            Current Value: {current_value if current_value else 'Not provided yet'}
            
            Provide a brief suggestion to improve this component. Be specific and actionable.
            If the current value is good, suggest a minor enhancement or confirm it's well-written.
            """
            
            suggestion = self.ai_assistant.run(prompt)
            self.metrics.ai_suggestions_offered += 1
            return suggestion
        except Exception as e:
            self.console.print(f"[yellow]Could not get AI suggestion: {e}[/yellow]")
            return None
    
    def validate_prompt(self) -> ValidationResult:
        """Validate the prompt quality"""
        issues = []
        suggestions = []
        
        # Check role clarity
        if not self.components.get("role"):
            issues.append("Role is not defined")
            clarity_score = 3.0
        elif len(self.components["role"]) < 20:
            suggestions.append("Consider adding more detail to the role description")
            clarity_score = 6.0
        else:
            clarity_score = 8.0
        
        # Check task specificity
        if not self.components.get("task"):
            issues.append("Task is not defined")
            clarity_score = min(clarity_score, 3.0)
        elif len(self.components["task"]) < 30:
            suggestions.append("Task could be more specific")
            clarity_score = min(clarity_score, 7.0)
        
        # Check constraints
        if not self.components.get("constraints"):
            suggestions.append("Consider adding constraints to guide behavior")
        
        # Calculate completeness
        filled = sum(1 for v in self.components.values() if v and (v != [] if isinstance(v, list) else True))
        completeness_score = filled / len(self.components)
        
        # Adjust clarity based on mode expectations
        if self.mode == AgentBuilderMode.EXPERT and completeness_score < 0.7:
            clarity_score = min(clarity_score, 6.0)
            suggestions.append("Expert mode should utilize more advanced components")
        
        result = ValidationResult(
            is_valid=len(issues) == 0,
            clarity_score=clarity_score,
            completeness_score=completeness_score,
            issues=issues,
            suggestions=suggestions
        )
        
        self.metrics.validation_score = result.overall_score
        return result
    
    def _display_mode_header(self, mode_name: str, description: str, color: str):
        """Display clean mode header"""
        title = f"Agent Builder - {mode_name}"
        panel_content = f"[{color}]{title}[/{color}]\n[dim italic]{description}[/dim italic]"
        
        self.console.print("\n" + "=" * 80)
        self.console.print(Panel.fit(
            panel_content,
            border_style=color,
            padding=(1, 2)
        ))
        self.console.print("=" * 80 + "\n")
    
    def _display_progress(self, step: int, total: int, step_name: str):
        """Display progress indicator"""
        progress_bar = "#" * step + "-" * (total - step)
        percentage = int((step / total) * 100)
        self.console.print(f"\n[cyan]Progress: [{progress_bar}] {percentage}% - {step_name}[/cyan]\n")
    
    def build_basic(self):
        """Build prompt using basic mode (3 components)"""
        if not self.interactive:
            return
        
        self._display_mode_header(
            "Basic Mode", 
            "Quick prompt creation with essential components (2-3 min)",
            "cyan"
        )
        
        # 1. Role
        self._display_progress(1, 3, "Define the Role")
        self.console.print(Panel(
            "[bold blue]Step 1: Define the Role[/bold blue]\n\n"
            "[dim]Who is the AI agent? What expertise should it have?\n"
            "Examples: 'a senior Python developer', 'a marketing expert', 'a data scientist'[/dim]",
            title="Role Definition",
            border_style="blue"
        ))
        role = Prompt.ask("[bold blue]Role[/bold blue]", console=self.console)
        self.components["role"] = role
        self.metrics.components_filled += 1
        
        # 2. Task
        self._display_progress(2, 3, "Define the Task")
        self.console.print(Panel(
            "[bold green]Step 2: Define the Task[/bold green]\n\n"
            "[dim]What should the agent do? Be specific about the goal.\n"
            "Examples: 'review code for bugs', 'write marketing copy', 'analyze data trends'[/dim]",
            title="Task Definition",
            border_style="green"
        ))
        task = Prompt.ask("[bold green]Task[/bold green]", console=self.console)
        self.components["task"] = task
        self.metrics.components_filled += 1
        
        # 3. Constraints
        self._display_progress(3, 3, "Define Constraints")
        self.console.print(Panel(
            "[bold red]Step 3: Define Constraints[/bold red]\n\n"
            "[dim]What rules or limitations should the agent follow?\n"
            "Examples: 'Be concise', 'Use simple language', 'Focus on security'[/dim]",
            title="Constraint Definition",
            border_style="red"
        ))
        
        constraints = []
        constraint_count = 1
        while True:
            constraint = Prompt.ask(f"[bold red]Constraint #{constraint_count} (or press Enter to finish)[/bold red]", default="", console=self.console)
            if not constraint:
                break
            constraints.append(constraint)
            self.console.print(f"[green]✓ Added:[/green] {constraint}")
            constraint_count += 1
        
        self.components["constraints"] = constraints
        if constraints:
            self.metrics.components_filled += 1
    
    def build_ai_assisted(self):
        """Build prompt with AI assistance"""
        if not self.interactive:
            return
        
        self._display_mode_header(
            "AI-Assisted Mode", 
            "Intelligent suggestions for enhanced prompts (5-8 min)",
            "green"
        )
        
        # Start with basic components
        self.build_basic()
        
        # AI enhancement for basic components
        if self.ai_assistant:
            self.console.print("\n[bold cyan]AI Enhancement Phase[/bold cyan]")
            
            # Suggest role improvements
            suggestion = self._get_ai_suggestion("role", self.components["role"])
            if suggestion:
                self.console.print(f"\n[yellow]AI Suggestion for Role:[/yellow]\n{suggestion}")
                if Confirm.ask("Apply this suggestion?"):
                    enhanced_role = Prompt.ask("Enhanced role", default=self.components["role"])
                    self.components["role"] = enhanced_role
                    self.metrics.ai_suggestions_used += 1
        
        # Additional components
        self.console.print("\n[bold]4. Add Context (Optional)[/bold]")
        self.console.print("[dim]Provide background information or domain context[/dim]")
        context = Prompt.ask("Context (press Enter to skip)", default="")
        if context:
            self.components["context"] = context
            self.metrics.components_filled += 1
        
        # Examples
        self.console.print("\n[bold]5. Add Examples (Optional)[/bold]")
        if Confirm.ask("Would you like to add examples?"):
            examples = []
            while True:
                self.console.print("[dim]Provide input-output example pair[/dim]")
                input_ex = Prompt.ask("Example input (or Enter to finish)")
                if not input_ex:
                    break
                output_ex = Prompt.ask("Expected output")
                examples.append({"input": input_ex, "output": output_ex})
            
            if examples:
                self.components["examples"] = examples
                self.metrics.components_filled += 1
        
        # Output format
        self.console.print("\n[bold]6. Define Output Format (Optional)[/bold]")
        output_format = Prompt.ask("Output format requirements (press Enter to skip)", default="")
        if output_format:
            self.components["output_format"] = output_format
            self.metrics.components_filled += 1
    
    def build_expert(self):
        """Build prompt with full expert control"""
        if not self.interactive:
            return
        
        self._display_mode_header(
            "Expert Mode", 
            "Full control for complex requirements (10-15 min)",
            "red"
        )
        
        # Start with AI-assisted components
        self.build_ai_assisted()
        
        # Expert-only components
        self.console.print("\n[bold]Expert Components[/bold]")
        
        # Reasoning pattern
        self.console.print("\n[bold]7. Reasoning Pattern[/bold]")
        patterns = ["analytical", "creative", "technical", "step-by-step", "comparative", "custom"]
        
        # Display numbered options
        for i, pattern_option in enumerate(patterns, 1):
            self.console.print(f"  {i}. {pattern_option.title()}")
        
        choice = Prompt.ask("Choose reasoning pattern", 
                          choices=[str(i) for i in range(1, len(patterns) + 1)], 
                          default="1")
        
        selected_pattern = patterns[int(choice) - 1]
        if selected_pattern == "custom":
            pattern = Prompt.ask("Define custom reasoning pattern")
        else:
            pattern = selected_pattern
        
        self.components["reasoning_pattern"] = pattern
        self.metrics.components_filled += 1
        
        # Success criteria
        self.console.print("\n[bold]8. Success Criteria[/bold]")
        criteria = []
        while True:
            criterion = Prompt.ask("Add success criterion (or Enter to finish)")
            if not criterion:
                break
            criteria.append(criterion)
        
        if criteria:
            self.components["success_criteria"] = criteria
            self.metrics.components_filled += 1
        
        # Edge cases
        if Confirm.ask("\nDefine edge cases?"):
            edge_cases = []
            while True:
                edge_case = Prompt.ask("Add edge case (or Enter to finish)")
                if not edge_case:
                    break
                edge_cases.append(edge_case)
            
            if edge_cases:
                self.components["edge_cases"] = edge_cases
                self.metrics.components_filled += 1
        
        # Performance requirements
        if Confirm.ask("\nAdd performance requirements?"):
            perf_req = Prompt.ask("Performance requirements")
            self.components["performance_requirements"] = perf_req
            self.metrics.components_filled += 1
        
        # Custom instructions
        if Confirm.ask("\nAdd custom instructions?"):
            custom = []
            while True:
                instruction = Prompt.ask("Add custom instruction (or Enter to finish)")
                if not instruction:
                    break
                custom.append(instruction)
            
            if custom:
                self.components["custom_instructions"] = custom
                self.metrics.components_filled += 1
    
    def build(self):
        """Main build method - routes to appropriate mode"""
        if self.mode == AgentBuilderMode.BASIC:
            self.build_basic()
        elif self.mode == AgentBuilderMode.AI_ASSISTED:
            self.build_ai_assisted()
        else:  # EXPERT
            self.build_expert()
        
        self.metrics.end_time = time.time()
    
    def generate_prompt(self) -> str:
        """Generate the final prompt string"""
        prompt_parts = []
        
        # Role
        if self.components.get("role"):
            prompt_parts.append(f"You are {self.components['role']}.")
        
        # Context
        if self.components.get("context"):
            prompt_parts.append(f"\nContext: {self.components['context']}")
        
        # Task
        if self.components.get("task"):
            prompt_parts.append(f"\nYour task is to {self.components['task']}.")
        
        # Constraints
        if self.components.get("constraints"):
            prompt_parts.append("\nConstraints:")
            for constraint in self.components["constraints"]:
                prompt_parts.append(f"- {constraint}")
        
        # Examples
        if self.components.get("examples"):
            prompt_parts.append("\nExamples:")
            for i, example in enumerate(self.components["examples"], 1):
                prompt_parts.append(f"\nExample {i}:")
                prompt_parts.append(f"Input: {example['input']}")
                prompt_parts.append(f"Output: {example['output']}")
        
        # Reasoning pattern
        if self.components.get("reasoning_pattern"):
            reasoning_instructions = {
                "analytical": "Think through this step-by-step, showing your reasoning.",
                "creative": "Explore multiple approaches before selecting the best one.",
                "technical": "Break down the technical requirements systematically.",
                "step-by-step": "Approach this methodically, one step at a time.",
                "comparative": "Compare different options and explain your choice."
            }
            
            pattern = self.components["reasoning_pattern"]
            if pattern in reasoning_instructions:
                prompt_parts.append(f"\n{reasoning_instructions[pattern]}")
            else:
                prompt_parts.append(f"\n{pattern}")
        
        # Output format
        if self.components.get("output_format"):
            prompt_parts.append(f"\nOutput Format: {self.components['output_format']}")
        
        # Success criteria
        if self.components.get("success_criteria"):
            prompt_parts.append("\nSuccess Criteria:")
            for criterion in self.components["success_criteria"]:
                prompt_parts.append(f"- {criterion}")
        
        # Edge cases
        if self.components.get("edge_cases"):
            prompt_parts.append("\nConsider these edge cases:")
            for edge_case in self.components["edge_cases"]:
                prompt_parts.append(f"- {edge_case}")
        
        # Performance requirements
        if self.components.get("performance_requirements"):
            prompt_parts.append(f"\nPerformance Requirements: {self.components['performance_requirements']}")
        
        # Custom instructions
        if self.components.get("custom_instructions"):
            prompt_parts.append("\nAdditional Instructions:")
            for instruction in self.components["custom_instructions"]:
                prompt_parts.append(f"- {instruction}")
        
        return "\n".join(prompt_parts)
    
    def save(self, filename: Optional[str] = None) -> str:
        """Save the prompt and metrics to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"sdpp_prompt_{self.mode.value}_{timestamp}.json"
        
        filepath = Path(filename)
        
        data = {
            "mode": self.mode.value,
            "components": self.components,
            "prompt": self.generate_prompt(),
            "metrics": self.metrics.to_dict(),
            "validation": None,
            "timestamp": datetime.now().isoformat()
        }
        
        # Add validation results
        validation = self.validate_prompt()
        data["validation"] = {
            "is_valid": validation.is_valid,
            "clarity_score": validation.clarity_score,
            "completeness_score": validation.completeness_score,
            "overall_score": validation.overall_score,
            "issues": validation.issues,
            "suggestions": validation.suggestions
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        return str(filepath)
    
    def display_summary(self):
        """Display summary of the created prompt"""
        self.console.clear()
        self.console.print("\n" + "=" * 60)
        self.console.print(Panel(
            "[bold green]Agent Builder Prompt Generation Complete[/bold green]",
            style="bold green",
            padding=(1, 2)
        ))
        self.console.print("=" * 60 + "\n")
        
        # Display metrics
        table = Table(title="Performance Metrics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Mode", self.mode.value.upper())
        table.add_row("Time to Create", f"{self.metrics.time_to_create:.1f} seconds")
        table.add_row("Components Filled", f"{self.metrics.components_filled}/{self.metrics.total_components}")
        table.add_row("Estimated Success Rate", f"{self.metrics.success_rate:.1%}")
        
        if self.metrics.ai_suggestions_offered > 0:
            table.add_row("AI Suggestions Used", f"{self.metrics.ai_suggestions_used}/{self.metrics.ai_suggestions_offered}")
        
        self.console.print(table)
        
        # Display validation
        validation = self.validate_prompt()
        
        val_table = Table(title="Validation Results")
        val_table.add_column("Aspect", style="cyan")
        val_table.add_column("Score", style="green")
        
        val_table.add_row("Clarity", f"{validation.clarity_score:.1f}/10")
        val_table.add_row("Completeness", f"{validation.completeness_score:.1%}")
        val_table.add_row("Overall Quality", f"{validation.overall_score:.1%}")
        val_table.add_row("Status", "Valid" if validation.is_valid else "Has Issues")
        
        self.console.print(val_table)
        
        if validation.issues:
            self.console.print("\n[bold red]Issues Found:[/bold red]")
            for issue in validation.issues:
                self.console.print(f"  - {issue}")
        
        if validation.suggestions:
            self.console.print("\n[bold yellow]Suggestions:[/bold yellow]")
            for suggestion in validation.suggestions:
                self.console.print(f"  - {suggestion}")
        
        # Display the generated prompt
        self.console.print("\n[bold]Generated Prompt:[/bold]")
        self.console.print(Panel(self.generate_prompt(), expand=False))


def interactive_mode_selection() -> AgentBuilderMode:
    """Interactive mode selection for users"""
    console = Console()
    
    # Clean welcome display
    console.print("\n" + "=" * 60)
    console.print(Panel(
        "[bold cyan]Welcome to Agent Builder[/bold cyan]\n\n"
        "[italic]Three-tier architecture for progressive prompt engineering[/italic]\n"
        "[dim]Choose your complexity level based on your needs[/dim]",
        title="Agent Builder v1.0",
        border_style="cyan",
        padding=(1, 3)
    ))
    console.print("=" * 60 + "\n")
    
    # Clean table styling
    table = Table(
        title="Available Modes", 
        show_header=True, 
        header_style="bold cyan",
        border_style="bright_blue",
        row_styles=["none", "dim"]
    )
    table.add_column("Mode", style="bold cyan", width=15)
    table.add_column("Components", style="bold yellow", width=35)
    table.add_column("Time", style="bold green", width=10)
    table.add_column("Success Rate", style="bold magenta", width=12)
    table.add_column("Best For", style="bold white", width=30)
    
    table.add_row(
        "BASIC",
        "3 (Role, Task, Constraints)",
        "2-3 min",
        "85%",
        "Quick prototypes, simple tasks"
    )
    table.add_row(
        "AI-ASSISTED",
        "6 (Basic + Context, Examples, Format)",
        "5-8 min",
        "92%",
        "Most use cases, optimal balance"
    )
    table.add_row(
        "EXPERT",
        "11+ (Full control + Advanced features)",
        "10-15 min",
        "98%",
        "Complex requirements, research"
    )
    
    console.print(table)
    
    # Clean mode selection with numbered options
    console.print("\n[bold]Select your mode:[/bold]")
    console.print("  1. Basic (2-3 min, simple tasks)")
    console.print("  2. AI-Assisted (5-8 min, most use cases) [Recommended]")
    console.print("  3. Expert (10-15 min, complex requirements)")
    
    mode_choice = Prompt.ask(
        "\n[bold cyan]Choose mode[/bold cyan]",
        choices=["1", "2", "3"],
        default="2",
        console=console
    )
    
    mode_map = {
        "1": AgentBuilderMode.BASIC,
        "2": AgentBuilderMode.AI_ASSISTED,  
        "3": AgentBuilderMode.EXPERT
    }
    
    return mode_map[mode_choice]


# def main():
#     """Main entry point for Agent Builder"""
#     console = Console()
    
#     try:
#         # Select mode with enhanced UI
#         mode = interactive_mode_selection()
        
#         # Create builder
#         builder = AgentBuilder(mode=mode)
        
#         # Build prompt with progress tracking
#         with console.status("[bold green]Initializing Agent Builder...") as status:
#             time.sleep(1)  # Brief loading animation
        
#         builder.build()
        
#         # Display summary with better visuals
#         builder.display_summary()
        
#         # Clean save dialog
#         save_panel = Panel(
#             "[bold blue]Save Your Prompt[/bold blue]\n\n"
#             "[dim]Would you like to save this prompt to a file for future use?\n"
#             "This will create a JSON file with your prompt and performance metrics.[/dim]",
#             title="Save Options",
#             border_style="blue"
#         )
#         console.print(save_panel)
        
#         if Confirm.ask("[bold blue]Save this prompt to file?[/bold blue]", console=console):
#             with console.status("[bold blue]Saving prompt..."):
#                 filepath = builder.save()
#                 time.sleep(0.5)  # Brief animation
#             console.print(Panel(
#                 f"[bold green]Success![/bold green]\n\nPrompt saved to: [cyan]{filepath}[/cyan]",
#                 title="Saved",
#                 border_style="green"
#             ))
        
#         # Clean feedback section
#         feedback_panel = Panel(
#             "[bold magenta]Rate Your Experience[/bold magenta]\n\n"
#             "[dim]Your feedback helps us improve the Agent Builder experience![/dim]",
#             title="Feedback",
#             border_style="magenta"
#         )
#         console.print(feedback_panel)
        
#         if Confirm.ask("[bold magenta]Would you like to rate this experience?[/bold magenta]", console=console):
#             rating = Prompt.ask(
#                 "[bold magenta]Rate your satisfaction (1-10)[/bold magenta]", 
#                 default="8",
#                 console=console
#             )
#             try:
#                 rating_num = float(rating)
#                 builder.metrics.user_satisfaction = rating_num
                
#                 # Visual feedback based on rating
#                 if rating_num >= 8:
#                     console.print(Panel(
#                         "[bold green]Thank you for the great rating![/bold green]\n"
#                         "[dim]We're glad you had a positive experience with Agent Builder![/dim]",
#                         title="Excellent!",
#                         border_style="green"
#                     ))
#                 elif rating_num >= 6:
#                     console.print(Panel(
#                         "[bold yellow]Thanks for your feedback![/bold yellow]\n"
#                         "[dim]We're always working to improve the experience![/dim]",
#                         title="Good!",
#                         border_style="yellow"
#                     ))
#                 else:
#                     console.print(Panel(
#                         "[bold red]Thank you for the honest feedback![/bold red]\n"
#                         "[dim]We'll use this to make Agent Builder better![/dim]",
#                         title="Feedback Received",
#                         border_style="red"
#                     ))
#             except ValueError:
#                 console.print("[yellow]Invalid rating, but thanks anyway![/yellow]")
        
#         # Final goodbye message
#         console.print(Panel(
#             "[bold cyan]Thank you for using Agent Builder![/bold cyan]\n\n"
#             "[dim]Visit us at github.com/agent-builder for more tools and updates![/dim]",
#             title="Goodbye!",
#             border_style="cyan"
#         ))
    
#     except KeyboardInterrupt:
#         console.print(Panel(
#             "[bold yellow]Process cancelled by user[/bold yellow]\n\n"
#             "[dim]No worries! Come back anytime to build amazing AI agents![/dim]",
#             title="Until next time!",
#             border_style="yellow"
#         ))
#     except Exception as e:
#         console.print(Panel(
#             f"[bold red]An error occurred:[/bold red]\n\n[dim]{e}[/dim]",
#             title="Error",
#             border_style="red"
#         ))
#         raise


# if __name__ == "__main__":
#     main()