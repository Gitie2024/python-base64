import base64

# Remplacez par le chemin de votre fichier
image_path = "chrome_screenshot.jpg" 

with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Formatage prêt pour le navigateur
    data_uri = f"data:image/jpeg;base64,{encoded_string}"
    
    # Sauvegarde dans un fichier texte
    with open("image_base64.txt", "w") as text_file:
        text_file.write(data_uri)
        
    print("Le fichier Base64 a été généré avec succès !")