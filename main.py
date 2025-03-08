import cv2 # Importing opencv
import numpy as np # Importing numpy
import time

# Images path
img_input_path = "Image/image_input.png" # Image input Path
img_output_path = "Image/image_output.png" # Image output Path

# Load Images
img_input = cv2.imread(img_input_path)
img_output = cv2.imread(img_output_path)

# Transform into grayscale
img_input_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY) # convert input to gray
img_output_gray  = cv2.cvtColor(img_output, cv2. COLOR_BGR2GRAY) # convert output to gray

# Start Execution Time
initial_time = time.time()

def adjust_element_mean(img_input, target_mean_value):
    """
    Adjusts the mean of img_input to match target_mean_value
    while maintaining pixel values in [0, 255]
    """
    current = np.mean(img_input)
    
    # Create a copy to avoid modifying original
    adjusted = img_input.copy().astype(np.float32)
    
    while abs(target_mean_value - current) > 0.5:
        if target_mean_value > current:
            adjusted += (target_mean_value - current)
        else:
            adjusted -= 3
        
        # Clip values and recalculate mean
        adjusted = np.clip(adjusted, 0, 255)
        current = np.mean(adjusted)
    
    return adjusted.astype(np.uint8)

"""
Creates a photomosaic where:
- img_output_gray: guide image (H x W)
- img_input: tile image (N x M)
"""
H, W = img_output_gray.shape[:2]
N, M = img_input_gray.shape[:2]

# Initialize mosaic canvas
mosaic = np.zeros((H*N, W*M, 3), dtype=np.uint8) if img_input_gray.ndim == 3 else np.zeros((H*N, W*M), dtype=np.uint8)

for i in range(H):
    for j in range(W):
        # Get target mean from img_output_gray pixel
        target_mean = img_output_gray[i, j]
        
        # Adjust element image's mean
        adjusted_element = adjust_element_mean(img_input_gray, target_mean)
        
        # Calculate position in mosaic
        y_start = i * N
        y_end = (i + 1) * N
        x_start = j * M
        x_end = (j + 1) * M
        
        # Place adjusted element in mosaic
        mosaic[y_start:y_end, x_start:x_end] = adjusted_element

# print execution time
print("--- %s seconds ---" % (time.time() - initial_time))

cv2.imshow("photomosaic", mosaic)
cv2.waitKey(0)