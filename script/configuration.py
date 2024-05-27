import os

# Répertoires des données
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
VAL_DIR = os.path.join(DATA_DIR, 'val')
TEST_DIR = os.path.join(DATA_DIR, 'test')

# Paramètres de traitement des données
IMAGE_SIZE = (229, 229)  # Exemple pour des images, ajustez selon vos besoins
BATCH_SIZE = 32

# Hyperparamètres pour l'entraînement du modèle
EPOCHS = 6
LEARNING_RATE = 0.001

# Chemin pour sauvegarder le modèle
MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'model', 'model_final.h5')

# Autres configurations pertinentes
RANDOM_SEED = 42
