# Free Draw Bot

Free Draw Bot is a Python utility that automates drawing tasks by simulating mouse movements. It offers the flexibility to draw images or custom data files, with customizable settings for delay, drawing speed, offsets, and progress bar style.

## Features

- **Draw from Data File**: Draw images using custom data files containing coordinate points.
- **Draw from Image**: Generate custom data files from images and draw them.
- **Make Your Own Data File**: Manually mark points on the screen to create custom data files.
- **Preview**: Preview the drawing before executing.
- **Customizable Settings**: Adjust settings such as start delay, drawing speed, offsets, and progress bar style.

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/DankWhat/FreeDraw-Bot.git

```css

2. Navigate to the project directory:

```

cd free-draw-bot

```md

3. Install the required dependencies:

```
```py
pip install -r requirements.txt
```

## Draw from Image
bash
```bash
python main.py --draw-image
```
## Make Your Own Data File
```bash
python main.py --make-data
```
## Preview
```bash
python main.py --preview
```
## Customization
Adjust the settings in settings.json to customize the drawing experience:

start_delay: Delay before starting the drawing process (in seconds).
draw_speed: Speed of drawing (lower values for faster drawing).
x_offset: Horizontal offset for drawing.
y_offset: Vertical offset for drawing.
progress_bar_style: Style of the progress bar (1 for 100% done, 2 for [|||||||||||||||||]).
Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or submit a pull request.

License
This project is licensed under the GNU License.

