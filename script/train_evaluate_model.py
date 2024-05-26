import os
import configuration as config
from data_preprocessor import create_data_generators
from model_builder import build_model
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

def main():
    train_ds, val_ds, test_ds = create_data_generators(config.TRAIN_DIR, config.VAL_DIR, config.TEST_DIR, config.IMAGE_SIZE, config.BATCH_SIZE, config.RANDOM_SEED)
    
    model = build_model(config.IMAGE_SIZE)
    
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, min_delta=0.001, verbose=1)
    
    history = model.fit(train_ds, epochs=config.EPOCHS, validation_data=val_ds, callbacks=[early_stopping])
    
    model.save(config.MODEL_SAVE_PATH)
    
    # Évaluer le modèle
    test_loss, test_acc = model.evaluate(test_ds)
    print(f'Test accuracy: {test_acc}')
    
    # Générer la documentation avec pydoc
    import pydoc

    # Créer le dossier 'doc' s'il n'existe pas
    doc_dir = 'doc'
    os.makedirs(doc_dir, exist_ok=True)

    # Générer la documentation pour chaque module et sauvegarder dans le dossier 'doc'
    modules = ['configuration', 'data_preprocessor', 'model_builder', 'train_evaluate_model']
    for module in modules:
        output_path = os.path.join(doc_dir, f'{module}.html')
        pydoc.writedoc(module)
        with open(f'{module}.html', 'r') as f:
            content = f.read()
        os.remove(f'{module}.html')
        with open(output_path, 'w') as f:
            f.write(content)

if __name__ == '__main__':
    main()
