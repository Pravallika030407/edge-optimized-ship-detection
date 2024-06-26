# -*- coding: utf-8 -*-
"""ship_port.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YL1914JnUozu3FAJmkQMg9KV9RgBbpAM
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# Pip install method (recommended)
# %pip install ultralytics
!pip install ultralytics

!pip install squarify

# Commented out IPython magic to ensure Python compatibility.
# Importing the required libraries
from ultralytics import YOLO
# import squarify
import matplotlib.pyplot as plt
import cv2
import os
import random
import pandas as pd
import matplotlib.image as mpimg
import seaborn as sns

sns.set_style('darkgrid')

# %matplotlib inline

# Define the paths to the images and labels directories
train_images = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/train/images"
train_labels = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/train/labels"

test_images = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/test/images"
test_labels = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/test/labels"

val_images = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/valid/images"
val_labels = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/valid/labels"

# Get a list of all the image files in the training images directory
image_files = os.listdir(train_images)

# Choose 16 random image files from the list
random_images = random.sample(image_files, 16)

# Set up the plot
fig, axs = plt.subplots(4, 4, figsize=(16, 16))

# Loop over the random images and plot the object detections
for i, image_file in enumerate(random_images):
    row = i // 4
    col = i % 4

    # Load the image
    image_path = os.path.join(train_images, image_file)
    image = cv2.imread(image_path)

    # Load the labels for this image
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(train_labels, label_file)
    with open(label_path, "r") as f:
        labels = f.read().strip().split("\n")

    # Loop over the labels and plot the object detections
    # Loop over the labels and plot the object detections
    for label in labels:
        if len(label.split()) != 5:
            continue
        class_id, x_center, y_center, width, height = map(float, label.split())
        x_min = int((x_center - width/2) * image.shape[1])
        y_min = int((y_center - height/2) * image.shape[0])
        x_max = int((x_center + width/2) * image.shape[1])
        y_max = int((y_center + height/2) * image.shape[0])
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)


    # Show the image with the object detections
    axs[row, col].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[row, col].axis('off')

plt.show()

import os
import cv2
import random
import matplotlib.pyplot as plt

# Define the paths to the images and labels directories
train_images = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/train/images"
train_labels = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/train/labels"

# Get a list of all the image files in the training images directory
image_files = os.listdir(train_images)

# Choose 16 random image files from the list
random_images = random.sample(image_files, 16)



# Set up the plot
fig, axs = plt.subplots(4, 4, figsize=(16, 16))

# Loop over the random images and plot the object detections
for i, image_file in enumerate(random_images):
    row = i // 4
    col = i % 4

    # Load the image
    image_path = os.path.join(train_images, image_file)
    image = cv2.imread(image_path)

    # Load the labels for this image
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(train_labels, label_file)
    with open(label_path, "r") as f:
        lines = f.readlines()

    # Loop over the labels and plot the object detections
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])

        # Calculate bounding box coordinates
        image_height, image_width, _ = image.shape
        x_min = int((x_center - width / 2) * image_width)
        y_min = int((y_center - height / 2) * image_height)
        x_max = int((x_center + width / 2) * image_width)
        y_max = int((y_center + height / 2) * image_height)

        # Draw bounding box
        color = (0, 255, 0)  # Default color for now
        if class_id == 1:
            color = (0, 0, 255)  # Red color for class 1
        elif class_id == 2:
            color = (255, 0, 0)  # Blue color for class 2

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 3)

    # Show the image with the object detections
    axs[row, col].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[row, col].axis('on')

plt.show()

import os
import cv2
import random
import matplotlib.pyplot as plt

# Define the paths to the images and labels directories
train_images_dir = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/train/images"
train_labels_dir = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/train/labels"
test_images_dir = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/test/images"
test_labels_dir = "/content/drive/MyDrive/Ship Port1.v1i.yolov8/test/labels"

# Get a list of all the image files in the training images directory
train_image_files = os.listdir(train_images_dir)
test_image_files = os.listdir(test_images_dir)

# Construct the full paths to the label files corresponding to each image
train_label_files = [os.path.join(train_labels_dir, os.path.splitext(image_file)[0] + ".txt") for image_file in train_image_files]
test_label_files = [os.path.join(test_labels_dir, os.path.splitext(image_file)[0] + ".txt") for image_file in test_image_files]

# Choose 16 random image files from the training set
random_train_images = random.sample(train_image_files, 8)

# Choose 8 random image files from the test set
random_test_images = random.sample(test_image_files, 8)

# Set up the plot
fig, axs = plt.subplots(4, 4, figsize=(16, 16))

# Loop over the random training images and plot the object detections
for i, image_file in enumerate(random_train_images):
    row = i // 4
    col = i % 4

    # Load the image
    image_path = os.path.join(train_images_dir, image_file)
    image = cv2.imread(image_path)

    # Load the labels for this image
    label_path = train_label_files[i]
    with open(label_path, "r") as f:
        lines = f.readlines()

    # Define colors for different classes
    class_colors = {
        1: (0, 255, 0),  # Green for ships and ship ports
        2: (0, 0, 255)   # Red for containers
    }

    # Loop over the labels and plot the object detections
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])

        # Calculate bounding box coordinates
        image_height, image_width, _ = image.shape
        x_min = int((x_center - width / 2) * image_width)
        y_min = int((y_center - height / 2) * image_height)
        x_max = int((x_center + width / 2) * image_width)
        y_max = int((y_center + height / 2) * image_height)

        # Draw bounding box with class-specific color
        color = class_colors.get(class_id, (0, 0, 0))  # Default to black if class color is not defined
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 3)

    # Show the image with the object detections
    axs[row, col].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[row, col].axis('on')

# Loop over the random test images and plot the object detections
for i, image_file in enumerate(random_test_images, len(random_train_images)):
    row = i // 4
    col = i % 4

    # Load the image
    image_path = os.path.join(test_images_dir, image_file)
    image = cv2.imread(image_path)

    # Load the labels for this image
    label_path = test_label_files[i - len(random_train_images)]
    with open(label_path, "r") as f:
        lines = f.readlines()

    # Loop over the labels and plot the object detections
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])

        # Calculate bounding box coordinates
        image_height, image_width, _ = image.shape
        x_min = int((x_center - width / 2) * image_width)
        y_min = int((y_center - height / 2) * image_height)
        x_max = int((x_center + width / 2) * image_width)
        y_max = int((y_center + height / 2) * image_height)

        # Draw bounding box with class-specific color
        color = class_colors.get(class_id, (0, 0, 0))  # Default to black if class color is not defined
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 3)

    # Show the image with the object detections
    axs[row, col].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[row, col].axis('on')

plt.show()

image = cv2.imread("/content/drive/MyDrive/Ship Port1.v1i.yolov8/test/images/10_jpg.rf.ba22be578b860143148d4beebb11d20b.jpg")

# Get the size of the image
height, width, channels = image.shape
print(f"The image has dimensions {width}x{height} and {channels} channels.")

# Loading a pretrained model
model = YOLO('yolov8x.pt')

# Training the model
model.train(data = '/content/drive/MyDrive/Ship Port1.v1i.yolov8/data.yaml',
            epochs = 15,
            imgsz = height,
            seed = 42,
            batch = 8,
            workers = 4)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# read in the results.csv file as a pandas dataframe
df = pd.read_csv('/content/runs/detect/train/results.csv')
df.columns = df.columns.str.strip()

# create subplots using seaborn
fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(15, 15))

# plot the columns using seaborn
sns.lineplot(x='epoch', y='train/box_loss', data=df, ax=axs[0,0])
sns.lineplot(x='epoch', y='train/cls_loss', data=df, ax=axs[0,1])
sns.lineplot(x='epoch', y='train/dfl_loss', data=df, ax=axs[1,0])
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, ax=axs[1,1])
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, ax=axs[2,0])
sns.lineplot(x='epoch', y='metrics/mAP50(B)', data=df, ax=axs[2,1])
sns.lineplot(x='epoch', y='metrics/mAP50-95(B)', data=df, ax=axs[3,0])
sns.lineplot(x='epoch', y='val/box_loss', data=df, ax=axs[3,1])
sns.lineplot(x='epoch', y='val/cls_loss', data=df, ax=axs[4,0])
sns.lineplot(x='epoch', y='val/dfl_loss', data=df, ax=axs[4,1])

# set titles and axis labels for each subplot
axs[0,0].set(title='Train Box Loss')
axs[0,1].set(title='Train Class Loss')
axs[1,0].set(title='Train DFL Loss')
axs[1,1].set(title='Metrics Precision (B)')
axs[2,0].set(title='Metrics Recall (B)')
axs[2,1].set(title='Metrics mAP50 (B)')
axs[3,0].set(title='Metrics mAP50-95 (B)')
axs[3,1].set(title='Validation Box Loss')
axs[4,0].set(title='Validation Class Loss')
axs[4,1].set(title='Validation DFL Loss')

# add suptitle and subheader
plt.suptitle('Training Metrics and Loss', fontsize=24)

# adjust top margin to make space for suptitle
plt.subplots_adjust(top=0.8)

# adjust spacing between subplots
plt.tight_layout()

plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# Loading the best performing model
model = YOLO('/content/drive/MyDrive/best v8 .pt')

# Evaluating the model on the test dataset
metrics = model.val(conf = 0.25, split = 'test')

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# Create the barplot
ax = sns.barplot(x=['mAP50-95', 'mAP50', 'mAP75'], y=[metrics.box.map, metrics.box.map50, metrics.box.map75])

# Set the title and axis labels
ax.set_title('YOLO Evaluation Metrics')
ax.set_xlabel('Metric')
ax.set_ylabel('Value')

# Set the figure size
fig = plt.gcf()
fig.set_size_inches(8, 6)

# Add the values on top of the bars
for p in ax.patches:
    ax.annotate('{:.3f}'.format(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

# Show the plot
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# Reading the confusion matrix image file
img = mpimg.imread('/content/runs/detect/train/confusion_matrix.png')

# Plotting the confusion matrix image
fig, ax = plt.subplots(figsize = (15, 15))

ax.imshow(img)
ax.axis('off');

def ship_detect(img):

    # Pass the image through the detection model and get the result
    detect_result = model(img)

    # Plot the detections
    detect_img = detect_result[0].plot()

    # Convert the image to RGB format
    detect_img = cv2.cvtColor(detect_img, cv2.COLOR_BGR2RGB)

    return detect_img

import random

# Define the directory where the custom images are stored
custom_image_dir = '/content/drive/MyDrive/Ship Port1.v1i.yolov8/test/images'

# Get the list of image files in the directory
image_files = os.listdir(custom_image_dir)

# Select 16 random images from the list
selected_images = random.sample(image_files, 16)

# Create a figure with subplots for each image
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(15, 15))

# Iterate over the selected images and plot each one
for i, img_file in enumerate(selected_images):

    # Compute the row and column index of the current subplot
    row_idx = i // 4
    col_idx = i % 4

    # Load the current image and run object detection
    img_path = os.path.join(custom_image_dir, img_file)
    detect_img = ship_detect(img_path)

    # Plot the current image on the appropriate subplot
    axes[row_idx, col_idx].imshow(detect_img)
    axes[row_idx, col_idx].axis('off')

# Adjust the spacing between the subplots
plt.subplots_adjust(wspace=0.05, hspace=0.05)

# Create subplots with proper layout
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))

# Plot validation metrics
sns.lineplot(x='epoch', y='val/box_loss', data=metrics_df, ax=axs[0], label='Validation Box Loss')
sns.lineplot(x='epoch', y='val/cls_loss', data=metrics_df, ax=axs[1], label='Validation Class Loss')

# Set titles and axis labels with improved font properties
axs[0].set_title('Validation Box Loss', fontsize=14, fontweight='bold')
axs[1].set_title('Validation Class Loss', fontsize=14, fontweight='bold')

# Add suptitle and adjust top margin
plt.suptitle('Validation Metrics', fontsize=24)
plt.subplots_adjust(top=0.9)

# Show the plot
plt.show()

import tensorflow as tf

# Assuming 'model' is your TensorFlow model object
model.save('ship_port_detection_model')  # Save the entire model

# To save only the model weights
#model.save_weights('ship_detection_weights.h5')

# Remove leading spaces from column names
df.columns = df.columns.str.strip()

# Plot the training and validation metrics
plt.figure(figsize=(10, 6))
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Training Precision')
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Validation Precision')
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Training Recall')
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Validation Recall')

plt.title('Training and Validation Metrics')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend()
plt.show()

# Remove leading spaces from column names
df.columns = df.columns.str.strip()

# Plot the training and validation metrics
plt.figure(figsize=(10, 6))

# Plot training precision with a dashed line
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Training Precision', linestyle='--')

# Plot validation precision with a solid line
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Validation Precision', linestyle='-')

# Plot training recall with a dashed line
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Training Recall', linestyle='--')

# Plot validation recall with a solid line
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Validation Recall', linestyle='-')

plt.title('Training and Validation Metrics')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend()
plt.show()

# Read the results.csv file as a pandas DataFrame
df = pd.read_csv('/content/runs/detect/train/results.csv')
df.columns = df.columns.str.strip()

# Plotting the training and validation precision
plt.figure(figsize=(10, 6))
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Training Precision')
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Training Recall')
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Validation Precision')
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Validation Recall')

plt.title('Training and Validation Metrics')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend()
plt.show()

# Read the results.csv file as a pandas DataFrame
df = pd.read_csv('/content/runs/detect/train/results.csv')
df.columns = df.columns.str.strip()

# Plotting the training and validation metrics
plt.figure(figsize=(10, 6))

# Plot training precision
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Training Precision', linestyle='--')

# Plot training recall
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Training Recall', linestyle='-')

# Plot validation precision
sns.lineplot(x='epoch', y='metrics/precision(B)', data=df, label='Validation Precision', linestyle='-')

# Plot validation recall
sns.lineplot(x='epoch', y='metrics/recall(B)', data=df, label='Validation Recall', linestyle='--')

plt.title('Training and Validation Metrics')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend()
plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/pp.jpg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Display the sample image with bounding boxes drawn around detected objects
    result.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/drive/MyDrive/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/ps.jpg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/img1.jpeg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/img2.jpeg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/pp.jpeg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/img1.jpeg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/pp.jpg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/ps.jpg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/detect.jpg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load your trained YOLOv8 model
model = YOLO('/content/runs/detect/train/weights/best.pt')

# Load the sample image from your PC
sample_image_path = '/content/drive/MyDrive/detect_1.jpg'
sample_image = sample_image_path

# Perform object detection on the sample image
results = model(sample_image)

# Iterate over the results to access predictions for each image
for result in results:
    # Print the detected classes and confidence scores for the current image
    print(result.probs)

    # Save the annotated image to a file
    result.save("annotated_image.jpg")

    # Load and display the annotated image using matplotlib
    annotated_image = plt.imread("annotated_image.jpg")
    plt.imshow(annotated_image)
    plt.axis("off")
    plt.show()

model.save('yolov8')

# Creating the gradio interface for the model
!pip install gradio --upgrade

import gradio as gr

input_image = gr.Image(label="Input Image")
output_image = gr.Image(label="Processed Image")

# Create the Gradio interface with a clear title and informative error message
interface = gr.Interface(
    fn=ship_detect,
    inputs=input_image,
    outputs=output_image,
    title="Ship Port Detection",
    description="This interface is currently under development. It is used to identify the ships and ports in the images.")

# Launch the interface
interface.launch(share=True)

