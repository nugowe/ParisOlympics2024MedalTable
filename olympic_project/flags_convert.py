from PIL import Image
import potrace
import numpy as np

def png_to_svg(png_path, svg_path):
    # Load PNG image
    image = Image.open(png_path).convert('1')  # Convert to binary image (black & white)
    
    # Convert image to numpy array
    bitmap = np.array(image)
    
    # Create potrace bitmap
    potrace_bitmap = potrace.Bitmap(bitmap)
    path = potrace_bitmap.trace()
    
    # Convert path to SVG
    svg = path.to_svg()
    
    # Save SVG to file
    with open(svg_path, 'w') as f:
        f.write(svg)

# Example usage
png_to_svg('/home/nosa2k/MYPROJECTS/DJANGO/ParisOlympics2024MedalTable/olympic_project/static/images/hong_kong.png', '/home/nosa2k/MYPROJECTS/DJANGO/ParisOlympics2024MedalTable/olympic_project/static/images/HongKong.svg')

