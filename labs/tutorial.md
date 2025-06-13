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

### Memory Persistence

You can load or save a memory file when launching the tutorial:

```bash
python labs/tutorial_app.py --load-memory mem.txt --save-memory mem.txt
```

This preserves experiences between sessions using the helper functions
`load_memory` and `save_memory`.

The tutorial shows how memories are reflected upon and expanded using `MetaReflection`.

