from flask import Flask, request
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import io

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle
model = MobileNetV2(weights="imagenet")

# Dictionnaire de catégories traduites en français
clothing_categories_fr = {
    "abaya": "abaya",
    "academic_gown": "robe académique",
    "apron": "tablier",
    "bathing_cap": "bonnet de bain",
    "bikini": "bikini",
    "bow_tie": "nœud papillon",
    "brassiere": "soutien-gorge",
    "cardigan": "cardigan",
    "cloak": "cape",
    "coat": "manteau",
    "cowboy_boot": "botte de cowboy",
    "cowboy_hat": "chapeau de cowboy",
    "crinoline": "crinoline",
    "diaper": "couche",
    "fur_coat": "manteau en fourrure",
    "gown": "robe",
    "hoopskirt": "jupon",
    "jean": "jean",
    "jersey": "maillot",
    "kimono": "kimono",
    "knee_pad": "genouillère",
    "lab_coat": "blouse de laboratoire",
    "maillot": "maillot",
    "miniskirt": "mini-jupe",
    "overskirt": "surjupe",
    "pajama": "pyjama",
    "poncho": "poncho",
    "sarong": "sarong",
    "suit": "costume",
    "sweatshirt": "sweatshirt",
    "swimming_trunks": "short de bain",
    "trench_coat": "trench",
    "vestment": "habit",
    "wool": "laine",
    "sock": "chaussette"
}

# Pré-traitement de l'image reçue
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

# Fonction de classification
def classify_image(image_bytes):
    img_preprocessed = preprocess_image(image_bytes)
    predictions = model.predict(img_preprocessed)
    decoded = decode_predictions(predictions, top=6)[0]  # Obtenez les 6 premières prédictions

    # Vérifier si l'un des 6 premiers labels correspond à un vêtement
    for _, label, score in decoded:
        if label in clothing_categories_fr:
            # Retourne la catégorie traduite en français
            return clothing_categories_fr[label]
    
    return "autres"  # Si aucun vêtement n'est trouvé parmi les 6 premiers labels

# Point de terminaison pour la classification
@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return "Erreur : aucune image fournie", 400
    
    image = request.files['image'].read()
    result = classify_image(image)
    return result  # Retourne directement la chaîne de caractères du label en français
