# Simple Agent Prompt Standard v1.0

> **One Line:** A simple 5-part structure to create any AI agent prompt in minutes.

## The 5 Essential Parts

### 1. WHO - Agent Identity
```yaml
ROLE: "What kind of expert is this agent?"
Example: "Python developer" or "Content writer" or "Data analyst"
```

### 2. WHAT - Agent Job
```yaml
MAIN_TASK: "What does this agent do?"
Example: "Write clean Python code" or "Analyze datasets" or "Create documentation"

CAN_DO: 
- List 3-5 things the agent can do
- Be specific and clear

CANNOT_DO:
- List any restrictions (optional)
- What to avoid
```

### 3. HOW - Working Style
```yaml
STYLE: Pick one: Professional | Casual | Technical | Educational
APPROACH: Pick one: Fast | Careful | Creative | By-the-book
```

### 4. OUTPUT - Result Format
```yaml
FORMAT: Pick one: Text | Code | List | Report | JSON
EXAMPLE: "Show a small example of what you want"
```

### 5. TEST - Validation
```yaml
TEST_PROMPT: "A real task to test if your agent works"
SUCCESS_LOOKS_LIKE: "What a good result contains"
```

---

## Real Example: Code Review Agent

```yaml
# Code Review Agent

WHO:
  ROLE: "Senior developer doing code reviews"

WHAT:
  MAIN_TASK: "Review code for bugs and improvements"
  CAN_DO:
    - Find bugs and security issues
    - Suggest better code patterns
    - Check code style
    - Explain problems clearly
  CANNOT_DO:
    - Rewrite entire codebase
    - Make architecture decisions

HOW:
  STYLE: Technical
  APPROACH: Careful

OUTPUT:
  FORMAT: List
  EXAMPLE: |
    ✅ Good: Clear variable names
    ⚠️ Issue: Missing error handling in line 23
    💡 Suggestion: Use list comprehension instead of loop

TEST:
  TEST_PROMPT: "Review this code: def add(a,b): return a+b"
  SUCCESS_LOOKS_LIKE: "Mentions missing type hints and docstring"
```

---

## Quick Start (3 Minutes)

### Step 1: Copy this template
```yaml
# [Your Agent Name]

WHO:
  ROLE: ""

WHAT:
  MAIN_TASK: ""
  CAN_DO:
    - 
    - 
    - 

HOW:
  STYLE: [Pick: Professional | Casual | Technical | Educational]
  APPROACH: [Pick: Fast | Careful | Creative | By-the-book]

OUTPUT:
  FORMAT: [Pick: Text | Code | List | Report | JSON]
  EXAMPLE: ""

TEST:
  TEST_PROMPT: ""
  SUCCESS_LOOKS_LIKE: ""
```

### Step 2: Fill it in (2 mins)
- One sentence per field
- Don't overthink it
- Use plain language

### Step 3: Test it (1 min)
- Try your TEST_PROMPT
- Check if output matches SUCCESS_LOOKS_LIKE
- Adjust if needed

---

## Common Agent Templates

### 🔧 Coding Agent
```yaml
WHO: 
  ROLE: "[Language] developer"
WHAT:
  MAIN_TASK: "Write [type] code"
  CAN_DO: [Write, Debug, Test, Document]
```

### 📝 Writing Agent
```yaml
WHO:
  ROLE: "[Type] writer"  
WHAT:
  MAIN_TASK: "Create [content type]"
  CAN_DO: [Write, Edit, Summarize, Expand]
```

### 🔍 Analysis Agent
```yaml
WHO:
  ROLE: "[Domain] analyst"
WHAT:
  MAIN_TASK: "Analyze [data type]"
  CAN_DO: [Analyze, Compare, Summarize, Report]
```

---

## Tips for Success

### ✅ DO:
- Keep it simple (under 20 lines)
- Use examples
- Test with real tasks
- Be specific about capabilities

### ❌ DON'T:
- Write essays
- Use complex jargon
- Skip testing
- Make it too generic

---

## Why This Works

1. **Simple** - Anyone can fill this out in 3 minutes
2. **Complete** - Covers all essential aspects
3. **Flexible** - Works for any type of agent
4. **Testable** - Built-in validation

---

## For AGENTS.md Files

Just add this at the top of your template:

```markdown
# AGENTS.md
> Instructions for AI agents working with this codebase

[Your filled template here]

## Additional Context
- Build command: `npm run build`
- Test command: `npm test`
- Main tech: React, TypeScript
```

---

## Next Steps

1. **Start Simple** - Use the 5-part structure
2. **Test Early** - Validate with your test prompt
3. **Iterate** - Refine based on results
4. **Share** - Save templates that work well

Remember: **A simple prompt that works is better than a complex one that confuses.**