noisy-farm
==============================

A farm animal sound classifier

This toy project holds the backend logic and ML model to classify farm animals sound using a pre-trained TensorFlow model (YAMNet) as audio feature extractor and transfer leraning. Model performace has not been optimized. 



Project Organization
------------

    │ 
    ├── README.md          <- The top-level README.
    │
    │
    ├── models             <- Trained and serialized models.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description.
    │
    │
    ├── reports            
    │   └── figures        <- Generated plots and figures.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── inference.py   <- Script to run inference with the model created. Holds SoundClassifier class
    │   │
    │   ├── main.py       <- Contain the code to run a REST API 
    │   │
    │   ├── config.py     <- Contain static parameters
    │   │
    │   ├── yamnet.py     <- Contain YAMNet model
    │   ├── features.py   <- Contain code for feature creation for the original YAMNet model
    │   ├── params.py     <- Contain parametes to run YAMNet model
    │
    ├── Dockerfile.lambda <- Dockerfile to create a prod container to deploy in AWS Lambda functionS
    │
    └── Dockerfile            <- Dockerfile to create a dev container


--------
Project inspired by

<p align="center">
  <img src="https://pictures.abebooks.com/isbn/9781852920494-uk.jpg"  width="199" height="200" title="hover text">
</p>