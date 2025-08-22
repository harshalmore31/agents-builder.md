# AI Refinement Guide (Optional)

The Agent Builder includes optional AI refinement capabilities using the `swarms` library to enhance your agent prompts with Claude Opus.

## Setup

### 1. Install Optional Dependencies

```bash
# Install with AI support
pip install -r requirements.txt
pip install swarms python-dotenv

# Or use pip extras
pip install -e ".[ai]"
```

### 2. Configure API Keys

Create a `.env` file in the project root:

```env
# For Claude via Swarms
ANTHROPIC_API_KEY=your_api_key_here

# Or other providers supported by swarms
OPENAI_API_KEY=your_openai_key
```

### 3. Enable AI Refinement

When running the builder, you'll be asked:

```
Use AI to enhance this? [y/N]: y
```

## How It Works

1. **Human Input First**: You create the initial agent using the 5-part structure
2. **AI Enhancement**: The AI refines your prompt for:
   - Clarity and completeness
   - Better examples
   - More specific instructions
   - Professional formatting
3. **Review & Choose**: You see both versions and pick the best one

## Without AI Setup

The builder works perfectly fine without AI refinement! You can:
- Create agents manually using the 5-part structure
- Use the example templates
- Skip AI enhancement when prompted

## Troubleshooting

### "AI refinement not available"
- Check that `swarms` is installed: `pip install swarms`
- Verify `.env` file exists with API keys
- Ensure `python-dotenv` is installed

### "Refinement failed"
- Check your API key is valid
- Verify you have API credits/quota
- Try again or use manual mode

## When to Use AI Refinement

**Good for:**
- Complex agent requirements
- Professional documentation needs
- When you want alternative phrasings
- Improving clarity of instructions

**Not needed for:**
- Simple agents (the 5-part structure is sufficient)
- When using example templates
- Quick prototypes
- When you know exactly what you want

## Swarms Library

The project uses [swarms](https://github.com/kyegomez/swarms) for AI integration:

```python
from swarms import Agent

agent = Agent(
    name="AgentRefiner",
    model_name="claude-opus-4-20250514",
    system_prompt=metaprompt
)
```

### Alternative AI Providers

Swarms supports multiple providers. Update `simple_builder.py` to use:
- OpenAI GPT-4
- Anthropic Claude
- Local models
- Other providers

## Privacy Note

When using AI refinement:
- Your prompts are sent to the AI provider (Anthropic/OpenAI)
- Use appropriate API keys for your use case
- Don't include sensitive information in prompts
- The tool works 100% offline without AI refinement

## Example Refinement

**Before (Human):**
```
WHO: Python developer
WHAT: Write code
HOW: Professional
```

**After (AI Enhanced):**
```
WHO: Senior Python developer specializing in clean, maintainable code
WHAT: 
  Main Task: Design and implement Python solutions
  Can Do:
  - Write production-ready Python code
  - Implement best practices and design patterns
  - Add comprehensive error handling
HOW: 
  Style: Professional and technically precise
  Approach: Methodical with emphasis on code quality
```

## Disabling AI

To completely disable AI features:

1. Don't install swarms: Use only `pip install rich`
2. Or set environment variable: `DISABLE_AI=true`
3. Always choose "N" when asked about enhancement

The tool is designed to work excellently without AI - it's truly optional!