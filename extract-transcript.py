import subprocess
import os

def download_subtitles(video_url, language='fr'):
    """
    Télécharge les sous-titres d'une vidéo YouTube en utilisant yt-dlp
    """
    try:
        # Configuration de la commande yt-dlp
        command = [
            'yt-dlp',
            '--skip-download',  # Ne pas télécharger la vidéo
            '--sub-lang', language,  # Langue des sous-titres
            '--write-auto-sub',  # Télécharger les sous-titres auto-générés si nécessaire
            video_url
        ]
        
        # Exécution de la commande
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Vérification si la commande a réussi
        if result.returncode != 0:
            print("Erreur lors du téléchargement des sous-titres:")
            print(result.stderr)
            return None
            
        # Recherche du fichier VTT généré
        # yt-dlp génère généralement un fichier avec un pattern spécifique
        vtt_files = [f for f in os.listdir('.') if f.endswith('.vtt')]
        if not vtt_files:
            print("Aucun fichier VTT trouvé")
            return None
            
        return vtt_files[0]  # Retourne le nom du fichier VTT
        
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")
        return None

def extract_transcript_from_vtt(vtt_content):
    # La fonction précédente d'extraction du transcript
    lines = vtt_content.split('\n')
    transcript_lines = []
    previous_line = None
    
    for line in lines:
        if (not '-->' in line and 
            line.strip() and 
            not line.startswith('WEBVTT') and 
            not ':' in line and 
            not line.strip().startswith('align')):
            
            cleaned_line = ''
            skip_content = False
            
            for char in line:
                if char == '<':
                    skip_content = True
                elif char == '>':
                    skip_content = False
                elif not skip_content:
                    cleaned_line += char
            
            cleaned_line = cleaned_line.strip()
            
            if cleaned_line and cleaned_line != previous_line:
                transcript_lines.append(cleaned_line)
                previous_line = cleaned_line
    
    return ' '.join(transcript_lines)

def process_video_transcript(video_url, language='fr'):
    """
    Fonction principale qui combine le téléchargement et l'extraction
    """
    # Téléchargement des sous-titres
    vtt_filename = download_subtitles(video_url, language)
    
    if not vtt_filename:
        return None
        
    try:
        # Lecture du fichier VTT
        with open(vtt_filename, 'r', encoding='utf-8') as file:
            vtt_content = file.read()
        
        # Extraction du transcript
        transcript = extract_transcript_from_vtt(vtt_content)
        
        # Nettoyage : suppression du fichier VTT
        os.remove(vtt_filename)
        
        return transcript
        
    except Exception as e:
        print(f"Erreur lors du traitement du fichier VTT: {str(e)}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=aPLpx0HrNmY"  # Remplace par l'URL de ta vidéo
    transcript = process_video_transcript(video_url)
    
    if transcript:
        print("Transcript extrait :")
        print(transcript)
        
        # Optionnel : sauvegarder dans un fichier texte
        with open('transcript.txt', 'w', encoding='utf-8') as f:
            f.write(transcript)