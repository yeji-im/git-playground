from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.message import render_message


def test_render_message_normal():
    assert render_message("Yeji") == "Hello, Yeji!"


# def test_render_message_trims():
#     assert render_message("  Yeji  ") == "Hello, Yeji!"


def test_render_message_empty():
    assert render_message("") == "Hello, anonymous!"
