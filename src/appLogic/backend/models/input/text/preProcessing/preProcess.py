import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

nltk.download('stopwords')
nltk.download('punkt')

class TextPreprocess:
    """
    A class for text preprocessing.

    Attributes:
        stop_words (set): A set of stopwords in English.
        nlp (spacy.Language): An instance of the Spacy language model.

    Methods:
        clean_text(text): Cleans the input text by converting it to lowercase and removing non-alphanumeric characters.
        tokenize_text(text): Tokenizes the input text and removes stopwords.
        extract_features(text): Extracts keywords and entities from the input text using Spacy.
        validate_features(extracted_features, benchmark_data): Validates the extracted features against benchmark data.
    """

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.nlp = spacy.load("en_core_web_trf")
    
    def clean_text(self, text):
        """
        Cleans the input text by converting it to lowercase and removing non-alphanumeric characters.

        Args:
            text (str): The input text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        text = text.lower()
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        return text
    
    def tokenize_text(self, text):
        """
        Tokenizes the input text, converts it to lowercase, removes non-alphanumeric characters, and filters out stopwords.

        Args:
        text (str): The input text to be tokenized.

        Returns:
            list: A list of tokenized words after removing stopwords and non-alphanumeric characters.
        """
        # Convert text to lowercase
        text = text.lower()
        # Tokenize the text
        tokens = word_tokenize(text)
        # Remove non-alphanumeric characters and stopwords
        tokens = [word for word in tokens if word.isalpha() and word not in self.stop_words]
        return tokens
    
    def extract_features(self, text):
        """
        Extracts keywords and entities from the input text using Spacy.

        Args:
            text (str): The input text to extract features from.

        Returns:
            tuple: A tuple containing a list of keywords and a list of entities.
        """
        doc = self.nlp(text)
        keywords = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return keywords, entities
    
    def validate_features(self, extracted_features, benchmark_data):
        """
        Validates the extracted features against benchmark data.

        Args:
            extracted_features (tuple): A tuple containing a list of keywords and a list of entities.
            benchmark_data (dict): A dictionary containing benchmark data with "keywords" and "entities" keys.

        Returns:
            bool: True if the extracted features are valid, False otherwise.
        """
        keywords, entities = extracted_features
        keyword_validation = all(keyword in benchmark_data["keywords"] for keyword in keywords)
        entity_validation = all(entity in benchmark_data["entities"] for entity in entities)
        return keyword_validation and entity_validation