#!/usr/bin/env python3
"""
orchestrateur.py
Moteur d'orchestration multi-agents pour le projet VI.OS (Ma 6ᵉ République).
Charge la clé depuis .env.local, orchestre l'analyse système via Gemini,
et produit les spécifications techniques dans docs/ et sprints/.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Constante pour sécuriser la manipulation de backticks Markdown
BT = chr(96) * 3

# 1. Chargement de la clé API depuis .env.local
ENV_PATH = Path(".env.local")
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    print("[-] ERREUR: Clé GEMINI_API_KEY introuvable ou non configurée dans .env.local.")
    print("    Renseignez votre clé dans le fichier .env.local : GEMINI_API_KEY=\"AIzaSy...\"")
    sys.exit(1)

# Import du SDK officiel Google GenAI
try:
    from google import genai
    from google.genai import types
except ImportError:
    print("[-] Le paquet google-genai n'est pas installé.")
    print("    Installez-le avec : pip install google-genai python-dotenv rich")
    sys.exit(1)

# Initialisation du client
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-2.5-flash"


class AgentDocumentaliste:
    """Agent chargé de formaliser et consigner les spécifications techniques dans docs/ et sprints/."""

    def __init__(self, client: genai.Client):
        self.client = client
        self.system_prompt = (
            "Tu es l'Agent Documentaliste & Scribe en chef du projet 'Ma 6ᵉ République' (VI.OS).\n"
            "Ce projet démontre qu'une société humaine peut être formalisée à 95+% par du code informatique déterministe,\n"
            "que la constitution de 1958 est un OS obsolète (analogie Windows 95 à l'ère de l'IA),\n"
            "et que la souveraineté citoyenne repose sur des PODs décentralisés et des preuves à divulgation nulle (ZKP).\n"
            "Ton rôle est de rédiger des spécifications d'ingénierie formelles, percutantes, structurées en Markdown."
        )

    def generer_compte_rendu_sprint(self, sprint_num: int, theme: str, analyse_input: str) -> str:
        prompt = (
            f"Rédige le compte-rendu technique officiel pour le SPRINT #{sprint_num}.\n"
            f"Thème du Sprint : {theme}\n"
            f"Données d'analyse brutes des agents précédents :\n{analyse_input}\n\n"
            "Structure attendue du document Markdown :\n"
            "1. # Sprint Report: [Nom]\n"
            "2. ## Diagnostic Historique & Friction 1958 Identifiée\n"
            "3. ## Équivalent Système Informatique (Bug / Vulnérabilité)\n"
            "4. ## Spécification Technique de la Solution VI.OS (Microkernel / ZKP)\n"
            "5. ## Livrables Produits (Fichiers, Tests, Diagrammes)\n"
        )

        response = self.client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                temperature=0.3,
            )
        )
        return response.text

    def generer_doc_architecture(self, titre: str, composant: str) -> str:
        prompt = (
            f"Rédige une RFC formelle d'architecture pour le composant : {composant}.\n"
            f"Titre : {titre}\n\n"
            "Intègre impérativement :\n"
            "- L'isolation des privilèges (Ring-0 minimal vs Ring-3 subsidiaire)\n"
            "- La protection des données citoyennes via PODs et protocoles ZKP (Zero-Knowledge Proofs)\n"
            "- L'application des lois de conservation de Kirchhoff sur les flux.\n"
            "Sois extrêmement précis et utilise un vocabulaire d'ingénierie système."
        )

        response = self.client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                temperature=0.2,
            )
        )
        return response.text


def executer_sprint_pipeline():
    """Point d'entrée du pipeline de développement agile."""
    print("=" * 70)
    print("    VI.OS CORE ENGINE — ORCHESTRATEUR MULTI-AGENTS GEMINI")
    print("=" * 70)
    print(f"[*] Horodatage : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] Modèle sélectionné : {MODEL_ID}")

    Path("sprints").mkdir(parents=True, exist_ok=True)
    Path("docs/architecture").mkdir(parents=True, exist_ok=True)

    documentaliste = AgentDocumentaliste(client)

    # Sprint 1 : Décompilation de l'OS 1958 et invalidation du 49.3
    sprint_id = 1
    theme_sprint = "Décompilation du Monolithe 1958 & Invalidation du sudo 49.3"
    donnees_analyse = (
        "- Analyse de l'article 49 alinéa 3 de la Constitution de 1958.\n"
        "- Diagnostic système : Commande d'outrepassement direct de privilèges (sudo force write),\n"
        "  écrasant la validation du bus législatif sans consensus des pairs.\n"
        "- Conséquence : Désynchronisation du réseau civique, grèves de charge, rejet de l'exécutif.\n"
        "- Solution VI.OS : Remplacement par un mécanisme de Pull Request avec tests de résistance IA\n"
        "  et obligation d'auditabilité publique sur Ring-3."
    )

    print(f"\n[1/2] Lancement de la rédaction du rapport Sprint #{sprint_id}...")
    rapport_sprint = documentaliste.generer_compte_rendu_sprint(sprint_id, theme_sprint, donnees_analyse)

    sprint_file = Path("sprints") / f"sprint_{sprint_id}_decompiler_1958.md"
    sprint_file.write_text(rapport_sprint, encoding="utf-8")
    print(f"  └── Rapport sauvegardé : {sprint_file}")

    # Rédaction RFC : Architecture PODs & ZKP
    print("\n[2/2] Rédaction de la RFC technique sur les PODs et la cryptographie ZKP...")
    doc_zkp = documentaliste.generer_doc_architecture(
        titre="RFC-002 : Architecture des PODs Décentralisés & Preuves ZKP",
        composant="Souveraineté des Données Citoyennes & Zéro-Leakage"
    )

    doc_file = Path("docs") / "architecture" / "rfc_002_pods_zkp.md"
    doc_file.write_text(doc_zkp, encoding="utf-8")
    print(f"  └── Spécification sauvegardée : {doc_file}")

    print("\n" + "=" * 70)
    print("[✓] Pipeline d'orchestration exécuté avec succès.")
    print("    Les livrables ont été injectés dans les répertoires docs/ et sprints/.")
    print("=" * 70)


if __name__ == "__main__":
    executer_sprint_pipeline()