import json
from pathlib import Path

template_schema = json.load(
    open(Path(__file__).parent / "template.schema.json")
)
