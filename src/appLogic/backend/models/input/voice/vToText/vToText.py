import librosa
import numpy as np
from pydub import AudioSegment
import whisper

class VToText:
    """
    Class representing a voice-to-text converter.

    Attributes:
        model_name (str): The name of the model to use for transcription.

    Methods:
        __init__(self, model_name='base'): Initializes a VToText instance.
        load_audio(self, file_path): Loads an audio file from the given file path.
        extract_features(self, audio): Extracts features from the audio.
        voice_to_text(self, file_path): Converts voice to text using the loaded model.
        validate_transcription(self, transcription, reference): Validates the transcription against a reference text.
    """

    def __init__(self, model_name='base'):
        self.model = whisper.load_model(model_name)

    def load_audio(self, file_path):
        """
        Loads an audio file from the given file path.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            audio (AudioSegment): The loaded audio.
        """
        audio = AudioSegment.from_file(file_path)
        return audio

    def extract_features(self, audio):
        """
        Extracts features from the audio.

        Args:
            audio (AudioSegment or str): The audio to extract features from. Can be an AudioSegment object or a file path as a string.

        Returns:
            mfccs (numpy.ndarray): The Mel-frequency cepstral coefficients.
            spectrogram (numpy.ndarray): The spectrogram of the audio.
        """
        if isinstance(audio, str):
            audio = AudioSegment.from_file(audio)
            
        samples = np.array(audio.get_array_of_samples())
        sample_rate = audio.frame_rate
        mfccs = librosa.feature.mfcc(y=samples.astype(float), sr=sample_rate, n_mfcc=13)
        spectrogram = librosa.feature.melspectrogram(y=samples.astype(float), sr=sample_rate)
        return mfccs, spectrogram

    def voice_to_text(self, file_path):
        """
        Converts voice to text using the loaded model.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            result['text'] (str): The transcribed text.
        """
        result = self.model.transcribe(file_path)
        return result['text']

    def validate_transcription(self, transcription, reference):
        """
        Validates the transcription against a reference text.

        Args:
            transcription (str): The transcribed text.
            reference (str): The reference text.

        Returns:
            bool: True if the transcription matches the reference, False otherwise.
        """
        return transcription.strip().lower() == reference.strip().lower()