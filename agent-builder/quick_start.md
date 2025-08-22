# 🚀 Quick Start Guide

## 1-Minute Setup

```bash
# Run the builder
python build.py

# Or use the simple builder directly
python simple_builder.py
```

## What You'll Create

A simple **AGENTS.md** file with 5 parts:

1. **WHO** - Agent identity (1 line)
2. **WHAT** - What it does (5-6 lines)
3. **HOW** - Working style (2 choices)
4. **OUTPUT** - Result format (2 lines)
5. **TEST** - Validation (2 lines)

## Example Flow

```
🚀 Simple AGENTS.md Builder

Step 1: WHO is this agent?
Examples:
  • Coding: Senior Python developer
  • Writing: Technical writer
  • Testing: QA engineer

> Enter agent role: Python developer

Step 2: WHAT does this agent do?
> Main task: Write clean Python code
> Can do #1: Write functions
> Can do #2: Add tests
> Can do #3: Document code

Step 3: HOW should the agent work?
Style: 1. Professional 2. Casual 3. Technical 4. Educational
> Choose: 3

Step 4: OUTPUT format?
Format: 1. Text 2. Code 3. List 4. Report
> Choose: 2

Step 5: TEST your agent
> Test prompt: Write a hello world function
> Success: Function works with docstring

✅ Done! AGENTS.md created!
```

## Use Example Templates

```bash
# List all examples
python examples.py

# View specific example
python examples.py code_reviewer

# Save example as AGENTS.md
python examples.py save api_developer
```

## Available Examples

- **code_reviewer** - Reviews code for quality
- **api_developer** - Creates REST APIs
- **doc_writer** - Writes documentation
- **bug_hunter** - Finds bugs
- **data_analyst** - Analyzes data

## Tips

1. **Start simple** - You can always enhance later
2. **Use examples** - They guide you at each step
3. **Test immediately** - Validate with your test prompt
4. **Keep it under 20 lines** - Simple is better

## With AI Enhancement (Optional)

If you have API keys configured:

```bash
# The builder will ask if you want AI enhancement
> Use AI to enhance this? [y/N]: y
```

## Output Files

- `AGENTS.md` - Your agent instructions
- `AGENTS_config.json` - Settings (for reuse)

## Next Steps

1. Copy `AGENTS.md` to your repo root
2. AI agents will automatically use it
3. Test with any AI coding assistant

---

**Remember:** 3 minutes to a working agent! 🎯