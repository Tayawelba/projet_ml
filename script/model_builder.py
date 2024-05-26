from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.applications import EfficientNetB0
import configuration as config

def build_model(image_size, num_classes=3):
    base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(*image_size, 3))
    base_model.trainable = False
    
    model = models.Sequential()
    model.add(base_model)
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))
    
    model.compile(optimizer=optimizers.Adam(learning_rate=config.LEARNING_RATE),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model
