"""Demo script showing the cleaned Agent Builder interface"""

import time
from sdpp_builder import AgentBuilder, AgentBuilderMode
from rich.console import Console
from rich.panel import Panel

def demo_clean_interface():
    """Demonstrate the clean, professional interface"""
    console = Console()
    
    # Show clean welcome
    console.print("\n" + "=" * 60)
    console.print(Panel(
        "[bold cyan]Welcome to Agent Builder[/bold cyan]\n\n"
        "[italic]Three-tier architecture for progressive prompt engineering[/italic]\n"
        "[dim]Professional, clean interface for AI agent development[/dim]",
        title="Agent Builder v1.0",
        border_style="cyan",
        padding=(1, 2)
    ))
    console.print("=" * 60)
    
    # Demo each mode
    modes = [
        (AgentBuilderMode.BASIC, "Basic Mode", "cyan"),
        (AgentBuilderMode.AI_ASSISTED, "AI-Assisted Mode", "green"), 
        (AgentBuilderMode.EXPERT, "Expert Mode", "red")
    ]
    
    for mode, name, color in modes:
        console.print(f"\n[{color}]{'='*20} {name} Demo {'='*20}[/{color}]")
        
        # Create builder
        builder = AgentBuilder(mode=mode, interactive=False)
        
        # Set sample data based on mode
        if mode == AgentBuilderMode.BASIC:
            builder.components.update({
                "role": "a professional Python code reviewer",
                "task": "review Python code for bugs, security issues, and best practices",
                "constraints": [
                    "Focus on critical security vulnerabilities",
                    "Provide specific, actionable recommendations",
                    "Explain the reasoning behind each suggestion"
                ]
            })
            builder.metrics.components_filled = 3
            
        elif mode == AgentBuilderMode.AI_ASSISTED:
            builder.components.update({
                "role": "a senior business intelligence analyst",
                "task": "analyze sales performance data and generate actionable business insights",
                "constraints": [
                    "Use statistical methods to validate findings", 
                    "Present results in business-friendly language",
                    "Include confidence levels for all predictions"
                ],
                "context": "Multi-channel retail company with seasonal business patterns",
                "examples": [
                    {
                        "input": "Q3 sales data showing 12% decline in mobile category",
                        "output": "Analysis: Mobile sales decline correlates with new competitor entry and seasonal patterns. Recommend targeted promotional campaign. Confidence: 78%"
                    }
                ],
                "output_format": "Executive summary with key findings, statistical confidence, and prioritized recommendations"
            })
            builder.metrics.components_filled = 6
            
        else:  # Expert mode
            builder.components.update({
                "role": "a principal AI system architect specializing in high-performance distributed systems",
                "task": "design a fault-tolerant, scalable machine learning inference pipeline for real-time recommendations",
                "constraints": [
                    "Must handle 1M+ requests per second with sub-100ms P99 latency",
                    "Ensure 99.99% uptime with automatic failover capabilities",
                    "Maintain GDPR and SOC2 compliance throughout the system"
                ],
                "context": "Global streaming platform serving 100M+ users across 50+ countries with strict regulatory requirements",
                "reasoning_pattern": "technical",
                "success_criteria": [
                    "P99 latency under 100ms during peak load",
                    "Zero data loss during system failures", 
                    "Automatic scaling to handle 10x traffic spikes"
                ],
                "edge_cases": [
                    "Cold start performance for new users",
                    "Multi-region failover scenarios",
                    "Gradual model rollout with A/B testing"
                ],
                "performance_requirements": "1M+ RPS, <100ms P99 latency, 99.99% availability, <0.01% error rate",
                "custom_instructions": [
                    "Prioritize horizontal scaling over vertical scaling",
                    "Use event-driven architecture where appropriate",
                    "Include comprehensive monitoring and alerting strategy"
                ]
            })
            builder.metrics.components_filled = 11
        
        # Show clean progress simulation
        console.print(f"[{color}]Processing {name}...[/{color}]")
        time.sleep(0.5)
        
        # Generate prompt
        prompt = builder.generate_prompt()
        
        # Show metrics
        validation = builder.validate_prompt()
        console.print(f"\n[bold]Results:[/bold]")
        console.print(f"  Quality Score: [green]{validation.overall_score:.1%}[/green]")
        console.print(f"  Success Rate: [green]{builder.metrics.success_rate:.1%}[/green]")
        console.print(f"  Components: [cyan]{builder.metrics.components_filled}/{builder.metrics.total_components}[/cyan]")
        
        # Show generated prompt (truncated for demo)
        console.print(f"\n[bold]Generated Prompt Preview:[/bold]")
        preview = prompt[:200] + "..." if len(prompt) > 200 else prompt
        console.print(Panel(preview, border_style=color, padding=(0, 1)))
    
    # Summary
    console.print("\n" + "=" * 60)
    console.print(Panel(
        "[bold green]Agent Builder Demo Complete[/bold green]\n\n"
        "[dim]Clean, professional interface without excessive emojis\n"
        "Optimized for Windows console compatibility\n"
        "Three-tier architecture with progressive complexity[/dim]",
        title="Demo Results",
        border_style="green"
    ))
    console.print("=" * 60)
    
    console.print("\n[bold cyan]Key Improvements:[/bold cyan]")
    console.print("  - Removed excessive emojis and Unicode characters")
    console.print("  - Clean, professional terminal output")
    console.print("  - Windows console compatibility")
    console.print("  - Maintained rich functionality with better UX")
    console.print("  - Progressive disclosure across three tiers")

if __name__ == "__main__":
    demo_clean_interface()