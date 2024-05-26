import os
import subprocess

# Définir les chemins des scripts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, '')
TRAIN_EVALUATE_MODEL_SCRIPT = os.path.join(SCRIPTS_DIR, 'train_evaluate_model.py')
TEST_EVALUATE_MODEL_SCRIPT = os.path.join(SCRIPTS_DIR, 'test_evalute_model.py')
VAL_EVALUATE_MODEL_SCRIPT = os.path.join(SCRIPTS_DIR, 'val_evalute_model.py')

# Fonction pour exécuter un script
def run_script(script_path):
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    print("1. Entraînement et évaluation du modèle")
    run_script(TRAIN_EVALUATE_MODEL_SCRIPT)
    
    print("2. Évaluation du modèle sur les données de test")
    run_script(TEST_EVALUATE_MODEL_SCRIPT)
    
    print("3. Évaluation du modèle sur les données de validation")
    run_script(VAL_EVALUATE_MODEL_SCRIPT)

if __name__ == '__main__':
    main()