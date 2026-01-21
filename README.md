# PyFrame
## Beginner Friendly Terminal Graphics Engine
### Description
PyFrame is a graphics engine that renders live frames to a terminal. The engine is build for beginners and experts alike to use with minimal implimentation. Everything needed to build a game, demo, frame, or even livesteam is included in a single script designed for maximum portability and ease of use.
### Usage
PyFrame supports a variety of potential use cases:
- Terminal based games
- Graphing
- Live data display
- RTSP
- Heatmaps
- Colorized Single Frames

Anything that can be represented with pixels is supported. PyFrame grants tools to take arbitrary data and transform it into live rendering to a terminal.

## Setup
The only software needed is Engine.py and the Python interpreter. To begin, simply download the script. The code defines a "frame" as defined by input parameters. On run, the script prompts for width, height, and framerate in order to define a canvas. In real implimentations, these may be hard coded values. Once a canvas is defined, the script begins to run the "simulationOn" loop until it is broken. All active rendering logic is to be included in that loop. Three main functions are given to render to the canvas:
### update_render
- this function updates any given pixel on the canvas with any arbitrary color. It's input parameters are an x coordinate, y coordinate, and a [r,g,b] tuple defining the color of the pixel.
### reverse_render
- the canvas is fundamentally a 1 dimentional array divided into slices to form a 2D frame. reverse_render gives the 2D coordinates of the array from any 1D index. It's input parameter is a single index integer.
### line
- this function draws a line between any two coordinates with any arbitrary color. It's input parameters are x1, y1, x2, y2, and an [r,g,b] tuple. 
