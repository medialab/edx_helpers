Edx Video Transcripts
=====================

**Transcription pour les vidéos YouTube**
**Marche à suivre**

Partant du principe que vous disposez du sous-titrage de la vidéo au format srt.

Récupération du script python
-----------------------------
```bash
git clone https://github.com/edx/edx-tools/tree/master/captions
```

Conversion du fichier srt vers le sjson
---------------------------------------
```bash
cd edx-tools/captions/youtube_util
mv /path/to/your.srt your.srt
python srt_to_sjson.py your.srt
```

Le fichier your.srt.sjson sera alors créé dans ce même dossier.

Rattachement à la vidéo dans la plateforme EDX
----------------------------------------------
Renommez votre fichier sjon de la sorte:

    subs_YOUTUBEID.srt.sjon

Example
    
    subs_OEoXaMPEzfM.srt.sjson

Rendez vous ensuite sur Studio et uploadez pour votre cours le fichier sjon. Une fois avoir activé le transcript pour la vidéo YouTube (activé par défaut normalement), celui-ci sera automatiquement proposé à l'utilisateur.