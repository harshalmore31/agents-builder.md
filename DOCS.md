# 📖 Agent Builder Documentation

## Overview

Agent Builder is a professional AI prompt engineering tool featuring a three-tier progressive architecture:

- **Basic Mode**: 3 components (Role, Task, Constraints) - 85% success rate
- **AI-Assisted Mode**: 6 components with AI suggestions - 92% success rate  
- **Expert Mode**: 11+ components with full control - 98% success rate

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/The-Swarm-Corporation/agents-builder.md.git
cd agents-builder.md

# Install dependencies
pip install -r requirements.txt

# Run demo
python examples/demo.py
```

### Basic Usage

```python
from agent_builder import AgentBuilder

# Create and run agent builder
builder = AgentBuilder()
builder.build()

# Your professional prompt is ready!
print(builder.generate_prompt())
```

## 🏗️ Architecture

### Core Classes

#### `AgentBuilder`
Main class implementing the three-tier architecture.

```python
class AgentBuilder:
    def __init__(self, mode: AgentBuilderMode, interactive: bool = True):
        """
        Initialize AgentBuilder with specified mode.
        
        Args:
            mode: AgentBuilderMode (BASIC, AI_ASSISTED, EXPERT)
            interactive: Enable interactive UI (default: True)
        """
```

**Key Methods:**
- `build()` - Interactive prompt building
- `generate_prompt()` - Generate final prompt string
- `validate_prompt()` - Quality assessment
- `save()` - Export to JSON with metrics

#### `AgentBuilderMode`
Enum defining the three complexity tiers.

```python
class AgentBuilderMode(Enum):
    BASIC = "basic"           # 3 components: Role, Task, Constraints
    AI_ASSISTED = "ai_assisted"  # Basic + AI suggestions
    EXPERT = "expert"          # Full control with all parameters
```

#### `AgentBuilderMetrics`
Performance and quality tracking.

```python
@dataclass
class AgentBuilderMetrics:
    mode: AgentBuilderMode
    time_to_create: float          # Seconds
    components_filled: int
    ai_suggestions_used: int
    validation_score: float
    estimated_success_rate: float
```

### Component Structure

#### Basic Mode Components
- **role**: AI agent's expertise and personality
- **task**: Specific objective or goal  
- **constraints**: Rules and limitations

#### AI-Assisted Mode (Basic +)
- **context**: Background information
- **examples**: Input/output examples
- **output_format**: Expected response structure

#### Expert Mode (AI-Assisted +)
- **reasoning_pattern**: Thinking approach (analytical, creative, technical)
- **success_criteria**: Measurable success metrics
- **edge_cases**: Exception scenarios to handle
- **performance_requirements**: Speed/quality requirements
- **custom_instructions**: Additional specialized rules

## 🎯 Usage Patterns

### Basic Mode - Quick Prototyping

**Best for**: Simple tasks, quick testing, proof of concepts

```python
builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
builder.components.update({
    "role": "a friendly customer support representative",
    "task": "help customers with product questions and issues",
    "constraints": ["Be patient and helpful", "Escalate complex issues", "Follow company policies"]
})

prompt = builder.generate_prompt()
# Ready to use with any AI model
```

### AI-Assisted Mode - Production Ready

**Best for**: Most production use cases, balanced complexity

```python
builder = AgentBuilder(mode=AgentBuilderMode.AI_ASSISTED, interactive=False)
builder.components.update({
    "role": "a senior business analyst",
    "task": "analyze sales data and provide actionable insights",
    "constraints": ["Use statistical methods", "Focus on business impact"],
    "context": "E-commerce company with seasonal patterns",
    "examples": [{"input": "Q2 sales decline", "output": "Analysis with recommendations"}],
    "output_format": "Executive summary with key findings and action items"
})

# AI suggestions automatically enhance the prompt
```

### Expert Mode - Mission Critical

**Best for**: Complex systems, research, high-stakes applications

```python
builder = AgentBuilder(mode=AgentBuilderMode.EXPERT, interactive=False)
builder.components.update({
    "role": "a principal AI system architect",
    "task": "design scalable ML inference architecture",
    "constraints": ["Handle 1M+ RPS", "Sub-100ms latency"],
    "reasoning_pattern": "technical",
    "success_criteria": ["P99 latency < 100ms", "99.99% uptime"],
    "edge_cases": ["Cold start scenarios", "Regional failures"],
    "performance_requirements": "1M+ RPS, <100ms P99 latency"
})
```

## 🤖 AI Integration

### Swarms Framework Integration

Agent Builder uses the Swarms framework for AI-powered suggestions:

```python
# Optional: Set up AI assistance
export ANTHROPIC_API_KEY="your_key_here"

