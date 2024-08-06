from fasttext import load_model
from fasttext.FastText import _FastText  # type: ignore
from huggingface_hub import hf_hub_download

from server.config import Config
from server.features.types.languages import Languages


class LanguageDetector:
    """
    Summary
    -------
    a static class for the Language Detector

    Methods
    -------
    load() -> None
        load the model

    detect(text: str) -> Languages
        detect the language of the input text
    """

    model: _FastText

    @classmethod
    def load(cls):
        """
        Summary
        -------
        download and load the model
        """
        #model_path = hf_hub_download(Config.language_detector_model_name, 'model.bin')
        model_path = Config.translator_model_name
        cls.model: _FastText = load_model(model_path)

    @classmethod
    def detect(cls, text: str) -> Languages:
        """
        Summary
        -------
        detect the language of the input text

        Parameters
        ----------
        text (str) : the input to detect the language of

        Returns
        -------
        language (Languages) : the detected language
        """
        return cls.model.predict(text, k=5)[0][0][9:]  # type: ignore
