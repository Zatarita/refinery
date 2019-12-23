from refinery.util import get_cwd
from mozzarilla.editor_constants import *
from pathlib import Path

REFINERYLIB_DIR = get_cwd(__file__)

REFINERY_ICON_PATH = Path(REFINERYLIB_DIR, "refinery.ico")
if not REFINERY_ICON_PATH.is_file():
    REFINERY_ICON_PATH = Path(REFINERYLIB_DIR, "icons", "refinery.ico")
if not REFINERY_ICON_PATH.is_file():
    REFINERY_ICON_PATH = Path(WORKING_DIR, "refinery.ico")
if not REFINERY_ICON_PATH.is_file():
    REFINERY_ICON_PATH = Path(WORKING_DIR, "icons", "refinery.ico")
if not REFINERY_ICON_PATH.is_file():
    REFINERY_ICON_PATH = ""

REFINERY_BITMAP_PATH = Path(REFINERYLIB_DIR, "refinery.png")
if not REFINERY_BITMAP_PATH.is_file():
    REFINERY_BITMAP_PATH = Path(REFINERYLIB_DIR, "icons", "refinery.png")
if not REFINERY_BITMAP_PATH.is_file():
    REFINERY_BITMAP_PATH = Path(WORKING_DIR, "refinery.png")
if not REFINERY_BITMAP_PATH.is_file():
    REFINERY_BITMAP_PATH = Path(WORKING_DIR, "icons", "refinery.png")
if not REFINERY_BITMAP_PATH.is_file():
    REFINERY_BITMAP_PATH = ""


# not for export
del Path
del get_cwd
