from pathlib import Path
import sys

import nanogui as ng

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import render_svg_file


class SvgScreen(ng.Screen):
    def __init__(self):
        super().__init__(size=(720, 540), caption="External SVG - NanoGUI + LunaSVG")
        window = ng.Window(self, "SVG loaded from an external file")
        window.set_layout(ng.GroupLayout())

        svg_path = Path(__file__).parent / "assets" / "sample.svg"
        pixels = render_svg_file(str(svg_path))
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
