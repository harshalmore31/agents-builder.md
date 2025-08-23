"""
Agent Builder - Create AI agent instructions in 3 minutes
"""

__version__ = "1.0.0"
__author__ = "The Swarm Corporation"

from .legacy_builder import SimpleAgent, AIRefiner, AgentsBuilder
from .agent_builder import AgentBuilder, AgentBuilderMode, AgentBuilderMetrics, ValidationResult, interactive_mode_selection

__all__ = [
    "SimpleAgent",
    "AIRefiner", 
    "AgentsBuilder",
    "AgentBuilder",
    "AgentBuilderMode",
    "AgentBuilderMetrics",
    "ValidationResult",
    "interactive_mode_selection"
]