import spacy

class PreProcess:
    """
    A class for preprocessing text using spaCy.

    Attributes:
        npm (spacy.Language): The spaCy language model.
        doc (spacy.Doc): The processed text document.

    Methods:
        process(text): Processes the input text.
        get_text(): Returns the processed text document.
    """

    def __init__(self):
        self.npm = spacy.load('en_core_web_trf')
        self.doc = ""

    def process(self, text):
        """
        Processes the input text.

        Args:
            text (str): The input text to be processed.
        """
        self.doc = self.npm(text)
    
    def get_text(self):
        """
        Returns the processed text document.

        Returns:
            spacy.Doc: The processed text document.
        """
        return self.doc
