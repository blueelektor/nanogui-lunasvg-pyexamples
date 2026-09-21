from pathlib import Path
import sys

import nanogui as ng

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import render_svg_string


SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="640" height="420" viewBox="0 0 640 420">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#182848"/>
      <stop offset="1" stop-color="#4b6cb7"/>
    </linearGradient>
  </defs>
  <rect width="640" height="420" rx="28" fill="url(#sky)"/>
  <circle cx="320" cy="190" r="105" fill="#ffd166"/>
  <path d="M90 335 C180 250 245 315 320 270 S470 230 550 335 Z" fill="#06d6a0"/>
  <text x="320" y="385" text-anchor="middle" fill="white"
        font-family="sans-serif" font-size="28">Embedded SVG</text>
</svg>
"""


class SvgScreen(ng.Screen):
    def __init__(self):
        super().__init__(size=(720, 540), caption="Embedded SVG - NanoGUI + LunaSVG")
        window = ng.Window(self, "SVG embedded in Python")
        window.set_layout(ng.GroupLayout())

        pixels = render_svg_string(SVG)
        texture = ng.Texture(
            pixel_format=ng.Texture.PixelFormat.RGBA,
            component_format=ng.Texture.ComponentFormat.UInt8,
            size=[pixels.shape[1], pixels.shape[0]],
            min_interpolation_mode=ng.Texture.InterpolationMode.Linear,
            mag_interpolation_mode=ng.Texture.InterpolationMode.Linear,
        )
        texture.upload(pixels)

        view = ng.ImageView(window)
        view.set_image(texture)
        view.set_size((640, 420))
        view.center()
        self.perform_layout()


def main():
    ng.init()
    try:
        screen = SvgScreen()
        screen.set_visible(True)
        ng.run()
    finally:
        ng.shutdown()


if __name__ == "__main__":
    main()
