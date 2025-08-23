# Agent Builder

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/swarms-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)

A professional AI agent prompt engineering framework with three-tier progressive complexity, making AI agent development accessible to everyone from beginners to experts through systematic prompt construction.

## ✨ Key Features

- **🎯 Three-Tier Progressive System**: Basic → AI-Assisted → Expert modes
- **🤖 AI-Powered Suggestions**: Intelligent prompt enhancement via Swarms integration  
- **📊 Quality Metrics**: Real-time validation and success rate tracking
- **💻 Professional Interface**: Clean, Windows-compatible terminal UI
- **💾 Export & Save**: JSON export with comprehensive metrics
- **📈 Performance Analytics**: Time-to-create and effectiveness tracking

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/The-Swarm-Corporation/agents-builder.md.git
cd agents-builder.md

# Install dependencies
pip install -r requirements.txt

# Run the demo
python examples/demo.py
```

### Basic Usage

```python
from agent_builder import AgentBuilder, AgentBuilderMode

# Interactive mode selection
from agent_builder import interactive_mode_selection
mode = interactive_mode_selection()
builder = AgentBuilder(mode=mode)
builder.build()
builder.display_summary()

# Programmatic usage
builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
builder.components["role"] = "a helpful Python developer"
builder.components["task"] = "review code for bugs and best practices"  
builder.components["constraints"] = ["Be constructive", "Focus on security"]

prompt = builder.generate_prompt()
print(prompt)
```

### Quick Example

```bash
# Run the demo
python examples/demo.py

# Test functionality  
python tests/test_simple.py
```

## 🏗️ Three-Tier Architecture

| Mode | Components | Time | Success Rate | Best For |
|------|------------|------|--------------|----------|
| **Basic** | 3 (Role, Task, Constraints) | 2-3 min | 85% | Quick prototypes, simple tasks |
| **AI-Assisted** | 6 (Basic + Context, Examples, Format) | 5-8 min | 92% | Most use cases, optimal balance |
| **Expert** | 11+ (Full control + Advanced features) | 10-15 min | 98% | Complex requirements, research |

### Basic Mode Example

```python
builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
builder.components.update({
    "role": "a professional Python code reviewer",
    "task": "review Python code for bugs and security issues", 
    "constraints": ["Focus on critical issues", "Provide examples"]
})
```

**Generated Output:**
```
You are a professional Python code reviewer.

Your task is to review Python code for bugs and security issues.

Constraints:
- Focus on critical issues
- Provide examples
```

## 📊 Quality & Performance

Agent Builder includes comprehensive quality assessment:

```python
validation = builder.validate_prompt()
print(f"Quality Score: {validation.overall_score:.1%}")
print(f"Success Rate: {builder.metrics.success_rate:.1%}")
print(f"Time to Create: {builder.metrics.time_to_create:.1f}s")
```

**Metrics Tracked:**
- Clarity score (1-10 scale)
- Completeness assessment  
- Component coverage
- AI suggestion adoption
- User satisfaction ratings

## 🤖 AI Integration

Leverages Swarms framework for intelligent suggestions:

```bash
# Setup (optional - fallback available)
export ANTHROPIC_API_KEY="your_key_here"
```

**Features:**
- Component analysis and improvement suggestions
- Context-aware recommendations
- Real-time quality scoring
- Adaptive suggestions based on use case

## 💾 Export & Persistence

```python
# Save with full metrics
filepath = builder.save()
print(f"Saved to: {filepath}")

# Load and analyze
import json
with open(filepath) as f:
    data = json.load(f)
    
