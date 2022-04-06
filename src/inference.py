import tensorflow as tf
import tensorflow_io as tfio
import numpy as np
import librosa

import src.params as yamnet_params
import src.yamnet as yamnet_model

import src.config as config

class SoundClassifier:
    """
    Classifies audio according to animal categories.
    """
    def __init__(self):
        """
        Prepares the model used by the application for use.
        """
        self.model = tf.saved_model.load(config.MODEL_PATH)

    # Utility functions for loading audio files and making sure the sample rate is correct.

    def _prepare_audio(self, file):
        """
        Prepares the audio for prediction.

        :param file: A wav file to prepare for prediction.

        :return: A processed tensor object.
        """
        data , sampling_rate = librosa.load(file,sr=None)
        data_tensor = tf.convert_to_tensor(data)
        data_tensor = tf.reshape(data_tensor,(data_tensor.shape[0],1))
        wav = tf.squeeze(data_tensor, axis=-1)
        sample_rate = tf.cast(sampling_rate, dtype=tf.int64)
        wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
        return wav

    def predict(self,file):
        """
        Predicts the category of an audio file.

        :param images: A file audio to classify.

        :return: An str with the predicted category.
        """
        wav = self._prepare_audio(file)
        serving_results = self.model.signatures['serving_default'](wav)
        animal = config.my_classes[tf.argmax(serving_results['classifier'])]

        return animal