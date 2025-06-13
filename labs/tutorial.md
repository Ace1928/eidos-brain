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
`EidosCore` now accepts custom memory backends such as `VectorMemory` and `KnowledgeGraph`. The tutorial uses the default `VectorMemory` implementation.

