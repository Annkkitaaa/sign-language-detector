import streamlit as st
import subprocess
import cv2
import time

def run_inference_classifier():
    try:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        subprocess.run(["python", "inference_classifier.py"])
    except Exception as e:
        st.error(f"Error running inference_classifier.py: {e}")

st.set_page_config(page_title="Sign Detection App", page_icon=":camera:")

st.title("Sign Detection App")

st.markdown("## Welcome to the Sign Detection App!")

st.write("This app allows you to run the `inference_classifier.py` file and classify gestures using your webcam.")

run_button = st.button("Run Inference Classifier")

if run_button:
    run_inference_classifier()
    st.success("Inference Classifier running!")

st.markdown("## Captured Image")
image_placeholder = st.empty()

with st.sidebar:
    st.markdown("## Instructions")
    st.info("Click the 'Run Inference Classifier' button to start classifying gestures using your webcam.")
    st.info("The captured image will be displayed in the main area.")
    st.info("Press 'q' to quit the webcam feed.")

    st.markdown("## About")
    st.write("This app was developed by [Your Name] as part of a sign detection project. The project uses computer vision and deep learning techniques to detect and classify gestures in real-time.")