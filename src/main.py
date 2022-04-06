import sys
import os

from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
import uvicorn
from pydantic import BaseModel, validator
import logging
from typing import Optional, List
from src.inference import SoundClassifier



logger = logging.getLogger(__name__)

class HealthCheck(BaseModel):
    """
    HealthCheck.
    """
    message: Optional[str] = 'OK'

class PredictResponse(BaseModel):
    """
    Represents the result of a prediction
    """
    category: Optional[str] = None


app = FastAPI()


@app.on_event('startup')
def load_model():
    """
    Loads the model prior to the first request.
    """
    if not hasattr(app.state, 'model'):
        configure_logging()
        logger.info('Loading models...')
        app.state.model = SoundClassifier()

def configure_logging(logging_level=logging.INFO):
    """
    Configures logging for the application.
    """
    root = logging.getLogger()
    root.handlers.clear()
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    root.setLevel(logging_level)
    root.addHandler(stream_handler)



@app.post("/sound/prediction")
async def get_sound_prediction(file: UploadFile = File(...)):
    """
    Predicts the category of the audio file contained in the request.
    :param file: The file-like object containing the audio data to predict.
    :return: The prediction results.
    """
    logger.info('Processing request.')
    results =  app.state.model.predict(file.file)
    logger.info('Transaction complete.')
    return {"Animal": results}

@app.get('/health')
def test():
    """
    Can be called by load balancers as a health check.
    """
    return HealthCheck()

# To use in AWS lambda
# handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)