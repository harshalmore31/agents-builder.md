# 🤖 Agent Builder

> **Create AI agent instructions in 3 minutes using the simple 5-part AGENTS.md standard**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## What is this?

Agent Builder helps you create standardized prompts for AI agents (like Claude, GPT-4, etc.) using a simple, proven structure. Perfect for:
- 🚀 Creating AGENTS.md files for your repositories
- 💡 Building consistent AI agent behaviors
- 🔧 Standardizing prompts across teams
- 📚 Learning prompt engineering best practices

## Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/agents-builder/agents-builder.git
cd agents-builder

# Install dependencies
pip install -r requirements.txt

# Run the builder
python agent-builder/build.py
```

### 2. The Simple 5-Part Structure

Every agent needs just 5 things:

1. **WHO** - What role/expertise?
2. **WHAT** - What's the main task?
3. **HOW** - What style/approach?
4. **OUTPUT** - What format for results?
5. **TEST** - How to validate it works?

### 3. Example Agent

```yaml
# Code Review Agent

WHO:
  ROLE: "Senior Python developer"

WHAT:
  MAIN_TASK: "Review code for quality"
  CAN_DO:
    - Find bugs
    - Suggest improvements
    - Check style

HOW:
  STYLE: Technical
  APPROACH: Careful

OUTPUT:
  FORMAT: List
  EXAMPLE: "✅ Good: Clear code ⚠️ Issue: Missing tests"

TEST:
  TEST_PROMPT: "Review: def add(a,b): return a+b"
  SUCCESS: "Should mention missing docstring"
```

## Features

### 🎯 Version 1.0 - Simple & Working
- **Interactive CLI** - Guided prompt creation with Rich UI
- **5-Part Structure** - Simple, proven template
- **Instant Testing** - Validate your prompts immediately  
- **JSON Export** - Save and reuse configurations
- **AGENTS.md Ready** - Generate files for your repos

### 🚀 Optional AI Enhancement
- **AI Refinement** - Enhance prompts with Claude Opus ([setup guide](AI_REFINEMENT.md))
- **Works Without AI** - Fully functional offline mode
- **Privacy First** - AI is completely optional
- **Multiple Providers** - Support via swarms library

## File Structure

```
agent-builder/
├── main.py                      # Current interactive builder
├── SIMPLE_AGENT_STANDARD_V1.md  # The 5-part standard
├── hybrid_generator.py          # v2.0 AI-enhanced builder
├── agents_md_generator.py       # AGENTS.md file generator
└── metaprompt_refiner.py        # AI refinement engine
```

## Why AGENTS.md?

**README.md** = For humans (setup, contribution guidelines)  
**AGENTS.md** = For AI agents (how to work with your code)

Benefits:
- 📍 Predictable location for AI instructions
- 🎯 Keeps READMEs human-focused
- 🔄 Works with all AI coding assistants
- 📦 Supports monorepos with nested files

## Usage Examples

### Create Your First Agent
```bash
# Interactive builder with examples at each step
python agent-builder/build.py
```

### Use Example Templates
```bash
# View available examples
python agent-builder/examples.py

# Use a specific template
python agent-builder/examples.py code_reviewer
```

## The Standard

Our **Simple Agent Standard v1.0** provides:
- ✅ 5 essential components
- ✅ 3-minute creation process
- ✅ Works for any agent type
- ✅ Built-in validation

Read the full standard: [SIMPLE_AGENT_STANDARD_V1.md](agent-builder/SIMPLE_AGENT_STANDARD_V1.md)

## Templates

### Quick Templates

**🔧 Coding Agent**
```yaml
WHO: ROLE: "Python developer"
WHAT: MAIN_TASK: "Write clean code"
HOW: STYLE: Technical, APPROACH: Careful
```

**📝 Writing Agent**
```yaml
WHO: ROLE: "Technical writer"
WHAT: MAIN_TASK: "Create documentation"
HOW: STYLE: Educational, APPROACH: Clear
```

**🔍 Analysis Agent**
```yaml
WHO: ROLE: "Data analyst"
WHAT: MAIN_TASK: "Analyze patterns"
HOW: STYLE: Professional, APPROACH: Thorough
```

## Contributing

We welcome contributions! The standard is meant to evolve with community input.

1. Try the builder
2. Create agents
3. Share what works
4. Suggest improvements

## Philosophy

> **Simple beats complex. Working beats perfect. Clear beats clever.**

We believe AI agents should be:
- Easy to create (3 minutes, not 3 hours)
- Simple to understand (5 parts, not 50)
- Quick to test (immediate validation)
- Ready to use (no complex setup)

## Roadmap

- [x] v1.0 - Simple 5-part structure
- [x] Interactive CLI builder
- [x] JSON import/export
- [ ] v2.0 - AI refinement integration
- [ ] Template library
- [ ] Web interface
- [ ] Team collaboration features

## License

MIT - Use freely in your projects!

## Links

- [Full Documentation](agent-builder/SIMPLE_AGENT_STANDARD_V1.md)
- [AI Refinement Guide](AI_REFINEMENT.md)
- [Quick Start Guide](agent-builder/quick_start.md)
- [Examples](agent-builder/examples.py)
- [Contributing](CONTRIBUTING.md)
- [Community Templates](https://github.com/agents-builder/agent-templates)

---

**Remember:** A simple prompt that works is better than a complex one that confuses. Start simple, test early, iterate often! 🚀