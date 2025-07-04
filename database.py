# database.py
import sqlite3
import os

# 📍 Utilise un chemin relatif pour que ça fonctionne en ligne
DB_PATH = os.path.join("data", "sofitel.db")

# 🔄 Connexion en lecture seule (mode=ro) pour hébergement Streamlit Cloud
def get_connection():
    uri = f"file:{DB_PATH}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.execute("PRAGMA foreign_keys = ON")  # 🔐 Active les clés étrangères (utile même en lecture)
    return conn


# 🔧 Création des tables si elles n'existent pas
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Table EMPLOYES
    cur.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYES (
        id_employe INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        fonction TEXT,
        departement TEXT,
        type_contrat TEXT,
        date_enregistrement DATE
    );
    """)

    # Table FORMATIONS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS FORMATIONS (
        id_formation INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT,
        duree INTEGER,
        unite_duree TEXT,
        date_enregistrement DATE
    );
    """)

    # Table FORMATEURS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS FORMATEURS (
        id_formateur INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        responsable TEXT,
        email TEXT,
        telephone TEXT,
        adresse TEXT,
        date_enregistrement DATE
    );
    """)

    # Table SESSIONS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS SESSIONS (
        id_session INTEGER PRIMARY KEY AUTOINCREMENT,
        id_formation INTEGER,
        id_formateur INTEGER,
        date_formation DATE,
        prix REAL,
        paiement_effectue BOOLEAN,
        FOREIGN KEY(id_formation) REFERENCES FORMATIONS(id_formation) ON DELETE CASCADE,
        FOREIGN KEY(id_formateur) REFERENCES FORMATEURS(id_formateur) ON DELETE SET NULL
    );
    """)

    # Table SUIVI
    cur.execute("""
    CREATE TABLE IF NOT EXISTS SUIVI (
        id_suivi INTEGER PRIMARY KEY AUTOINCREMENT,
        id_employe INTEGER,
        id_session INTEGER,
        statut TEXT,
        date_validation DATE,
        date_enregistrement DATE,
        FOREIGN KEY(id_employe) REFERENCES EMPLOYES(id_employe) ON DELETE CASCADE,
        FOREIGN KEY(id_session) REFERENCES SESSIONS(id_session) ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()
