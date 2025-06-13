"""Utilities for meta-level reflection and adaptation."""


class MetaReflection:
    """Provide data analysis and summarization utilities."""

    def _dict_depth(self, mapping: dict, level: int = 1) -> int:
        """Return the depth of nested dictionaries."""
        sub_levels = [
            self._dict_depth(v, level + 1)
            for v in mapping.values()
            if isinstance(v, dict)
        ]
        return max(sub_levels, default=level)

    def analyze(self, data: object) -> dict:
        """Analyze ``data`` and return reflection details.

        Parameters
        ----------
        data:
            Any Python object to reflect upon.

        Returns
        -------
        dict
            Dictionary containing a representation, type name, length of the
            stringified data, and a basic summary when possible. Numeric values
            are classified, and dictionaries report nesting depth.
        """
        summary = None
        if isinstance(data, (list, tuple, set)):
            summary = f"contains {len(data)} items"
        elif isinstance(data, dict):
            depth = self._dict_depth(data)
            summary = f"mapping with {len(data)} keys (depth {depth})"
        elif isinstance(data, (int, float)):
            kind = "integer" if isinstance(data, int) else "float"
            summary = f"{kind} value {data}"
        elif isinstance(data, str):
            summary = f"{min(len(data), 20)} chars preview: {data[:20]}"

        return {
            "repr": repr(data),
            "type": type(data).__name__,
            "length": len(str(data)),
            "summary": summary,
        }
