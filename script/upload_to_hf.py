import os
from huggingface_hub import HfApi, HfFolder, Repository

def upload_model_to_hf():
    # Récupérer le token d'authentification de Hugging Face
    hf_token = os.getenv('HF_TOKEN')
    model_path = "model"
    repo_name = "tayawelba/examen_github"

    # Authentifier
    HfFolder.save_token(hf_token)
    api = HfApi()
    api.create_repo(repo_name, exist_ok=True)

    # Créer le dépôt localement
    repo = Repository(local_dir=model_path, clone_from=repo_name)

    # Ajouter tous les fichiers et les téléverser
    repo.git_add(auto_lfs_track=True)
    repo.git_commit("Upload trained model")
    repo.git_push()

if __name__ == '__main__':
    upload_model_to_hf()
