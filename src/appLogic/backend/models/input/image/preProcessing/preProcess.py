import cv2
import numpy as np

class ImagePreprocessor:
    """
    A class that provides methods for preprocessing images.

    Args:
        target_width (int): The desired width of the image after resizing.
        target_height (int): The desired height of the image after resizing.
    """

    def __init__(self, target_width, target_height):
        self.target_width = target_width
        self.target_height = target_height
        self.final_image = None

    def load_image(self, image_path):
        """
        Loads an image from the specified path.

        Args:
            image_path (str): The path to the image file.

        Raises:
            FileNotFoundError: If the image file is not found at the specified path.

        Returns:
            numpy.ndarray: The loaded image.
        """
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at {image_path}")
        return image

    def resize_image(self, image):
        """
        Resizes the given image to the target width and height.

        Args:
            image (numpy.ndarray): The image to be resized.

        Returns:
            numpy.ndarray: The resized image.
        """
        resized_image = cv2.resize(image, (self.target_width, self.target_height))
        return resized_image

    def normalize_image(self, image):
        """
        Normalizes the pixel values of the given image to the range [0, 1].

        Args:
            image (numpy.ndarray): The image to be normalized.

        Returns:
            numpy.ndarray: The normalized image.
        """
        normalized_image = image / 255.0
        return normalized_image

    def preprocess_image(self, image_path):
        """
        Preprocesses the image at the specified path.

        Args:
            image_path (str): The path to the image file.
        """
        image = self.load_image(image_path)
        resized_image = self.resize_image(image)
        normalized_image = self.normalize_image(resized_image)
        self.final_image = normalized_image

    def get_final_image(self):
        """
        Returns the final preprocessed image.

        Returns:
            numpy.ndarray: The final preprocessed image.
        """
        return self.final_image
