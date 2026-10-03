#!/usr/bin/env python3
"""
setup_repo.py
Script d'initialisation et d'architecture pour le dépôt Republique6.
Génère l'arborescence, les configurations, le README.md, les dépendances et l'environnement.
"""

from pathlib import Path

# Constante pour éviter la collision avec les backticks Markdown
BT = chr(96) * 3

DIRECTORIES = [
    "docs",
    "docs/specifications",
    "docs/architecture",
    "sprints",
    "src",
    "src/agents",
    "src/kernel",
    "src/simulation",
]

README_CONTENT = f"""# VI.OS — Ma 6ᵉ République (Architecture Système & Réseau Souverain)

[![Status](https://img.shields.io/badge/Status-Alpha%20v6.0-cyan)](https://github.com/pascalranoroarijaona/Republique6)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Architecture](https://img.shields.io/badge/Architecture-Microkernel%20P2P-purple)](docs/architecture/)

Projet d'ingénierie open source visant à démontrer qu'une société humaine peut être formalisée à plus de **95 % sous forme de code informatique déterministe**.

---

## 🏛️️ Le Diagnostic : L'OS 1958 face au Monde de 2026

Notre société contemporaine est exploitée sur une architecture institutionnelle et constitutionnelle compilée en **1958**. Conçue dans l'urgence de la guerre d'Algérie pour une société industrielle centralisée, la Vᵉ République présente les caractéristiques d'un système d'exploitation obsolète :
* **Un compte `root` omnipotent :** Concentration monarchique des privilèges au sommet et commandes d'outrepassement non auditables (`sudo 49.3`, décrets d'urgence).
* **Le syndrome Windows 95 :** Empiler de nouvelles couches fiscales sur un modèle en déliquescence revient à essayer de patcher un système d'exploitation de 1995 pour faire tourner un cluster d'agents d'IA.
* **Fuites de mémoire & Dérive Cantillon :** L'émission monétaire par la dette irrigue le sommet avant la base, provoquant une captation asymétrique des actifs rares et des fuites hors-graphe non colmatées.

---

## ⚡ Les Trois Piliers Fondateurs

1. **Abstraction Informatique à 95+% :** Mathématiser l'allocation des flux (énergie, biens, monnaie, services) pour éliminer les latences bureaucratiques. Les **5 % restants** représentent l'arbitrage éthique et la délibération politique humaine incompressible.
2. **Architecture Micro-Noyau (Microkernel) :** Réduction du Ring-0 régalien au strict minimum (justice arbitrale, libertés fondamentales, défense). Déportation de la santé, de l'éducation et de l'énergie dans l'espace utilisateur Ring-3 selon le principe de subsidiarité territoriale.
3. **Souveraineté Cryptographique (PODs & ZKP) :** Fin des bases de données étatiques centralisées vulnérables aux fuites massives. Chaque citoyen dispose d'un conteneur personnel chiffré (**Personal Online Datastore - POD**) et fait valoir ses droits via des **Preuves à Divulgation Nulle (Zero-Knowledge Proofs - ZKP)**.

---

## 📁 Structure du Dépôt

{BT}
Republique6/
├── .env.local             # Clés d'API locales (Gemini, etc. - NON COMMITTÉ)
├── index.html             # Interface cartographique Canvas (28 nœuds) & UML
├── orchestrateur.py       # Moteur d'orchestration multi-agents Gemini
├── requirements.txt       # Dépendances Python
├── docs/                  # Documentation technique & RFCs formelles
│   ├── architecture/      # Spécifications du micro-noyau et Ring-0/Ring-3
│   └── specifications/    # Méta-modèle objet, PODs et protocoles ZKP
├── sprints/               # Journal d'incréments agiles généré par l'IA
└── src/
    ├── agents/            # Prompts et logiques des agents spécialisés
    ├── kernel/            # Primitives du micro-noyau
    └── simulation/        # Calculs de flux (Kirchhoff) et graphe territorial
{BT}

---

## 🤖 Pipeline d'Orchestration Multi-Agents

Le projet progresse au rythme de sprints bihebdomadaires pilotés par une équipe d'agents IA via l'API Gemini :
* **Agent 1 (AST Parser) :** Décompilation de la Constitution de 1958 en arbre syntaxique.
* **Agent 2 (Bug Profiler) :** Cartographie des crises historiques (1958, 1968, 1973, 1983, 2008, 2023) sous forme d'anomalies de concurrence et de fuites mémoire.
* **Agent 3 (Microkernel Architect) :** Définition des interfaces formelles d'isolation des privilèges.
* **Agent 4 (Graph Physics) :** Vérification de la loi de conservation de Kirchhoff sur 28 métropoles.
* **Agent 5 (Documentaliste & Scribe) :** Synthèse en temps réel dans `docs/` et `sprints/`.
* **Agent 6 (Web Compiler) :** Intégration des livrables dans `index.html`.

---

## 🚀 Démarrage Rapide

1. **Initialiser l'environnement virtuel :**
{BT}bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
{BT}

2. **Renseigner votre clé Gemini dans `.env.local` :**
{BT}bash
GEMINI_API_KEY="votre_cle_api_ici"
{BT}

3. **Exécuter un cycle d'orchestration :**
{BT}bash
python orchestrateur.py
{BT}

4. **Visualiser la plateforme :** Ouvrez `index.html` dans n'importe quel navigateur web.
"""

