# ODIN

**ODIN** (Optimized Dynamic Intelligent Network) est un assistant IA personnel inspiré de JARVIS. À terme, il doit comprendre les demandes en langage naturel, raisonner, coordonner plusieurs modèles d'IA et exécuter des tâches de manière autonome.

Aujourd'hui, ODIN est un assistant conversationnel multimodal : on peut lui écrire, lui parler ou lui envoyer une image depuis une interface web.

## Fonctionnalités

- **Conversation textuelle** : l'utilisateur pose ses questions dans un chat et ODIN répond en langage naturel.
- **Entrée vocale** : l'utilisateur peut enregistrer un message audio, transcrit en texte avant d'être envoyé au modèle.
- **Analyse d'images** : l'utilisateur peut joindre une image (JPG, JPEG ou PNG) à son message, et le modèle s'appuie dessus pour répondre.
- **Historique de conversation** : les échanges (texte et images) sont conservés pendant la session et renvoyés au modèle à chaque requête, ce qui lui permet de suivre le fil de la discussion.
- **Personnalité configurable** : le comportement et le ton de l'assistant sont définis dans `context.txt`, utilisé comme prompt système.

## Technologies

- **Python 3.11**
- **Streamlit** pour l'interface utilisateur
- **Groq** pour l'accès aux modèles :
  - `qwen/qwen3.8-27b` pour la génération des réponses et l'analyse d'images
  - `whisper-large-v3-turbo` pour la transcription audio
- **python-dotenv** pour le chargement de la clé API

## Structure du projet

```
.
├── llm_agent.py        # ConversationAgent : appels au modèle, transcription audio, historique
├── user_interface.py   # UserInterface : interface Streamlit (chat, audio, images)
├── context.txt         # Prompt système définissant la personnalité de l'assistant
├── requirements.txt    # Dépendances Python
└── README.md
```

## Installation

1. Cloner le dépôt puis créer et activer un environnement virtuel :

   ```bash
   python3.11 -m venv env
   source env/bin/activate
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Créer un fichier `.env` à la racine du projet avec sa clé API Groq :

   ```
   GROQ_KEY=ta_cle_groq
   ```

## Lancement

```bash
streamlit run user_interface.py
```

L'interface s'ouvre dans le navigateur. Il suffit ensuite d'écrire un message, d'enregistrer un audio ou de joindre une image.

## Limites actuelles

- L'historique n'est conservé que pendant la session Streamlit : il est perdu au rechargement de la page.
- ODIN ne peut que converser : il n'exécute pas encore d'actions.
