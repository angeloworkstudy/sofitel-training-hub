import streamlit as st
from database import create_tables
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(
    page_title="Sofitel Training Hub",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS moderne style américain
# CSS Sofitel optimisé pour la lisibilité - Remplacez votre section CSS par ceci :

with open('styles/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Créer les tables au lancement
create_tables()

# Header moderne
st.markdown("""
<div class="modern-card" style="margin-bottom: 2rem;">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 60px; height: 60px; border-radius: 1rem; display: flex; align-items: center; justify-content: center; margin-right: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                <span style="color: white; font-size: 1.75rem; font-weight: bold;">S</span>
            </div>
            <div>
                <h1 style="margin: 0; font-size: 1.875rem; font-weight: 800; color: #1e293b; letter-spacing: -0.025em;">Sofitel Training Hub</h1>
                <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Plateforme de gestion des formations • Rabat Jardin des Roses</p>
            </div>
        </div>
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 0.5rem 1rem; border-radius: 9999px; color: white; font-size: 0.75rem; font-weight: 600; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <span style="margin-right: 0.5rem;">🟢</span>Système Actif
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
# Sidebar moderne
st.sidebar.markdown("""
<div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 1.5rem;">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
        <span style="color: white; font-size: 2rem;">🏨</span>
    </div>
    <h3 style="margin: 0; color: #1e293b; font-weight: 700; font-size: 1.125rem;">Navigation Principale</h3>
    <p style="margin: 0.5rem 0 0 0; color: #64748b; font-size: 0.75rem;">Sélectionnez une section</p>
</div>
""", unsafe_allow_html=True)

# Menu principal
menu = st.sidebar.selectbox("Navigation", [
    "🏠 Accueil / Tableau de bord",
    "👤 Gérer les employés", 
    "📚 Gérer les formations",
    "🧑‍🏫 Gérer les formateurs",
    "🗓️ Planifier une session",
    "✅ Suivi des participations"
])

# DASHBOARD
if menu == "🏠 Accueil / Tableau de bord":
    from helpers import (
        recuperer_formations, recuperer_formateurs, recuperer_employes,
        recuperer_sessions, recuperer_suivis
    )
    
    st.markdown('<div class="section-header"><h2>📊 Tableau de Bord Exécutif</h2></div>', unsafe_allow_html=True)
    
    # Métriques principales avec design moderne
    col1, col2, col3, col4 = st.columns(4)
    
    formations_count = len(recuperer_formations())
    formateurs_count = len(recuperer_formateurs())
    employes_count = len(recuperer_employes())
    sessions_count = len(recuperer_sessions())
    participations_count = len(recuperer_suivis())
    
    with col1:
        st.markdown(f"""
        <div class="modern-card">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Formations</p>
                    <p style="margin: 0; color: #1e293b; font-size: 2.5rem; font-weight: 800; line-height: 1;">{formations_count}</p>
                </div>
                <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); width: 56px; height: 56px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                    <span style="color: white; font-size: 1.5rem;">📚</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="modern-card">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Formateurs</p>
                    <p style="margin: 0; color: #1e293b; font-size: 2.5rem; font-weight: 800; line-height: 1;">{formateurs_count}</p>
                </div>
                <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); width: 56px; height: 56px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                    <span style="color: white; font-size: 1.5rem;">🧑‍🏫</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="modern-card">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Employés</p>
                    <p style="margin: 0; color: #1e293b; font-size: 2.5rem; font-weight: 800; line-height: 1;">{employes_count}</p>
                </div>
                <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); width: 56px; height: 56px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                    <span style="color: white; font-size: 1.5rem;">👥</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="modern-card">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Sessions</p>
                    <p style="margin: 0; color: #1e293b; font-size: 2.5rem; font-weight: 800; line-height: 1;">{sessions_count}</p>
                </div>
                <div style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); width: 56px; height: 56px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                    <span style="color: white; font-size: 1.5rem;">📅</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Graphiques modernes avec Plotly
    col1, col2 = st.columns(2)
    
    with col1:
        suivis = recuperer_suivis()
        if suivis:
            df_suivis = pd.DataFrame(suivis, columns=[
                "ID", "Nom", "Prénom", "Formation", "Formateur", "Date", "Statut", "Validation"
            ])
            
            statut_counts = df_suivis["Statut"].value_counts()
            
            fig = px.pie(
                values=statut_counts.values,
                names=statut_counts.index,
                title="<b>Répartition des Participations</b>",
                color_discrete_map={'validé': '#10b981', 'absent': '#ef4444'},
                hole=0.4
            )
            
            fig.update_layout(
                font=dict(family="Inter", size=12),
                title_font_size=18,
                title_font_color="#1e293b",
                title_x=0.5,
                paper_bgcolor="rgba(255,255,255,0.98)",
                plot_bgcolor="rgba(255,255,255,0.98)",
                margin=dict(l=20, r=20, t=60, b=20),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if employes_count > 0:
            employes = recuperer_employes()
            df_emp = pd.DataFrame(employes, columns=[
                "ID", "Nom", "Prénom", "Fonction", "Département", "Contrat", "Date"
            ])
            
            dept_counts = df_emp["Département"].value_counts().head(6)
            
            fig = px.bar(
                x=dept_counts.values,
                y=dept_counts.index,
                title="<b>Employés par Département</b>",
                orientation='h',
                color=dept_counts.values,
                color_continuous_scale=["#dbeafe", "#2563eb"]
            )
            
            fig.update_layout(
                font=dict(family="Inter", size=12),
                title_font_size=18,
                title_font_color="#1e293b",
                title_x=0.5,
                paper_bgcolor="rgba(255,255,255,0.98)",
                plot_bgcolor="rgba(255,255,255,0.98)",
                margin=dict(l=20, r=20, t=60, b=20),
                showlegend=False,
                yaxis={'categoryorder':'total ascending'}
            )
            
            fig.update_traces(
                marker_line_color='#1d4ed8',
                marker_line_width=1
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # KPIs supplémentaires
    if participations_count > 0:
        col1, col2, col3 = st.columns(3)
        
        taux_reussite = (df_suivis[df_suivis['Statut'] == 'validé'].shape[0] / participations_count) * 100
        formation_populaire = df_suivis['Formation'].value_counts().index[0] if len(df_suivis['Formation'].value_counts()) > 0 else "Aucune"
        
        sessions = recuperer_sessions()
        df_sessions = pd.DataFrame(sessions, columns=["ID", "Formation", "Formateur", "Date", "Prix", "Paiement"])
        df_sessions['Date'] = pd.to_datetime(df_sessions['Date'])
        sessions_ce_mois = df_sessions[df_sessions['Date'].dt.month == datetime.date.today().month].shape[0]
        
        with col1:
            st.markdown(f"""
            <div class="modern-card">
                <h4 style="margin: 0 0 0.5rem 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase;">Taux de Réussite</h4>
                <p style="margin: 0; color: #10b981; font-size: 2rem; font-weight: 800;">{taux_reussite:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="modern-card">
                <h4 style="margin: 0 0 0.5rem 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase;">Formation Populaire</h4>
                <p style="margin: 0; color: #3b82f6; font-size: 1rem; font-weight: 600; line-height: 1.2;">{formation_populaire[:40]}{"..." if len(formation_populaire) > 40 else ""}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="modern-card">
                <h4 style="margin: 0 0 0.5rem 0; color: #64748b; font-size: 0.875rem; font-weight: 500; text-transform: uppercase;">Sessions ce Mois</h4>
                <p style="margin: 0; color: #8b5cf6; font-size: 2rem; font-weight: 800;">{sessions_ce_mois}</p>
            </div>
            """, unsafe_allow_html=True)

# SECTION EMPLOYÉS (Corrección)
elif menu == "👤 Gérer les employés":
    from helpers import (
        ajouter_employe, recuperer_employes, supprimer_employe,
        modifier_employe, get_fiche_employe, exporter_employes_excel
    )
    
    st.markdown('<div class="section-header"><h2>👥 Gestion des Employés</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["➕ Ajouter", "📋 Liste", "🔍 Fiches"])
    
    with tab1:
        st.markdown("### Nouvel Employé")
        
        with st.form("form_employe", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                nom = st.text_input("Nom *", placeholder="Nom de famille", help="Champ obligatoire")
                fonction = st.text_input("Fonction", placeholder="Ex: Manager, Agent...")
                type_contrat = st.selectbox("Type de contrat", ["CDI", "CDD"])
            
            with col2:
                prenom = st.text_input("Prénom *", placeholder="Prénom", help="Champ obligatoire")
                departement = st.text_input("Département", placeholder="Ex: IT, RH, F&B...")
                date_enregistrement = st.date_input("Date d'enregistrement", value=datetime.date.today())
            
            submitted = st.form_submit_button("✅ Ajouter l'employé", use_container_width=True)
            
            if submitted:
                if nom and prenom:
                    ajouter_employe(nom, prenom, fonction, departement, type_contrat, str(date_enregistrement))
                    st.success(f"✅ {prenom} {nom} ajouté avec succès!")
                    st.balloons()
                else:
                    st.error("❌ Le nom et le prénom sont obligatoires")
    
    with tab2:
        employes = recuperer_employes()
        if employes:
            df_employes = pd.DataFrame(employes, columns=[
                "ID", "Nom", "Prénom", "Fonction", "Département", "Contrat", "Date enregistrement"
            ])
            
            # Recherche
            search_term = st.text_input(
                "🔍 Rechercher un employé",
                placeholder="Nom, prénom ou département...",
                help="Recherche en temps réel"
            )
            
            if search_term:
                mask = (
                    df_employes["Nom"].str.lower().str.contains(search_term.lower(), na=False) |
                    df_employes["Prénom"].str.lower().str.contains(search_term.lower(), na=False) |
                    df_employes["Département"].str.lower().str.contains(search_term.lower(), na=False)
                )
                df_filtered = df_employes[mask]
            else:
                df_filtered = df_employes
            
            # Affichage responsive du tableau
            st.markdown("""
            <div style="overflow-x: auto; border-radius: 1rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
            """, unsafe_allow_html=True)
            
            st.dataframe(
                df_filtered.drop(columns=["ID"]),
                use_container_width=True,
                height=400
            )
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Actions
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("📥 Exporter Excel", use_container_width=True):
                    chemin = exporter_employes_excel()
                    with open(chemin, "rb") as f:
                        st.download_button(
                            "📄 Télécharger",
                            f,
                            file_name="employes_export.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
            
            with col2:
                st.metric("Total", len(df_filtered), delta=f"{len(df_filtered) - len(df_employes)}" if search_term else None)
            
            with col3:
                if search_term:
                    st.metric("Résultats", len(df_filtered))
        else:
            st.info("📭 Aucun employé enregistré pour le moment")
    
    with tab3:
        st.markdown("### Fiches Employés Détaillées")
        
        employes = recuperer_employes()
        if employes:
            employe_dict = {f"{e[2]} {e[1]} – {e[3]} ({e[4]})": e[0] for e in employes}
            
            selected_emp = st.selectbox(
                "Choisir un employé",
                options=list(employe_dict.keys()),
                help="Sélectionnez un employé pour voir sa fiche complète"
            )
            
            if st.button("📄 Afficher la fiche", use_container_width=True):
                id_selected = employe_dict[selected_emp]
                fiches = get_fiche_employe(id_selected)
                
                if fiches:
                    nom, prenom, fonction, departement, contrat = fiches[0][:5]
                    
                    st.markdown(f"""
                    <div class="employee-card">
                        <div style="display: flex; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap;">
                            <div class="avatar">{prenom[0]}{nom[0]}</div>
                            <div style="min-width: 0; flex: 1;">
                                <h3 style="margin: 0; color: #1e293b; font-size: 1.5rem; font-weight: 700; word-wrap: break-word;">{prenom} {nom}</h3>
                                <p style="margin: 0; color: #64748b; font-size: 1rem; font-weight: 500;">{fonction}</p>
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
                            <div>
                                <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Département</p>
                                <p style="margin: 0; color: #1e293b; font-weight: 600; font-size: 1rem; word-wrap: break-word;">{departement}</p>
                            </div>
                            <div>
                                <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Type de contrat</p>
                                <p style="margin: 0; color: #1e293b; font-weight: 600; font-size: 1rem;">{contrat}</p>
                            </div>
                            <div>
                                <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Formations suivies</p>
                                <p style="margin: 0; color: #2563eb; font-weight: 700; font-size: 1.25rem;">{len(fiches)} formation(s)</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 📚 Historique des Formations")
                    for f in fiches:
                        status_color = "#10b981" if f[7] == "validé" else "#ef4444"
                        status_bg = "rgba(16, 185, 129, 0.1)" if f[7] == "validé" else "rgba(239, 68, 68, 0.1)"
                        
                        st.markdown(f"""
                        <div style="background: rgba(255,255,255,0.95); border-radius: 1rem; padding: 1.5rem; margin-bottom: 1rem; border-left: 4px solid {status_color}; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1); overflow-x: auto;">
                            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
                                <h4 style="margin: 0; color: #1e293b; font-size: 1.125rem; font-weight: 600; flex-grow: 1; min-width: 0; word-wrap: break-word;">{f[5]}</h4>
                                <span class="status-badge" style="background: {status_bg}; color: {status_color}; border: 1px solid {status_color}; white-space: nowrap;">{f[7]}</span>
                            </div>
                            <div style="display: flex; gap: 1rem; color: #64748b; font-size: 0.875rem; flex-wrap: wrap;">
                                <span><strong>📅 Date:</strong> {f[6]}</span>
                                <span><strong>🧑‍🏫 Formateur:</strong> {f[9]}</span>
                                <span><strong>✅ Validé le:</strong> {f[8]}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("📭 Aucune formation trouvée pour cet employé")
        else:
            st.info("📭 Aucun employé enregistré")
        
        # Section de modification/suppression avec corrections
        st.subheader("🔧 Modifier ou supprimer un employé ciblé")
        
        search_modif = st.text_input("🔍 Rechercher un employé pour modifier ou supprimer (nom ou prénom)", key="search_modif").lower()
        
        if search_modif and employes:
            df_employes = pd.DataFrame(employes, columns=[
                "ID", "Nom", "Prénom", "Fonction", "Département", "Contrat", "Date enregistrement"
            ])
            
            results_modif = df_employes[df_employes["Nom"].str.lower().str.contains(search_modif) |
                                        df_employes["Prénom"].str.lower().str.contains(search_modif)]
            
            if not results_modif.empty:
                for _, row in results_modif.iterrows():
                    with st.expander(f"{row['Prénom']} {row['Nom']} – {row['Fonction']} ({row['Département']})"):
                        st.write(f"ID : {row['ID']}")
                        st.write(f"Type de contrat : {row['Contrat']}")
                        st.write(f"Date d'enregistrement : {row['Date enregistrement']}")
                        
                        col1, col2 = st.columns(2)
                        
                        if col1.button("🗑️ Supprimer", key=f"del_{row['ID']}"):
                            supprimer_employe(row['ID'])
                            st.warning("Employé supprimé. Rechargez la page.")
                            st.rerun()
                        
                        with col2:
                            # Formulaire de modification SANS key sur form_submit_button
                            with st.form(f"form_modif_emp_{row['ID']}"):
                                st.write("**✏️ Modifier l'employé:**")
                                new_nom = st.text_input("Nom", row['Nom'], key=f"nom_{row['ID']}")
                                new_prenom = st.text_input("Prénom", row['Prénom'], key=f"prenom_{row['ID']}")
                                new_fonction = st.text_input("Fonction", row['Fonction'], key=f"fonction_{row['ID']}")
                                new_departement = st.text_input("Département", row['Département'], key=f"dept_{row['ID']}")
                                new_type = st.selectbox("Contrat", ["CDI", "CDD"], index=["CDI", "CDD"].index(row['Contrat']), key=f"type_{row['ID']}")
                                
                                # CORRECTION: Pas de key sur form_submit_button
                                if st.form_submit_button("💾 Sauvegarder"):
                                    modifier_employe(row['ID'], new_nom, new_prenom, new_fonction, new_departement, new_type)
                                    st.success("Employé mis à jour. Rechargez la page.")
                                    st.rerun()
            else:
                st.info("Aucun employé trouvé avec ce nom ou prénom.")
        else:
            st.caption("🔕 Entrez un nom ou prénom ci-dessus pour activer la modification ciblée.")

# SECTION FORMATIONS (Corrección)
elif menu == "📚 Gérer les formations":
    from helpers import (
        ajouter_formation, recuperer_formations, supprimer_formation,
        modifier_formation, exporter_formations_excel
    )
    
    st.markdown('<div class="section-header"><h2>📚 Gestion des Formations</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["➕ Créer", "📋 Catalogue", "🔧 Modifier"])
    
    with tab1:
        st.markdown("### Nouvelle Formation")
        
        with st.form("form_formation", clear_on_submit=True):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                titre = st.text_input("Titre de la formation *", placeholder="Ex: Leadership et Management...")
            
            with col2:
                duree = st.number_input("Durée *", min_value=1, value=8, help="Durée de la formation")
            
            with col3:
                unite = st.selectbox("Unité", ["heures", "jour(s)"])
            
            date_enregistrement = st.date_input("Date d'enregistrement", value=datetime.date.today())
            
            submitted = st.form_submit_button("✅ Créer la formation", use_container_width=True)
            
            if submitted:
                if titre:
                    ajouter_formation(titre, duree, unite, str(date_enregistrement))
                    st.success(f"✅ Formation '{titre}' créée avec succès!")
                    st.balloons()
                else:
                    st.error("❌ Le titre est obligatoire")
    
    with tab2:
        formations = recuperer_formations()
        if formations:
            df_formations = pd.DataFrame(formations, columns=[
                "ID", "Titre", "Durée", "Unité", "Date enregistrement"
            ])
            
            # Recherche
            search_formation = st.text_input(
                "🔍 Rechercher une formation",
                placeholder="Tapez le titre d'une formation...",
                help="Recherche par titre"
            )
            
            if search_formation:
                mask = df_formations["Titre"].str.lower().str.contains(search_formation.lower(), na=False)
                df_filtered = df_formations[mask]
            else:
                df_filtered = df_formations
            
            # Affichage en cards modernes avec responsive
            st.markdown("### Catalogue des Formations")
            
            for _, formation in df_filtered.iterrows():
                st.markdown(f"""
                <div class="modern-card">
                    <div style="display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap; gap: 1rem;">
                        <div style="flex-grow: 1; min-width: 0;">
                            <h4 style="margin: 0 0 0.5rem 0; color: #1e293b; font-size: 1.125rem; font-weight: 600; word-wrap: break-word;">{formation['Titre']}</h4>
                            <div style="display: flex; gap: 1rem; color: #64748b; font-size: 0.875rem; flex-wrap: wrap;">
                                <span><strong>⏱️ Durée:</strong> {formation['Durée']} {formation['Unité']}</span>
                                <span><strong>📅 Créée le:</strong> {formation['Date enregistrement']}</span>
                            </div>
                        </div>
                        <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); width: 48px; height: 48px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <span style="color: white; font-size: 1.25rem;">📚</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Export
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("📥 Exporter Excel", use_container_width=True):
                    chemin = exporter_formations_excel()
                    with open(chemin, "rb") as f:
                        st.download_button(
                            "📄 Télécharger",
                            f,
                            file_name="formations_export.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
            
            with col2:
                st.metric("Total Formations", len(df_filtered))
        else:
            st.info("📭 Aucune formation créée pour le moment")
    
    with tab3:
        st.markdown("### Modifier ou Supprimer une Formation")
        
        formations = recuperer_formations()
        if formations:
            df_formations = pd.DataFrame(formations, columns=[
                "ID", "Titre", "Durée", "Unité", "Date enregistrement"
            ])
            
            search_modif = st.text_input(
                "🔍 Rechercher pour modifier",
                placeholder="Titre de la formation...",
                key="search_modif_formation"
            )
            
            if search_modif:
                mask = df_formations["Titre"].str.lower().str.contains(search_modif.lower(), na=False)
                results = df_formations[mask]
                
                if not results.empty:
                    for _, row in results.iterrows():
                        with st.expander(f"📚 {row['Titre']} ({row['Durée']} {row['Unité']})"):
                            col1, col2 = st.columns([1, 2])
                            
                            with col1:
                                st.write(f"**ID:** {row['ID']}")
                                st.write(f"**Durée:** {row['Durée']} {row['Unité']}")
                                st.write(f"**Créée le:** {row['Date enregistrement']}")
                                
                                if st.button("🗑️ Supprimer", key=f"del_f_{row['ID']}", help="Attention: action irréversible"):
                                    supprimer_formation(row['ID'])
                                    st.success("✅ Formation supprimée!")
                                    st.rerun()
                            
                            with col2:
                                # CORRECTION: Formulaire sans key sur form_submit_button
                                with st.form(f"form_modif_f_{row['ID']}"):
                                    st.write("**✏️ Modifier la formation:**")
                                    new_titre = st.text_input("Titre", row['Titre'], key=f"titre_{row['ID']}")
                                    new_duree = st.number_input("Durée", min_value=1, value=int(row['Durée']), key=f"duree_{row['ID']}")
                                    new_unite = st.selectbox("Unité", ["heures", "jour(s)"],
                                                            index=["heures", "jour(s)"].index(row['Unité']), key=f"unite_{row['ID']}")
                                    
                                    # CORRECTION: Pas de key sur form_submit_button
                                    if st.form_submit_button("💾 Sauvegarder"):
                                        modifier_formation(row['ID'], new_titre, new_duree, new_unite)
                                        st.success("✅ Formation modifiée!")
                                        st.rerun()
                else:
                    st.info("🔍 Aucune formation trouvée")
        else:
            st.info("📭 Aucune formation disponible")

# SECTION FORMATEURS (Corrección)
elif menu == "🧑‍🏫 Gérer les formateurs":
    from helpers import (
        ajouter_formateur, recuperer_formateurs, supprimer_formateur,
        modifier_formateur, exporter_formateurs_excel
    )
    
    st.markdown('<div class="section-header"><h2>🧑‍🏫 Gestion des Formateurs</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["➕ Ajouter", "📋 Liste", "🔧 Modifier"])
    
    with tab1:
        st.markdown("### Nouveau Formateur")
        
        with st.form("form_formateur", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                nom = st.text_input("Nom du formateur/organisme *", placeholder="Nom ou raison sociale")
                responsable = st.text_input("Responsable", placeholder="Nom du contact principal")
                email = st.text_input("Email", placeholder="contact@example.com")
            
            with col2:
                telephone = st.text_input("Téléphone", placeholder="+212 6XX XX XX XX")
                adresse = st.text_area("Adresse", placeholder="Adresse complète...")
                date_enregistrement = st.date_input("Date d'enregistrement", value=datetime.date.today())
            
            submitted = st.form_submit_button("✅ Ajouter le formateur", use_container_width=True)
            
            if submitted:
                if nom:
                    ajouter_formateur(nom, responsable, email, telephone, adresse, str(date_enregistrement))
                    st.success(f"✅ Formateur '{nom}' ajouté avec succès!")
                    st.balloons()
                else:
                    st.error("❌ Le nom est obligatoire")
    
    with tab2:
        formateurs = recuperer_formateurs()
        if formateurs:
            df_formateurs = pd.DataFrame(formateurs, columns=[
                "ID", "Nom", "Responsable", "Email", "Téléphone", "Adresse", "Date enregistrement"
            ])
            
            # Recherche
            search_formateur = st.text_input(
                "🔍 Rechercher un formateur",
                placeholder="Nom, responsable ou email...",
                help="Recherche par nom, responsable ou email"
            )
            
            if search_formateur:
                mask = (
                    df_formateurs["Nom"].str.lower().str.contains(search_formateur.lower(), na=False) |
                    df_formateurs["Responsable"].str.lower().str.contains(search_formateur.lower(), na=False) |
                    df_formateurs["Email"].str.lower().str.contains(search_formateur.lower(), na=False)
                )
                df_filtered = df_formateurs[mask]
            else:
                df_filtered = df_formateurs
            
            # Affichage en cards modernes avec responsive
            st.markdown("### Répertoire des Formateurs")
            
            for _, formateur in df_filtered.iterrows():
                st.markdown(f"""
                <div class="modern-card">
                    <div style="display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap; gap: 1rem;">
                        <div style="flex-grow: 1; min-width: 0;">
                            <h4 style="margin: 0 0 0.5rem 0; color: #1e293b; font-size: 1.125rem; font-weight: 600; word-wrap: break-word;">{formateur['Nom']}</h4>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Responsable</p>
                                    <p style="margin: 0; color: #1e293b; font-weight: 600; word-wrap: break-word;">{formateur['Responsable'] or 'Non spécifié'}</p>
                                </div>
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Email</p>
                                    <p style="margin: 0; color: #1e293b; font-weight: 600; word-wrap: break-word;">{formateur['Email'] or 'Non spécifié'}</p>
                                </div>
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Téléphone</p>
                                    <p style="margin: 0; color: #1e293b; font-weight: 600;">{formateur['Téléphone'] or 'Non spécifié'}</p>
                                </div>
                            </div>
                        </div>
                        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); width: 48px; height: 48px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <span style="color: white; font-size: 1.25rem;">🧑‍🏫</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Export
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("📥 Exporter Excel", use_container_width=True):
                    chemin = exporter_formateurs_excel()
                    with open(chemin, "rb") as f:
                        st.download_button(
                            "📄 Télécharger",
                            f,
                            file_name="formateurs_export.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
            
            with col2:
                st.metric("Total Formateurs", len(df_filtered))
        else:
            st.info("📭 Aucun formateur enregistré pour le moment")
    
    with tab3:
        st.markdown("### Modifier ou Supprimer un Formateur")
        
        formateurs = recuperer_formateurs()
        if formateurs:
            df_formateurs = pd.DataFrame(formateurs, columns=[
                "ID", "Nom", "Responsable", "Email", "Téléphone", "Adresse", "Date enregistrement"
            ])
            
            search_modif = st.text_input(
                "🔍 Rechercher pour modifier",
                placeholder="Nom du formateur...",
                key="search_modif_formateur"
            )
            
            if search_modif:
                mask = df_formateurs["Nom"].str.lower().str.contains(search_modif.lower(), na=False)
                results = df_formateurs[mask]
                
                if not results.empty:
                    for _, row in results.iterrows():
                        with st.expander(f"🧑‍🏫 {row['Nom']} - {row['Responsable']}"):
                            col1, col2 = st.columns([1, 2])
                            
                            with col1:
                                st.write(f"**Email:** {row['Email']}")
                                st.write(f"**Téléphone:** {row['Téléphone']}")
                                st.write(f"**Adresse:** {row['Adresse']}")
                                
                                if st.button("🗑️ Supprimer", key=f"del_fmt_{row['ID']}", help="Attention: action irréversible"):
                                    supprimer_formateur(row['ID'])
                                    st.success("✅ Formateur supprimé!")
                                    st.rerun()
                            
                            with col2:
                                # CORRECTION: Formulaire sans key sur form_submit_button
                                with st.form(f"form_modif_fmt_{row['ID']}"):
                                    st.write("**✏️ Modifier le formateur:**")
                                    new_nom = st.text_input("Nom", row['Nom'], key=f"nom_fmt_{row['ID']}")
                                    new_responsable = st.text_input("Responsable", row['Responsable'], key=f"resp_{row['ID']}")
                                    new_email = st.text_input("Email", row['Email'], key=f"email_{row['ID']}")
                                    new_telephone = st.text_input("Téléphone", row['Téléphone'], key=f"tel_{row['ID']}")
                                    new_adresse = st.text_area("Adresse", row['Adresse'], key=f"adr_{row['ID']}")
                                    
                                    # CORRECTION: Pas de key sur form_submit_button
                                    if st.form_submit_button("💾 Sauvegarder"):
                                        modifier_formateur(row['ID'], new_nom, new_responsable, new_email, new_telephone, new_adresse)
                                        st.success("✅ Formateur modifié!")
                                        st.rerun()
                else:
                    st.info("🔍 Aucun formateur trouvé")
        else:
            st.info("📭 Aucun formateur disponible")

# SECTION SESSIONS
elif menu == "🗓️ Planifier une session":
    from helpers import (
        ajouter_session, recuperer_sessions, supprimer_session,
        recuperer_formations, recuperer_formateurs
    )
    
    st.markdown('<div class="section-header"><h2>📅 Planification des Sessions</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["➕ Planifier", "📋 Sessions"])
    
    with tab1:
        st.markdown("### Nouvelle Session de Formation")
        
        formations = recuperer_formations()
        formateurs = recuperer_formateurs()
        
        if formations and formateurs:
            with st.form("form_session", clear_on_submit=True):
                col1, col2 = st.columns(2)
                
                with col1:
                    formation_choices = {f"{f[1]} ({f[2]} {f[3]})": f[0] for f in formations}
                    formateur_choices = {f"{f[1]} - {f[2]}": f[0] for f in formateurs}
                    
                    selected_formation = st.selectbox("Formation", list(formation_choices.keys()))
                    selected_formateur = st.selectbox("Formateur", list(formateur_choices.keys()))
                    date_formation = st.date_input("Date de la formation", value=datetime.date.today())
                
                with col2:
                    prix = st.number_input("Prix (MAD)", min_value=0.0, value=0.0, format="%.2f")
                    paiement = st.radio("Paiement effectué ?", ["Non", "Oui"], horizontal=True)
                
                submitted = st.form_submit_button("✅ Planifier la session", use_container_width=True)
                
                if submitted:
                    ajouter_session(
                        formation_choices[selected_formation],
                        formateur_choices[selected_formateur],
                        str(date_formation),
                        prix,
                        1 if paiement == "Oui" else 0
                    )
                    st.success("✅ Session planifiée avec succès!")
                    st.balloons()
        else:
            st.warning("⚠️ Veuillez d'abord ajouter des formations et des formateurs")
    
    with tab2:
        sessions = recuperer_sessions()
        if sessions:
            st.markdown("### Sessions Planifiées")
            
            for session in sessions:
                paiement_status = "✅ Payé" if session[5] else "❌ Non payé"
                paiement_color = "#10b981" if session[5] else "#ef4444"
                
                st.markdown(f"""
                <div class="modern-card">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div style="flex-grow: 1;">
                            <h4 style="margin: 0 0 0.5rem 0; color: #1e293b; font-size: 1.125rem; font-weight: 600;">{session[1]}</h4>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Formateur</p>
                                    <p style="margin: 0; color: #1e293b; font-weight: 600;">{session[2]}</p>
                                </div>
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Date</p>
                                    <p style="margin: 0; color: #1e293b; font-weight: 600;">{session[3]}</p>
                                </div>
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Prix</p>
                                    <p style="margin: 0; color: #1e293b; font-weight: 600;">{session[4]} MAD</p>
                                </div>
                                <div>
                                    <p style="margin: 0; color: #64748b; font-size: 0.875rem; font-weight: 500;">Paiement</p>
                                    <p style="margin: 0; color: {paiement_color}; font-weight: 600;">{paiement_status}</p>
                                </div>
                            </div>
                        </div>
                        <div style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); width: 48px; height: 48px; border-radius: 0.75rem; display: flex; align-items: center; justify-content: center; margin-left: 1rem;">
                            <span style="color: white; font-size: 1.25rem;">📅</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Bouton supprimer dans un expander
                with st.expander("⚙️ Actions"):
                    if st.button("🗑️ Supprimer cette session", key=f"del_sess_{session[0]}", help="Attention: action irréversible"):
                        supprimer_session(session[0])
                        st.success("✅ Session supprimée!")
                        st.rerun()
            
            st.metric("Total Sessions", len(sessions))
        else:
            st.info("📅 Aucune session planifiée pour le moment")

# SECTION PARTICIPATIONS
elif menu == "✅ Suivi des participations":
    from helpers import (
        ajouter_suivi, recuperer_suivis, supprimer_suivi,
        recuperer_employes, recuperer_sessions, recuperer_suivis_groupes_par_session,
        exporter_suivis_excel
    )
    
    st.markdown('<div class="section-header"><h2>✅ Suivi des Participations</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["➕ Enregistrer", "📊 Export Filtré", "📋 Par Session"])
    
    with tab1:
        st.markdown("### Enregistrer une Participation")
        
        employes = recuperer_employes()
        sessions = recuperer_sessions()
        
        if employes and sessions:
            with st.form("form_suivi"):
                employe_dict = {f"{e[2]} {e[1]} – {e[3]}": e[0] for e in employes}
                session_dict = {f"{s[1]} – {s[2]} ({s[3]})": s[0] for s in sessions}
                
                id_employe = st.selectbox("Employé", list(employe_dict.keys()))
                id_session = st.selectbox("Session", list(session_dict.keys()))
                statut = st.selectbox("Statut", ["validé", "absent"])
                date_validation = st.date_input("Date de validation", value=datetime.date.today())
                date_enregistrement = datetime.date.today()
                
                submitted = st.form_submit_button("Enregistrer")
                if submitted:
                    ajouter_suivi(employe_dict[id_employe], session_dict[id_session], statut, str(date_validation), str(date_enregistrement))
                    st.success("Participation enregistrée avec succès.")
            
            st.divider()
            st.markdown("### ➕ Ajout Multiple de Participations")
            
            with st.form("form_ajout_lot"):
                selected_session = st.selectbox("Session concernée", list(session_dict.keys()), key="session_lot")
                selected_employes = st.multiselect("Employés participants", list(employe_dict.keys()), key="multi_employes")
                statut_lot = st.selectbox("Statut", ["validé", "absent"], key="statut_lot")
                date_validation_lot = st.date_input("Date de validation", value=datetime.date.today(), key="date_val_lot")
                submitted_lot = st.form_submit_button("Enregistrer tous")
                
                if submitted_lot:
                    if selected_employes and selected_session:
                        id_sess = session_dict[selected_session]
                        for emp in selected_employes:
                            id_emp = employe_dict[emp]
                            ajouter_suivi(id_emp, id_sess, statut_lot, str(date_validation_lot), str(datetime.date.today()))
                        st.success(f"{len(selected_employes)} participations enregistrées pour cette session.")
                    else:
                        st.warning("Veuillez choisir au moins une session et un ou plusieurs employés.")
        else:
            st.info("Veuillez ajouter des employés et des sessions avant d'enregistrer une participation.")
    
    with tab2:
        st.markdown("### 🔍 Export Avancé Filtré des Suivis")
        
        # Filtres
        col1, col2, col3 = st.columns(3)
        with col1:
            filtre_statut = st.selectbox("Filtrer par statut", ["Tous", "validé", "absent"], key="statut_filtre")
        with col2:
            date_debut = st.date_input("Date début", value=datetime.date(2025, 1, 1))
        with col3:
            date_fin = st.date_input("Date fin", value=datetime.date.today())
        
        mot_cle = st.text_input("🔎 Mot-clé (nom, formation, formateur)").lower()
        
        # Récupération des données
        df_suivis = pd.DataFrame(recuperer_suivis(), columns=[
            "ID", "Nom", "Prénom", "Formation", "Formateur", "Date", "Statut", "Validation"
        ])
        
        if not df_suivis.empty:
            # Application des filtres
            masque = (pd.to_datetime(df_suivis["Validation"]) >= pd.to_datetime(date_debut)) & \
                    (pd.to_datetime(df_suivis["Validation"]) <= pd.to_datetime(date_fin))
            
            if filtre_statut != "Tous":
                masque &= df_suivis["Statut"] == filtre_statut
            
            if mot_cle:
                masque &= df_suivis.apply(lambda row: mot_cle in str(row["Nom"]).lower()
                                                    or mot_cle in str(row["Prénom"]).lower()
                                                    or mot_cle in str(row["Formation"]).lower()
                                                    or mot_cle in str(row["Formateur"]).lower(), axis=1)
            
            df_filtré = df_suivis[masque].drop(columns=["ID"])
            
            # Affichage tableau
            st.dataframe(df_filtré, use_container_width=True)
            
            # Export bouton
            if not df_filtré.empty:
                if st.button("📥 Exporter le tableau filtré"):
                    chemin = exporter_suivis_excel(df_filtré)
                    with open(chemin, "rb") as f:
                        st.download_button("📄 Télécharger le fichier Excel", f, file_name="suivis_filtrés.xlsx")
            else:
                st.info("Aucun suivi correspondant aux filtres.")
        else:
            st.info("Aucune participation enregistrée.")
    
    with tab3:
        st.markdown("### 📋 Suivi des Participations par Session")
        
        from helpers import recuperer_suivis_groupes_par_session
        groupes = recuperer_suivis_groupes_par_session()
        
        for session_id, data in groupes.items():
            with st.expander(f"{data['titre']} – {data['formateur']} ({data['date']})"):
                df_participants = pd.DataFrame(data['participants'], columns=["Nom", "Prénom", "Statut", "Date de validation"])
                st.dataframe(df_participants, use_container_width=True)

# Footer moderne
st.markdown("""
<div style="margin-top: 3rem; padding: 2rem; background: rgba(255,255,255,0.98); backdrop-filter: blur(20px); border-radius: 1.5rem; text-align: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.3);">
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
            <span style="color: white; font-size: 1.25rem;">🏨</span>
        </div>
        <h3 style="margin: 0; color: #1e293b; font-weight: 700;">Sofitel Training Hub</h3>
    </div>
    <p style="margin: 0; color: #64748b; font-size: 0.875rem; line-height: 1.5;">
        💡 Développé par <strong>TOUGOUMA Céphas Angelo</strong><br>
        Étudiant en 1ère année cycle ingénieur informatique – JUNIA Maroc<br>
        Stage réalisé au <strong>Sofitel Rabat Jardin des Roses</strong> • Été 2025
    </p>
    <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e2e8f0;">
        <p style="margin: 0; color: #64748b; font-size: 0.75rem;">
            ⚡ Plateforme moderne de gestion des formations • Version 1.0
        </p>
    </div>
</div>
""", unsafe_allow_html=True)