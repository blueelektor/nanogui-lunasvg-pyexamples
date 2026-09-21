# NanoGUI + LunaSVG Python examples

Python 예제로 NanoGUI 창에 LunaSVG가 렌더링한 SVG를 표시합니다.

- `embedded_svg/`: SVG 마크업을 Python 문자열에 내장
- `external_svg/`: 외부 `assets/sample.svg` 파일을 로드

## 요구 사항

- Python 3.9+
- OpenGL/GLFW 실행 환경
- [NanoGUI Python bindings](https://github.com/mitsuba-renderer/nanogui)
- [pylunasvg](https://pypi.org/project/pylunasvg/)
- NumPy

```bash
python -m pip install -r requirements.txt
```

> NanoGUI와 pylunasvg의 배포판/바인딩 버전에 따라 패키지 설치 방법이 달라질 수 있습니다. `nanogui` 모듈과 `pylunasvg` 모듈을 import할 수 있는 환경에서 실행하세요.

## 실행

```bash
python embedded_svg/example.py
python external_svg/example.py
```

각 예제는 LunaSVG `Document`를 RGBA NumPy 배열로 래스터라이즈한 뒤 NanoGUI `Texture`에 업로드하고 `ImageView`로 표시합니다.

## 구현 흐름

```text
SVG 문자열 또는 파일
        ↓
pylunasvg.Document
        ↓
Document.render() → RGBA bitmap
        ↓
NumPy uint8 (height, width, 4)
        ↓
nanogui.Texture.upload()
        ↓
nanogui.ImageView
```

원본 NanoGUI의 Python 바인딩은 `ImageView`와 `Texture.upload()`를 제공하지만 LunaSVG와의 직접적인 브리지는 제공하지 않습니다. 따라서 이 저장소에서는 두 라이브러리 사이를 RGBA NumPy 배열로 연결합니다.
