import unittest
from model_builder import build_model
from data_preprocessor import create_data_generators
import configuration as config

class TestModel(unittest.TestCase):
    def test_model_structure(self):
        model = build_model(config.IMAGE_SIZE)
        # Construire le modèle avec une entrée fictive pour obtenir output_shape
        model.build((None, *config.IMAGE_SIZE, 3))
        self.assertIsNotNone(model)
        self.assertEqual(model.output_shape[-1], 3)
    
    def test_data_generators(self):
        train_ds, val_ds, test_ds = create_data_generators(config.TRAIN_DIR, config.VAL_DIR, config.TEST_DIR, config.IMAGE_SIZE, config.BATCH_SIZE, config.RANDOM_SEED)
        self.assertIsNotNone(train_ds)
        self.assertIsNotNone(val_ds)
        self.assertIsNotNone(test_ds)
        
    def test_training(self):
        train_ds, val_ds, _ = create_data_generators(config.TRAIN_DIR, config.VAL_DIR, config.TEST_DIR, config.IMAGE_SIZE, config.BATCH_SIZE, config.RANDOM_SEED)
        model = build_model(config.IMAGE_SIZE)
        history = model.fit(train_ds, epochs=1, validation_data=val_ds)
        self.assertGreater(len(history.history['loss']), 0)

if __name__ == '__main__':
    unittest.main()
