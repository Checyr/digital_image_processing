import cv2 # Importing opencv

# Images path
img_input_path = "Image/image_input_small.png" # Image input Path
img_output_path = "Image/image_output_small.png" # Image output Path


# Load Images
img_input = cv2.imread(img_input_path)
img_output = cv2. imread(img_output_path)

# Transform into grayscale
img_input_gray = img_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY) # convert input to gray
img_output_gray = img_gray = cv2.cvtColor(img_output, cv2. COLOR_BGR2GRAY) # convert output to gray


# Load in grayscale mode
img_input_gray_mode = cv2.imread(img_input_path, 0)
img_output_gray_mode = cv2.imread(img_input_path, 0)

cv2.imshow("gray_", img_input_gray)
cv2.imshow("gray_banana", img_input_gray)
cv2.waitKey(0)