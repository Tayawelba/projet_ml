import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_data_generators(train_dir, val_dir, test_dir, image_size, batch_size, seed):
    data_gen = ImageDataGenerator(validation_split=0.20)
    
    train_ds = data_gen.flow_from_directory(train_dir,
                                            class_mode="categorical",
                                            target_size=image_size,
                                            batch_size=batch_size,
                                            shuffle=True,
                                            subset='training',
                                            seed=seed)
    
    validation_ds = data_gen.flow_from_directory(train_dir,
                                                 class_mode="categorical",
                                                 target_size=image_size,
                                                 batch_size=batch_size,
                                                 shuffle=True,
                                                 subset='validation',
                                                 seed=seed)
    
    test_gen = ImageDataGenerator()
    test_ds = test_gen.flow_from_directory(test_dir,
                                           target_size=image_size,
                                           batch_size=batch_size,
                                           shuffle=False)
    
    return train_ds, validation_ds, test_ds
