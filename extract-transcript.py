import subprocess
import os

def download_subtitles(video_url, language='fr'):
    """
    Télécharge les sous-titres d'une vidéo YouTube en utilisant yt-dlp
    """
    try:
        command = [
            'yt-dlp',
            '--skip-download',
            '--sub-lang', language,
            '--write-auto-sub',
            '--convert-subs', 'vtt',
            video_url
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Erreur lors du téléchargement des sous-titres:")
            print(result.stderr)
            return None
            
        vtt_files = [f for f in os.listdir('.') if f.endswith('.vtt')]
        if not vtt_files:
            print("Aucun fichier VTT trouvé")
            return None
            
        return vtt_files[0]
        
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")
        return None

def extract_transcript_from_vtt(vtt_content):
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
    vtt_filename = download_subtitles(video_url, language)
    
    if not vtt_filename:
        return None
        
    try:
        with open(vtt_filename, 'r', encoding='utf-8') as file:
            vtt_content = file.read()
        
        transcript = extract_transcript_from_vtt(vtt_content)
        
        os.remove(vtt_filename)
        
        return transcript
        
    except Exception as e:
        print(f"Erreur lors du traitement du fichier VTT: {str(e)}")
        if os.path.exists(vtt_filename):
            os.remove(vtt_filename)
        return None

def main():
    # Demande de l'URL à l'utilisateur
    print("Veuillez entrer l'URL de la vidéo YouTube :")
    video_url = input().strip()
    
    # Demande de la langue à l'utilisateur
    print("Veuillez entrer le code de la langue souhaitée (fr, en, es, etc.) :")
    language = input().strip()
    
    # Traitement
    transcript = process_video_transcript(video_url, language)
    
    if transcript:
        # Création du nom de fichier de sortie
        output_filename = f"transcript_{language}.txt"
        
        # Sauvegarde dans un fichier
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(transcript)
        
        print(f"\nLe transcript a été sauvegardé dans le fichier : {output_filename}")
    else:
        print("\nUne erreur s'est produite lors de l'extraction du transcript.")

if __name__ == "__main__":
    main()