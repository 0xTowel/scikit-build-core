from __future__ import annotations

from typing import Any

__all__ = ["dynamic_metadata"]


def dynamic_metadata(
    pyproject_dict: dict[str, Any]
) -> dict[str, str | dict[str, str | None]]:
    from hatch_fancy_pypi_readme._builder import build_text
    from hatch_fancy_pypi_readme._config import load_and_validate_config

    config = load_and_validate_config(
        pyproject_dict["tool"]["hatch"]["metadata"]["hooks"]["fancy-pypi-readme"]
    )

    return {
        "readme": {
            "content-type": config.content_type,
            "text": build_text(config.fragments, config.substitutions),
        }
    }