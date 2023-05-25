
## Repository Contents

- map_maker.py: The main script that processes the image and identifies vertices.
- ur_map.png: The input image that the script processes.
- output.png: The output image annotated with the vertices found.

## Usage

1. Clone this repository to your local machine.
```bash
git clone https://github.com/ondals/map_creator.git
```
2. Make sure you have the necessary Python packages installed. You can install them using pip:
```bash
pip install opencv-python numpy
```
3. Design your map using a tool like PowerPoint, where you can draw different shapes to represent different areas of the map. 

4. After designing your map, simplify it as much as possible, using solid colors and simple shapes.

5. Save your map as an image file (PNG or JPEG). In PowerPoint, you can do this by going to "File" > "Save As" > and then select "PNG" or "JPEG" in the "Save as type" drop down menu.

6. Place the image file in the same directory as the Python script and update the `image_path` variable in the script with the name of your image file.

7. Run the script using Python3:
```bash
python3 map_maker.py
```
The script will print the coordinates of the vertices of each box it finds in the console. It also outputs an image, annotating the vertices on the map.

