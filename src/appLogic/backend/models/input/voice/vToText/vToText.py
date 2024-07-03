import whisper

class vToText:
    """
    This class represents a voice-to-text converter.

    Attributes:
        text (str): The converted text from audio.
        language (str): The detected language of the audio.

    Methods:
        __init__(): Initializes an instance of the vToText class.
        convert(audioFilePath): Converts the given audio file to text and detects the language.
        get_text(): Returns the converted text.
        get_language(): Returns the detected language.
    """

    def __init__(self):
        self.text = ""
        self.language = ""

    def convert(self, audioFilePath):
        """
        Converts the given audio file to text and detects the language.

        Args:
            audioFilePath (str): The path to the audio file.

        Returns:
            None
        """
        model = whisper.load_model("base")
        result = model.transcribe(audioFilePath)
        self.text = result["text"]
        self.language = result["language"]

    def get_text(self):
        """
        Returns the converted text.

        Returns:
            str: The converted text.
        """
        return self.text

    def get_language(self):
        """
        Returns the detected language.

        Returns:
            str: The detected language.
        """
        return self.language
