TEMPLATE_SCHEMA = {
    "type": "object",
    "required": ["name", "version", "files"],
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "string"},
        "files": {
            "type": "object",
            "additionalProperties": {"type": "string"}
        }
    }
}