print(f"Mode: {data['mode']}")
print(f"Quality: {data['validation']['overall_score']:.1%}")
print(f"Success Rate: {data['metrics']['estimated_success_rate']:.1%}")
```

## 📁 Project Structure

```
agents-builder.md/
├── agent_builder/           # Main package
│   ├── __init__.py         # Package exports
│   ├── agent_builder.py    # Core AgentBuilder class
│   ├── legacy_builder.py   # Legacy SimpleAgent (compatibility)
│   └── metaprompt.md       # AI assistant system prompt
├── examples/               # Usage examples
│   ├── demo.py            # Interactive demo
│   └── basic_examples.py   # Programmatic examples
├── tests/                 # Test suite
│   └── test_simple.py     # Core functionality tests
├── archive/               # Legacy files (not included in package)
├── DOCS.md                # Complete documentation
├── CONTRIBUTING.md        # Contribution guidelines
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
├── LICENSE               # MIT License
└── README.md             # This file
```

## 🧪 Testing

```bash
# Run core functionality tests
python tests/test_simple.py

# Run interactive demo
python examples/demo.py

# Test all three modes
python -c "
from agent_builder import AgentBuilder, AgentBuilderMode
for mode in AgentBuilderMode:
    builder = AgentBuilder(mode=mode, interactive=False)
    print(f'{mode.value}: {builder.metrics.success_rate:.1%} success rate')
"
```

## 📖 Usage Examples

### Code Review Agent (Basic Mode)
```python
from agent_builder import AgentBuilder, AgentBuilderMode

builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
builder.components.update({
    "role": "an experienced Python code reviewer",
    "task": "review Python code for bugs, security issues, and best practices",
    "constraints": ["Focus on critical issues", "Provide actionable feedback", "Be educational"]
})

prompt = builder.generate_prompt()
# Generates professional code review agent prompt
```

### Data Analyst Agent (AI-Assisted Mode)
```python
builder = AgentBuilder(mode=AgentBuilderMode.AI_ASSISTED, interactive=False)
builder.components.update({
    "role": "a senior business intelligence analyst",
    "task": "analyze sales data and provide actionable business insights",
    "constraints": ["Use statistical validation", "Focus on business impact"],
    "context": "E-commerce company with seasonal patterns",
    "examples": [{"input": "Q2 sales decline", "output": "Analysis with recommendations"}],
    "output_format": "Executive summary with key findings and action items"
})
# AI suggestions enhance the prompt automatically
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick Start:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Documentation

For detailed documentation, examples, and advanced usage:

- **[Complete Documentation](DOCS.md)** - Full API reference and usage guide
- **[Examples](examples/)** - Comprehensive usage examples
- **[Contributing](CONTRIBUTING.md)** - Development and contribution guidelines

## 🤝 Contributing

We welcome contributions! Agent Builder is designed to be extensible and community-driven.

**Quick Start:**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests and documentation
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📖 Citation

If you use Agent Builder in your research or project, please cite:

```bibtex
@software{agent_builder_2024,
  author = {The Swarm Corporation},
  title = {Agent Builder: Professional AI Agent Prompt Engineering},
  url = {https://github.com/The-Swarm-Corporation/agents-builder.md},
  year = {2024}
}
```

## 🔗 Related Work

- **[Swarms Framework](https://github.com/kyegomez/swarms)** - Multi-agent orchestration platform
- **[AI-CoScientist](https://github.com/The-Swarm-Corporation/AI-CoScientist)** - AI research assistant

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/The-Swarm-Corporation/agents-builder.md/issues)
- **Discussions**: [GitHub Discussions](https://github.com/The-Swarm-Corporation/agents-builder.md/discussions)
- **Discord**: [Join our community](https://discord.gg/agentops)
- **Documentation**: [Complete guide](DOCS.md)

## 🚧 TODO

- [ ] Web interface for non-technical users
- [ ] Template marketplace for community-contributed prompts
- [ ] Integration with additional AI providers (OpenAI, Anthropic direct APIs)
- [ ] Advanced analytics dashboard with usage metrics
- [ ] Team collaboration features for enterprise use
- [ ] Plugin system for custom validators and enhancers
- [ ] Multi-language prompt generation support
- [ ] Automated prompt testing and optimization
- [ ] Integration with popular AI development frameworks
- [ ] Mobile app for prompt creation on-the-go

---

**🎯 Start with AI-Assisted mode for the best balance of simplicity and power!**

*Built with ❤️ by [The Swarm Corporation](https://github.com/The-Swarm-Corporation)*