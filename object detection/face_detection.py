import cv2
import streamlit as st

# Function to detect faces in an image
def detect_faces(image):
    # Load the Haar cascade xml file for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return faces

# Main function
def main():
    # Set app title
    st.title("Face Detection App")
    
    # Upload image file
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read the image file
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        
        # Detect faces in the image
        faces = detect_faces(image)
        
        # Display the original image
        st.image(image, channels="BGR")
        
        # Display the number of faces detected
        st.write(f"Number of faces detected: {len(faces)}")
        
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the annotated image
        st.image(image, channels="BGR")

# Run the app
if __name__ == "__main__":
    main()
