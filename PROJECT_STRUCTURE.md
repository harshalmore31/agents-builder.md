# Project Structure

```
agents-builder.md/
│
├── agent-builder/              # Main package directory
│   ├── simple_builder.py       # Core builder with 5-part structure
│   ├── examples.py             # Example agent templates
│   ├── build.py                # Quick start entry point
│   ├── quick_start.md          # 1-minute guide
│   ├── SIMPLE_AGENT_STANDARD_V1.md  # The standard specification
│   └── archive/                # Old implementations (gitignored)
│
├── README.md                   # Project overview and quick start
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
├── requirements.txt            # Python dependencies
├── setup.py                    # Installation script
├── PROJECT_STRUCTURE.md        # This file
└── .gitignore                  # Git ignore rules
```

## Core Files

### `simple_builder.py`
The main builder with three classes:
- `SimpleAgent` - 5-part structure with examples
- `AIRefiner` - Optional AI enhancement
- `AgentsBuilder` - Main orchestrator

### `examples.py`
Ready-to-use templates:
- code_reviewer
- api_developer
- doc_writer
- bug_hunter
- data_analyst

### `build.py`
One-command entry: `python build.py`

## Usage

### Install
```bash
pip install -r requirements.txt
```

### Run
```bash
# Interactive builder
python agent-builder/build.py

# View examples
python agent-builder/examples.py

# Use template
python agent-builder/examples.py save code_reviewer
```

## Output

Creates two files:
- `AGENTS.md` - Agent instructions
- `AGENTS_config.json` - Reusable configuration

## Philosophy

> Simple beats complex. Working beats perfect. Clear beats clever.

The entire system is designed to create a working agent in 3 minutes.