# Bytefall

Bytefall is a Matrix-style digital rain animation made with Python and Pygame. It opens in fullscreen mode and fills the display with falling binary streams, glowing green trails, bright leading characters, and occasional white flashes.

## Features

- Fullscreen digital rain animation built with Pygame
- Randomized columns, fall speeds, and trail lengths for an organic effect
- Binary `0` and `1` character streams
- Bright green leading characters with darker green trailing characters
- Rare white glyph flashes for extra visual variation
- Smooth 30 FPS animation loop
- Simple keyboard controls for exiting

## Requirements

- Python 3.10 or newer
- Pygame

## Installation

Clone the repository and install the Python dependency:

```bash
git clone https://github.com/your-username/bytefall.git
cd bytefall
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.\.venv\Scripts\activate
```

## Usage

Run the animation with:

```bash
python matrix.py
```

Bytefall launches fullscreen. Press `Esc` or `Q` to exit.

## Controls

- `Esc`: exit the animation
- `Q`: exit the animation

## Customization

Basic visual settings live near the top of `matrix.py`:

- `FONT_SIZE` controls character size and column spacing.
- `CHARACTERS` controls which symbols appear in the rain.
- `GREEN`, `BRIGHT_GREEN`, `WHITE`, and `BLACK` control the color palette.
- The random `speeds` range controls how fast columns fall.
- The random `length` range controls trail length.
- `clock.tick(30)` controls the target frame rate.

After changing settings, run `python matrix.py` again to see the result.

## License

Bytefall is released under the MIT License. See [LICENSE](LICENSE) for details.
