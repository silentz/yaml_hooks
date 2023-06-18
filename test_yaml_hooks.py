import io
from typing import Any, Dict, Union

import yaml

import yaml_hooks


class Tests:
    def dump_with_args(
        self,
        data: Any,
        before: Union[Dict[str, Any], None] = None,
        after: Union[Dict[str, Any], None] = None,
        style: Union[Dict[str, Any], None] = None,
    ) -> str:
        # run custom dumper with args and return result
        dumper = yaml_hooks.Dumper.spawn(
            before=before, after=after, style=style, delimiter="/"
        )
        buffer = io.StringIO(initial_value="")
        yaml.dump(data, buffer, dumper)
        buffer.seek(0)
        return buffer.getvalue()

    def test_before_global_keys(self) -> None:
        data = {"a": "1", "b": [1, 1, 1], "c": None, "d": True}
        result = self.dump_with_args(data)
        print(result)
