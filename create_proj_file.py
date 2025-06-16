import os

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def create_emotion_project_structure():
    folders = [
        "emotion_recognition",
        "emotion_recognition/data/fer2013",
        "emotion_recognition/data/ck_plus",
        "emotion_recognition/models",
        "emotion_recognition/utils"
    ]

    files = {
        "emotion_recognition/train.py": "# Training script goes here\n",
        "emotion_recognition/predict_live.py": "# Live emotion prediction script\n",
        "emotion_recognition/utils/preprocess.py": "# Preprocessing utilities\n",
        "emotion_recognition/utils/labels.py": "EMOTIONS = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']\n",
        "emotion_recognition/requirements.txt": "tensorflow\nopencv-python\nnumpy\n",
        "emotion_recognition/README.md": "# Facial Emotion Recognition Project\n\nUsing CNN and VGG16 Transfer Learning.",
    }

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files
    for path, content in files.items():
        create_file(path, content)

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_emotion_project_structure()