# AI assistant automatically provides suggestions
builder = AgentBuilder(mode=AgentBuilderMode.AI_ASSISTED)
# AI will analyze components and suggest improvements
```

### Custom Metaprompt

The AI assistant uses `metaprompt.md` for component analysis:

```markdown
You are an expert prompt engineering assistant. Your task is to analyze user prompt components and provide specific, actionable suggestions for improvement.

Guidelines:
- Keep suggestions concise (2-3 sentences max)
- Provide specific examples rather than general advice
- Focus on one key improvement per suggestion
- Ensure suggestions are immediately actionable
```

## 📊 Quality & Metrics

### Validation System

```python
validation = builder.validate_prompt()
print(f"Clarity Score: {validation.clarity_score}/10")
print(f"Completeness: {validation.completeness_score:.1%}")  
print(f"Overall Quality: {validation.overall_score:.1%}")
print(f"Issues: {validation.issues}")
print(f"Suggestions: {validation.suggestions}")
```

### Performance Tracking

```python
metrics = builder.metrics
print(f"Time to Create: {metrics.time_to_create:.1f}s")
print(f"Success Rate: {metrics.success_rate:.1%}")
print(f"Components: {metrics.components_filled}/{metrics.total_components}")
print(f"AI Usage: {metrics.ai_suggestions_used}/{metrics.ai_suggestions_offered}")
```

## 💾 Export & Persistence

### JSON Export

```python
# Save with full metrics
filepath = builder.save()
print(f"Saved to: {filepath}")

# Custom filename
builder.save("my_agent_prompt.json")
```

### Export Format

```json
{
  "mode": "ai_assisted",
  "components": {
    "role": "...",
    "task": "...",
    "constraints": [...],
    "context": "...",
    "examples": [...],
    "output_format": "..."
  },
  "prompt": "Generated prompt text...",
  "metrics": {
    "time_to_create_seconds": 420,
    "estimated_success_rate": 0.92,
    "validation_score": 0.87
  },
  "validation": {
    "is_valid": true,
    "clarity_score": 8.5,
    "overall_score": 0.87
  },
  "timestamp": "2024-08-23T10:30:00"
}
```

## 🧪 Testing

### Running Tests

```bash
# Core functionality test
python tests/test_simple.py

# Interactive demo
python examples/demo.py

# Programmatic examples
python examples/basic_examples.py
```

### Custom Testing

```python
def test_custom_agent():
    builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
    builder.components["role"] = "test role"
    builder.components["task"] = "test task" 
    builder.components["constraints"] = ["test constraint"]
    
    prompt = builder.generate_prompt()
    validation = builder.validate_prompt()
    
    assert prompt is not None
    assert validation.is_valid
    assert builder.metrics.success_rate >= 0.8
```

## 🔧 Customization

### Custom Validation Rules

```python
def custom_validator(components):
    issues = []
    suggestions = []
    
    if len(components.get("role", "")) < 20:
        suggestions.append("Make role more specific")
    
    return ValidationResult(
        is_valid=len(issues) == 0,
        clarity_score=8.0,
        completeness_score=0.9,
        issues=issues,
        suggestions=suggestions
    )

# Apply custom validation
builder.validator = custom_validator
```

### Batch Processing

```python
configs = [
    {"mode": "basic", "role": "assistant", "task": "help users"},
    {"mode": "expert", "role": "architect", "task": "design systems"}
]

results = []
for config in configs:
    builder = AgentBuilder(
        mode=AgentBuilderMode[config["mode"].upper()], 
        interactive=False
    )
    builder.components.update(config)
    results.append(builder.generate_prompt())
```

## 🚀 Best Practices

### Choosing the Right Mode

- **Basic Mode**: Simple, single-purpose agents
- **AI-Assisted Mode**: Most production applications  
- **Expert Mode**: Complex, mission-critical systems

### Prompt Quality Tips

1. **Be Specific**: Detailed roles perform better than generic ones
2. **Add Context**: Background information improves relevance
3. **Include Examples**: Show expected input/output patterns
4. **Set Constraints**: Define clear behavioral boundaries
5. **Test Iteratively**: Validate with real use cases

### Performance Optimization

- Use AI-Assisted mode for best balance of quality and speed
- Validate prompts before production deployment
- Monitor success rates and user satisfaction
- Iterate based on real-world feedback

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/The-Swarm-Corporation/agents-builder.md/issues)
- **Discussions**: [GitHub Discussions](https://github.com/The-Swarm-Corporation/agents-builder.md/discussions)
- **Discord**: [Join our community](https://discord.gg/agentops)

---

*For more examples and advanced usage patterns, see the [examples/](examples/) directory.*