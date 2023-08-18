
# Image Conversion App using Streamlit

The **Image Conversion App** is a web application developed using Streamlit, designed to facilitate various image conversions in a user-friendly manner. The app enables users to upload their images and choose from different conversion options, such as grayscale, black and white conversion, and image resizing. This repository provides the code and resources needed to run the app.

## Features

- **Introduction**: The app begins with a welcoming title and an introductory message, explaining its functionality.

- **Image Upload**: Users can upload image files in JPG, JPEG, or PNG formats using the provided file uploader.

- **Conversion Options**: Users can select from the following conversion options:
  - Grayscale Conversion: Converts the image to grayscale.
  - Black and White Conversion: Converts the image to black and white using a specified threshold.
  - Resize to 1/2 Size: Resizes the image to half of its original dimensions.
  - Resize to 1/4 Size: Resizes the image to one-fourth of its original dimensions.

- **Interactive Threshold Slider**: For the black and white conversion, users can adjust the threshold level using an interactive slider.

- **Image Display**: The app displays the converted images with appropriate captions, offering an easy-to-understand visual representation of the conversion results.

## How to Use

1. **Prerequisites**: Make sure you have Python and the required packages installed. You can install the required packages using the command:
   ```
   pip install -r requirements.txt
   ```

2. **Clone the Repository**: Clone this repository to your local machine using Git or by downloading the ZIP archive.

3. **Run the App**: Open a terminal/command prompt, navigate to the repository directory, and run the following command:
   ```
   streamlit run app.py
   ```

4. **Use the App**: Once the app is running, access it by opening a web browser and navigating to the provided URL. Upload an image and select the desired conversion options.

5. **Interact with the UI**: Play with the conversion options, sliders, and checkboxes to observe the real-time image conversions and their visual representation.

## Customization

Feel free to customize and extend the app according to your preferences and needs:

- Modify the UI layout and styling to match your design preferences.
- Add additional image processing functionalities to expand the app's capabilities.
- Enhance error handling and user guidance for a smoother user experience.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## Credits

This project was created with the help of the following technologies and resources:

- [Streamlit](https://www.streamlit.io/): A Python library for creating interactive web applications.
- [NumPy](https://numpy.org/): A fundamental package for scientific computing with Python.
- [OpenCV](https://opencv.org/): An open-source computer vision and machine learning software library.

## License

This project is licensed under the [MIT License](LICENSE).



**Note**: This readme provides a general overview of the Image Conversion App using Streamlit. Make sure to adapt any paths, configurations, or instructions to match your specific environment and needs.
