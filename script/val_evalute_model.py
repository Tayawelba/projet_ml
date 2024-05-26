import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import configuration as config

# Charger le modèle
model = load_model(config.MODEL_SAVE_PATH)

# Générer les données de validation
datagen = ImageDataGenerator()
val_generator = datagen.flow_from_directory(config.VAL_DIR,
                                            target_size=config.IMAGE_SIZE,
                                            batch_size=config.BATCH_SIZE,
                                            shuffle=False)

# Prédictions
predictions = model.predict(val_generator)
predicted_labels = np.argmax(predictions, axis=1)
true_labels = val_generator.classes

# Matrice de confusion
cm = confusion_matrix(true_labels, predicted_labels)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=val_generator.class_indices.keys(), yticklabels=val_generator.class_indices.keys())
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Rapport de classification
print("Classification Report:\n", classification_report(true_labels, predicted_labels, target_names=val_generator.class_indices.keys()))
