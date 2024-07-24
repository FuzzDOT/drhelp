import torch
from PIL import Image
import torchvision.models as models
import torchvision.transforms as T

class PreProcessing:
    """
    Class for preprocessing images using a specified model.

    Args:
        model_name (str): The name of the model to use for preprocessing. Default is 'resnet'.

    Attributes:
        model: The pretrained model used for feature extraction.
        preprocess: A series of image transformations applied to input images.

    Methods:
        load_model: Loads the specified model.
        preprocess_image: Preprocesses an image by applying transformations.
        extract_features: Extracts features from an image using the pretrained model.
    """

    def __init__(self, model_name='resnet'):
        self.model = self.load_model(model_name)
        self.preprocess = T.Compose([
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
    
    def load_model(self, model_name):
        """
        Loads the specified model.

        Args:
            model_name (str): The name of the model to load.

        Returns:
            model: The pretrained model.
        """
        if model_name == 'resnet':
            model = models.resnet50(pretrained=True)
        elif model_name == 'efficientnet':
            model = models.efficientnet_b0(pretrained=True)
        else:
            raise ValueError("Unsupported model name. Use 'resnet' or 'efficientnet'.")
        model.eval()
        return model
    
    def preprocess_image(self, image_path):
        """
        Preprocesses an image by applying transformations.

        Args:
            image_path (str): The path to the image file.

        Returns:
            image_tensor: The preprocessed image tensor.
        """
        image = Image.open(image_path).convert("RGB")
        image_tensor = self.preprocess(image)
        return image_tensor
    
    def extract_features(self, image_path):
        """
        Extracts features from an image using the pretrained model.

        Args:
            image_path (str): The path to the image file.

        Returns:
            features: The extracted features.
        """
        image_tensor = self.preprocess_image(image_path).unsqueeze(0)
        with torch.no_grad():
            features = self.model(image_tensor)
        return features