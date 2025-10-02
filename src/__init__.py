# Upstream: https://github.com/kuuuube/kanjigrid
# AnkiWeb:  https://ankiweb.net/shared/info/1610304449

import sys
import pathlib


def is_running_as_addon() -> bool:
    return pathlib.Path(__file__).parent.parent.name == "addons21"


if __name__ != "__main__" and "pytest" not in sys.modules and is_running_as_addon():
    from aqt import mw

    from . import kanjigrid
    # Save a reference to the toolkit onto the mw, preventing garbage collection of PyQt objects
    if mw:
        mw.kanjigrid = kanjigrid.KanjiGrid(mw)
else:
    print("This is an addon for the Anki spaced repetition learning system and cannot be run directly.")  # noqa: T201
    print("Please download Anki from <https://apps.ankiweb.net/>")  # noqa: T201
