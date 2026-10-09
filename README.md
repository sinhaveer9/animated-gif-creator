# Animated GIF Creator

### A Python-Based Image Processing Project

## Overview

The Animated GIF Creator is a Python project I developed to explore image processing and understand how different Python libraries can work together to automate a task.

The program takes static images, resizes them to a consistent resolution, and combines them into a continuously looping animated GIF. I used this project to apply my knowledge of Python programming to a practical task while gaining experience with external libraries and image manipulation.

## Technologies Used

- **Python:** Used to develop the program and manage the image-processing workflow.
- **Pillow (PIL):** Used to open images, convert them into RGB format, and resize them.
- **NumPy:** Used to convert processed images into arrays.
- **imageio:** Used to combine the processed images and generate the final animated GIF.

## Key Features

- Processes multiple images through an automated workflow.
- Resizes input images to a uniform resolution of 500 × 500 pixels.
- Converts images into RGB format for consistent processing.
- Uses NumPy arrays to prepare images for GIF generation.
- Combines individual images into a continuously looping GIF.
- Allows image dimensions and input filenames to be modified directly in the Python script.

## How the Program Works

The program begins by defining a list of image filenames and a target resolution.

Using a `for` loop, it opens each image with Pillow, converts it into RGB format, and resizes it to the specified dimensions. Each processed image is then converted into a NumPy array and stored in a list.

Finally, the program uses imageio to combine the processed images into a single animated GIF, which is saved as `neon.gif`.

## Installation and Usage

**1. Clone the repository**

```bash
git clone https://github.com/sinhaveer9/animated-gif-creator.git
```

**2. Open the project directory**

```bash
cd animated-gif-creator
```

**3. Install the required Python libraries**

```bash
python3 -m pip install imageio pillow numpy
```

**4. Add the input images**

Place `Neon1.jpg` and `Neon2.jpg` in the project directory, alongside `create_gif.py`.

**5. Run the program**

```bash
python3 create_gif.py
```

The program creates an animated GIF named `neon.gif` in the project directory.

## What I Learned

Developing this project helped me understand how Python can be used for more than basic calculations and terminal programs.

I gained practical experience working with external libraries, manipulating image dimensions, converting images into numerical arrays, and using loops to automate repetitive operations.

One of the main things I learned was how different libraries can be combined to complete a single task. Pillow handles image preparation, NumPy represents the processed images as arrays, and imageio generates
This project also helped me become more comfortable reading library documentation and understanding how individual parts of a program work together.

Author
Veer Sinha
GitHub: sinhaveer9