GITIGNORE_CONTENT = """# Environnement & Clés d'API
.env
.env.local
.env.*.local
*.env

# Cache Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environnements virtuels
venv/
env/
ENV/
.venv/

# IDE & OS
.vscode/
.idea/
*.swp
.DS_Store
Thumbs.db
"""

REQUIREMENTS_CONTENT = """google-genai>=0.1.1
python-dotenv>=1.0.0
rich>=13.0.0
"""

ENV_LOCAL_CONTENT = """# Clé API Google Gemini pour l'orchestrateur multi-agents
# Obtenez votre clé sur : [https://aistudio.google.com/](https://aistudio.google.com/)
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
"""

def create_repository():
    root = Path(".")
    print(f"[+] Initialisation de l'architecture Republique6 dans : {root.resolve()}")

    for dir_path in DIRECTORIES:
        p = root / dir_path
        p.mkdir(parents=True, exist_ok=True)
        print(f"  └── Dossier créé : {dir_path}/")

    files_to_write = {
        "README.md": README_CONTENT.strip() + "\n",
        ".gitignore": GITIGNORE_CONTENT.strip() + "\n",
        "requirements.txt": REQUIREMENTS_CONTENT.strip() + "\n",
    }

    for filename, content in files_to_write.items():
        file_path = root / filename
        file_path.write_text(content, encoding="utf-8")
        print(f"  ├── Fichier initialisé : {filename}")

    env_file = root / ".env.local"
    if not env_file.exists():
        env_file.write_text(ENV_LOCAL_CONTENT.strip() + "\n", encoding="utf-8")
        print("  ├── Fichier configuré : .env.local (pensez à renseigner votre clé)")
    else:
        print("  ├── .env.local existe déjà (non écrasé)")

    manifesto_doc = root / "docs" / "manifeste_missions.md"
    manifesto_doc.write_text(
        "# Missions Fondatrices de la VIᵉ République\n\n"
        "1. **Abstraction à 95+%** : Mathématisation des flux sociaux déterministes.\n"
        "2. **Obsolescence 1958** : Abandon du bricolage fiscal de type Windows 95.\n"
        "3. **PODs & ZKP** : Souveraineté cryptographique individuelle et fin des fuites massives.\n",
        encoding="utf-8"
    )
    print("  └── Fichier de documentation créé : docs/manifeste_missions.md")

    print("\n[✓] Structure du dépôt déployée avec succès.")

if __name__ == "__main__":
    create_repository()