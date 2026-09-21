"""Shared helpers for the NanoGUI + LunaSVG examples."""

from __future__ import annotations

import numpy as np
import pylunasvg


def bitmap_to_rgba(bitmap) -> np.ndarray:
    """Convert a pylunasvg Bitmap into an owned HxWx4 uint8 array."""
    rgba = np.frombuffer(bitmap.data, dtype=np.uint8)
    expected = bitmap.width * bitmap.height * 4
    if rgba.size != expected:
        raise ValueError(
            f"Expected {expected} RGBA bytes, received {rgba.size}"
        )
    return rgba.reshape((bitmap.height, bitmap.width, 4)).copy()


def render_document(document: pylunasvg.Document) -> np.ndarray:
    """Render a LunaSVG document at its intrinsic size."""
    return bitmap_to_rgba(document.render())


def render_svg_string(svg: str) -> np.ndarray:
    return render_document(pylunasvg.Document.fromstring(svg))


def render_svg_file(filename: str) -> np.ndarray:
    return render_document(pylunasvg.Document.fromfile(filename))
