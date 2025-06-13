# Interactive Tutorial

This guide walks you through the `tutorial_app.py` application, which demonstrates how `EidosCore` stores memories and generates insights.

## Running the Tutorial

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the application:
   ```bash
   python labs/tutorial_app.py
   ```
3. Use the prompts to add experiences, view memories, and trigger recursion cycles.

The tutorial shows how memories are reflected upon and expanded using `MetaReflection`.

## Exploring Further with `sandbox1.py`

The `sandbox1.py` script accepts command-line options for rapid experimentation:

```bash
python labs/sandbox1.py --initial "hello" --cycles 3
```

This runs three recursion cycles after seeding the core with the word "hello".

