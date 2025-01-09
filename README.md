# YouTube Video Transcript Extractor

Ce script Python permet d'extraire automatiquement la transcription textuelle d'une vidéo YouTube. Il combine l'utilisation de yt-dlp pour le téléchargement des sous-titres et un traitement Python personnalisé pour extraire le texte propre.

## Prérequis

- Python 3.x
- yt-dlp

Pour installer yt-dlp :

```bash
pip install yt-dlp
```

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers
2. Assurez-vous que yt-dlp est installé sur votre système
3. Placez le script Python dans votre environnement de travail

## Fonctionnement

Le script effectue les opérations suivantes :

1. Téléchargement des sous-titres de la vidéo YouTube au format VTT
2. Extraction du texte en supprimant :
   - Les métadonnées VTT
   - Les marqueurs de temps
   - Les balises de formatage
   - Les doublons de lignes consécutifs
3. Génération d'un transcript propre et continu
4. Suppression du fichier VTT temporaire

## Utilisation

### Utilisation basique

```python
video_url = "https://www.youtube.com/watch?v=XXXXXXXXXXX"
transcript = process_video_transcript(video_url)

if transcript:
    print(transcript)
```

### Spécifier une langue différente

```python
# Pour obtenir les sous-titres en anglais
transcript = process_video_transcript(video_url, language='en')
```

## Structure du code

Le script est composé de trois fonctions principales :

### download_subtitles(video_url, language)

Cette fonction gère le téléchargement des sous-titres via yt-dlp. Elle :

- Configure et exécute la commande yt-dlp
- Vérifie la réussite du téléchargement
- Retourne le nom du fichier VTT généré

### extract_transcript_from_vtt(vtt_content)

Cette fonction traite le fichier VTT pour en extraire le texte propre. Elle :

- Filtre les lignes non pertinentes
- Nettoie les balises et les métadonnées
- Élimine les doublons consécutifs
- Retourne un texte continu

### process_video_transcript(video_url, language)

C'est la fonction principale qui :

- Orchestre le processus complet
- Gère les erreurs potentielles
- Nettoie les fichiers temporaires
- Retourne le transcript final

## Options de sortie

Le script propose deux options de sortie :

1. Affichage console :

```python
print(transcript)
```

2. Sauvegarde dans un fichier :

```python
with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(transcript)
```

## Gestion des erreurs

Le script inclut une gestion robuste des erreurs pour :

- Les échecs de téléchargement de sous-titres
- Les problèmes de lecture de fichier
- Les erreurs de traitement du contenu
- Les problèmes d'encodage

Chaque erreur est capturée et génère un message explicatif approprié.

## Limitations

1. Dépendances externes :

   - Nécessite une connexion Internet
   - Dépend de l'installation correcte de yt-dlp

2. Limitations liées à YouTube :

   - Dépend de la disponibilité des sous-titres
   - Qualité limitée par les sous-titres d'origine

3. Limitations techniques :
   - Traite uniquement le format VTT
   - Ne gère pas les sous-titres intégrés à la vidéo

## Support des langues

Le script supporte toutes les langues disponibles sur YouTube. Pour spécifier une langue :

- Français : 'fr'
- Anglais : 'en'
- Espagnol : 'es'
- Allemand : 'de'
- etc.

Utilisez les codes de langue ISO standard à deux lettres.

## Bonnes pratiques

1. Toujours vérifier le retour de la fonction principale :

```python
transcript = process_video_transcript(video_url)
if transcript is None:
    print("Une erreur est survenue")
```

2. Gérer les fichiers temporaires :

- Le script nettoie automatiquement les fichiers VTT
- Vérifier régulièrement qu'aucun fichier temporaire ne reste

3. Respect des limites d'utilisation :

- Éviter les requêtes massives vers YouTube
- Respecter les conditions d'utilisation de la plateforme

## Contribution

Les contributions sont les bienvenues :

1. Fork du projet
2. Création d'une branche pour votre fonctionnalité
3. Commit de vos changements
4. Push vers la branche
5. Création d'une Pull Request

## Licence

MIT License

Copyright (c) 2025 Nicolas Declerck

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# yt-extractor
