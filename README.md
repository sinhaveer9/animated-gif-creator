# Animated GIF Creator

## Overview

Animated GIF Creator is a Python project I developed to explore image processing and learn how different Python libraries can work together to automate a task.

The program takes static images, resizes them to a consistent resolution, and combines them into a continuously looping animated GIF. Through this project, I wanted to understand how images can be processed programmatically rather than edited manually.

## Technologies Used

- **Python** — Used to write the program and control the image-processing workflow.
- **Pillow (PIL)** — Opens, converts, and resizes input images.
- **NumPy** — Converts processed images into numerical arrays.
- **imageio** — Combines the image frames and saves the final animated GIF.

## Key Features

- Processes multiple static images using a Python loop.
- Resizes images to a consistent resolution of 500 × 500 pixels.
- Converts input images into RGB format.
- Uses NumPy arrays to prepare images for GIF generation.
- Combines the processed images into a continuously looping GIF.
- Allows input filenames and image dimensions to be changed in the source code.

## Sample Output

The following animation was generated using the Python script.

![Animated GIF created using Python](neon.gif)

## How It Works

The program starts with a list of image filenames and a target image resolution. It then uses a for loop to open each image, convert it into RGB format, and resize it to 500 × 500 pixels.

Each processed image is converted into a NumPy array and added to a list. Finally, imageio combines these arrays into an animated GIF named `neon.gif`.

This approach automates the process of preparing and combining image frames, making it easier to generate an animation without manually editing each image.

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/sinhaveer9/animated-gif-creator.git
```

### 2. Open the project directory

```bash
cd animated-gif-creator
```

### 3. Install the required libraries

```bash
python3 -m pip install -r requirements.txt
```

### 4. Prepare the input images

Place `Neon1.jpg` and `Neon2.jpg` in the same directory as `create_gif.py`.

### 5. Run the program

```bash
python3 create_gif.py
```

The program creates an animated GIF named `neon.gif` in the project directory.

## What I Learned

This project helped me develop a better understanding of Python programming and image processing.

I learned how to work with external Python libraries, manipulate image dimensions, convert images into arrays, and use loops to automate repetitive operations.

One of the most valuable parts of this project was understanding how different libraries can contribute to a single program. Pillow handles image preparation, NumPy provides a way to represent image data, and imageio creates the final animation.

Working on this project also gave me more confidence in exploring Python libraries and applying programming concepts to practical tasks.

## Author
**Veer Sinha**
