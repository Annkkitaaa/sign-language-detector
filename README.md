# Sign Language Recognition with Machine Learning

This repository contains an implementation of a sign language recognition system using machine learning techniques. The system is designed to recognize hand gestures from video input and translate them into corresponding text.

## Overview

The sign language recognition system is built using Python and various libraries, including OpenCV, MediaPipe, and scikit-learn. The system follows these steps:

1. **Data Acquisition**: Images of hand gestures are collected using OpenCV.
2. **Data Preprocessing**: The collected images are preprocessed, including color space conversion and hand landmark detection using MediaPipe.
3. **Feature Extraction**: Relevant features, such as normalized hand landmark coordinates, are extracted from the preprocessed images.
4. **Model Training**: A Random Forest classifier is trained using the extracted features and corresponding gesture labels.
5. **Inference**: The trained model is used to recognize hand gestures from real-time video input, and the predicted gestures are displayed on the screen.

## Requirements

To run the sign language recognition system, you need to have the following dependencies installed:

- Python 3.x
- OpenCV
- MediaPipe
- scikit-learn
- NumPy

You can install the required Python packages using pip:

```
pip install opencv-python mediapipe scikit-learn numpy
```

## Usage

1. Clone this repository:

```
git clone https://github.com/your-username/sign-language-recognition.git
```

2. Navigate to the project directory:

```
cd sign-language-recognition
```

3. Run the data collection script to create the dataset:

```
python data_collection.py
```

4. Train the Random Forest model:

```
python train_model.py
```

5. Run the real-time recognition script:

```
python inference.py
```

The real-time recognition script will open a window displaying the video feed from your webcam. The system will detect hand gestures and display the recognized text on the screen.



## Acknowledgments

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [scikit-learn](https://scikit-learn.org/)

