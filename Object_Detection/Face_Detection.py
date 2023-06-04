import cv2
import numpy as np
import streamlit as st

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def draw_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

def main():
    st.title("Face Detection App")
    st.write("Upload an image and let the app detect faces!")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = np.array(cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1))
        st.image(image, channels="BGR", caption="Original Image", use_column_width=True)

        if st.button("Detect Faces"):
            st.write("Detecting faces...")
            faces = detect_faces(image)
            if len(faces) == 0:
                st.warning("No faces detected!")
            else:
                image_with_faces = draw_faces(image.copy(), faces)
                st.image(image_with_faces, channels="BGR", caption="Image with Faces", use_column_width=True)
                st.success(f"Detected {len(faces)} face(s) in the image!")

if __name__ == "__main__":
    main()
