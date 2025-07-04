# 🏨 Projet_SOFITEL – Application de Gestion des Formations

## 🎯 Objectif du projet

Ce projet a été réalisé dans le cadre d’un stage au Sofitel Rabat Jardin des Roses.  
Il vise à digitaliser et centraliser la gestion des formations internes des employés, afin d'améliorer le suivi des compétences, la planification des sessions et l'évaluation de la participation.

L'application est conçue avec **Python**, **Streamlit** pour l'interface web, et **SQLite** pour le stockage local des données.

---

## ⚙️ Fonctionnalités principales

- **CRUD complet** : Création, lecture, mise à jour et suppression des données pour chaque entité
- **👤 Gérer les employés**
  - ➕ Ajouter facilement un nouvel employé
  - 🔍 Rechercher un employé par nom, prénom ou département
  - 📄 Afficher une fiche individuelle pour chaque employé
  - 📚 Gérer plusieurs formations par personne (relation multiple via une table de suivi)
- **📚 Gérer les formations**
  - Ajout de nouvelles formations avec durée personnalisée
- **🧑‍🏫 Gérer les formateurs**
  - Suivi des formateurs externes, paiements, coordonnées
- **🗓️ Planification des sessions**
  - Associer une formation, un formateur, une date
- **✅ Suivi des participations**
  - Associer un ou plusieurs employés à une session
  - ✅ Valider ou modifier le statut d’une formation suivie
- **📊 Tableau de bord**
  - Statistiques globales (taux de formation, services les plus formés…)
- **🔍 Filtres dynamiques**
  - Filtrer par formation, département, statut, date
- **📤 Export des résultats**
  - Exporter ou imprimer une liste filtrée (Excel ou PDF)
  - Possibilité d’imprimer des fiches propres pour les réunions

---

## ✅ Bénéfices attendus

- ⏱️ Gain de temps
- ❌ Réduction des erreurs humaines
- 🧠 Visualisation claire et rapide
- 🧾 Génération automatique de documents
- 🖥️ Interface moderne, simple et fluide

---

## 🧱 Architecture du projet

```
Projet_SOFITEL/
│
├── app.py               # ⚙️ Application principale Streamlit
├── database.py          # 🗃️ Création et connexion à la base SQLite
├── helpers.py           # 🔁 Fonctions utilitaires
│
├── data/
│   └── sofitel.db       # Base SQLite générée automatiquement
│
├── assets/              # 🎨 Images et ressources visuelles
│   ├── logo.png
│   └── background.jpg
│
├── styles/              # (Optionnel) CSS pour design personnalisé
│   └── style.css
│
└── README.md            # 🧾 Documentation actuelle
```

---

## 💻 Technologies utilisées

- Python 3.x
- Streamlit
- SQLite3
- Pandas (pour export Excel)
- FPDF ou ReportLab (pour export PDF)
- matplotlib / plotly (graphiques à venir)

---

## 🚀 Lancer l'application

```bash
streamlit run app.py
```

---

## 🙋‍♂️ Réalisé par

**TOUGOUMA Céphas Angelo**  
Étudiant en 1ère année cycle ingénieur informatique – JUNIA Maroc  
Stage réalisé au Sofitel Rabat Jardin des Roses  
Période : Juin - Juillet 2025


---

## 🔄 Évolutivité et perspectives

Ce projet a été conçu pour être évolutif : d'autres fonctionnalités pourront être ajoutées progressivement, telles que l'ajout de graphiques interactifs, la gestion multi-utilisateur avec authentification.
L’architecture actuelle permet d’intégrer ces évolutions sans remettre en cause la structure existante.