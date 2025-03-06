import cv2 # Importing opencv
import numpy as np # Importing numpy
import time 

# Images path
img_input_path = "Image/image_input_small.png" # Image input Path
img_output_path = "Image/pinguim.png" # Image output Path

# Load Images
img_input = cv2.imread(img_input_path)
img_output = cv2.imread(img_output_path)

# Transform into grayscale
img_input_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY) # convert input to gray
img_output_gray  = cv2.cvtColor(img_output, cv2. COLOR_BGR2GRAY) # convert output to gray


"""
 Uncomment if you want to print the Image with gray mode and opens it 

cv2.imshow("gray_", img_input_gray)
cv2.imshow("gray_banana", img_output_gray)
cv2.waitKey(0)
"""

# Define the grid size (e.g., 4 columns x 3 rows)
grid_cols = 50  # Number of columns
grid_rows = 30  # Number of rows

initial_time = time.time()
# Get image dimensions from rows(height) and columns(width)
img_height, img_width = img_input_gray.shape[:2] #e.g 119 (rows) and 64(columns)

mosaic_width = img_width * grid_cols  # e.g 32 * 40 = 1280
mosaic_height = img_height * grid_rows  # e.g 32 * 30 = 960
mosaic = np.zeros((mosaic_height, mosaic_width), dtype=np.uint8) # e.g the image dimension will be 714x1600 

# Tile the image into the grid
for row in range(grid_rows):
    for col in range(grid_cols):
        # Calculate offsets
        y_start = row * img_height
        y_end = y_start + img_height
        x_start = col * img_width
        x_end = x_start + img_width
        
        # Paste the image into the mosaic
        mosaic[y_start:y_end, x_start:x_end] = img_input_gray


print("--- %s seconds ---" % (time.time() - initial_time))

img_output_gray = cv2.resize(img_output_gray,(1280,960))
mosaic = cv2.resize(mosaic,(1280,960))
final_img = cv2.addWeighted(mosaic,0.5,img_output_gray,0.7,0)

# Display
cv2.imshow("Tiled Image Grid", mosaic)
cv2.imshow("Merged Images", final_img)
cv2.waitKey(0)
cv2.imwrite("matrix_intermedium.png", mosaic)

