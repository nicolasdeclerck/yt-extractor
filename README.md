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

## Utilisation

Lancez simplement le script et suivez les instructions :

```bash
python extract-transcript.py
```

Le script vous demandera :

1. L'URL de la vidéo YouTube
2. Le code de la langue souhaitée (fr, en, es, etc.)

À la fin de l'exécution, un fichier contenant le transcript sera créé dans le répertoire courant avec le nom `transcript_[langue].txt` (par exemple : `transcript_fr.txt`).

## Structure du code

Le script est composé de quatre fonctions principales :

### main()

Fonction principale qui :

- Gère l'interface utilisateur
- Collecte les entrées utilisateur (URL et langue)
- Orchestre le processus d'extraction
- Sauvegarde le résultat dans un fichier

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

Cette fonction :

- Orchestre le processus complet
- Gère les erreurs potentielles
- Nettoie les fichiers temporaires
- Retourne le transcript final

## Gestion des erreurs

Le script gère les erreurs suivantes :

- Échec du téléchargement des sous-titres
- Problèmes de lecture de fichier
- Erreurs de traitement du contenu
- Problèmes d'encodage

En cas d'erreur, un message explicatif est affiché à l'utilisateur.

## Limitations

1. Dépendances externes :

   - Nécessite une connexion Internet
   - Dépend de l'installation correcte de yt-dlp

2. Limitations liées à YouTube :
   - Dépend de la disponibilité des sous-titres
   - Qualité limitée par les sous-titres d'origine

## Support des langues

Le script supporte toutes les langues disponibles sur YouTube. Utilisez les codes de langue ISO standard à deux lettres :

- Français : 'fr'
- Anglais : 'en'
- Espagnol : 'es'
- Allemand : 'de'
- etc.

## Contribution

Les contributions sont les bienvenues :

1. Fork du projet
2. Création d'une branche pour votre fonctionnalité
3. Commit de vos changements
4. Push vers la branche
5. Création d'une Pull Request

## Licence

MIT License

Copyright (c) [année] [votre nom]

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
