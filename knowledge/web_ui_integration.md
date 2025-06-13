# Web UI Integration

This guide outlines how a future web interface could communicate with the
Eidos REST API and event bus. Consult `templates.md` for code patterns and
`recursive_patterns.md` for the recursive philosophy that shapes these
interfaces. Terminology matches entries in `glossary_reference.md`.

## REST API

Endpoints expose core functionality of `EidosCore` and associated agents.
All JSON responses follow the structure defined in the Function Template.

- `GET /memories` – return the current memory list.
- `POST /experience` – add a new experience; body contains a JSON string.
- `POST /recurse` – trigger a recursion cycle; returns updated memories.
- `GET /events` – retrieve recent event bus messages for the UI.

### Example Schema
```json
{
  "memories": ["string or insight"],
  "status": "ok"
}
```

## Event Bus

The event bus distributes changes to subscribed components. A typical
implementation uses a publish/subscribe model. Events include:

- `memory-added` – emitted after `POST /experience`.
- `recurse-complete` – emitted after `POST /recurse`.
- `ui-command` – messages from the UI requesting background actions.

Consumers connect via WebSocket or HTTP long polling. Message formats are
JSON dictionaries adhering to the templates in `templates.md`.

## Web UI Flow

1. UI sends `POST /experience` to store a user input.
2. UI optionally calls `POST /recurse` to append reflections.
3. UI listens on the event bus for updates like `recurse-complete`.
4. UI fetches `GET /memories` to display the latest state.

This design keeps the UI stateless and pushes all recursion logic into the
API layer, enabling modular growth as documented throughout the knowledge
base.
