import streamlit as st

# =============================
# CONFIG
# =============================
st.set_page_config(
    page_title="Interactive Tableau Dashboard",
    page_icon="📊",
    layout="wide"
)

# =============================
# CUSTOM CSS (STABIL & AMAN)
# =============================
st.markdown("""
<style>
/* Global */
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Title */
.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #f9fafb;
}
.sub-title {
    font-size: 17px;
    color: #d1d5db;
    margin-bottom: 40px;
}

/* Section */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #f9fafb;
}

/* Card */
.card {
    background-color: #111827;
    padding: 24px;
    border-radius: 14px;
    border: 1px solid #1f2937;
    margin-bottom: 30px;
}

/* Tableau wrapper */
.tableau-wrapper {
    background-color: #ffffff;
    border-radius: 14px;
    padding: 10px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #020617;
}
</style>
""", unsafe_allow_html=True)

# =============================
# SIDEBAR
# =============================
st.sidebar.title("📊 Navigasi Dashboard")

menu = st.sidebar.radio(
    "Pilih Tampilan:",
    ["🏠 Beranda", "📌 Dashboard 1", "📈 Dashboard 2"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Dibuat dengan:**")
st.sidebar.markdown("- Tableau Public")
st.sidebar.markdown("- Streamlit")
st.sidebar.markdown("- Python")

# =============================
# BERANDA
# =============================
if menu == "🏠 Beranda":
    st.markdown("<div class='main-title'>Dashboard Interaktif Tableau</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='sub-title'>Visualisasi data interaktif berbasis Tableau Public yang diintegrasikan menggunakan Streamlit.</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class='card'>
            <h3>🎯 Tujuan</h3>
            <p>
            Website ini bertujuan menyajikan hasil analisis data dalam bentuk dashboard interaktif
            agar pengguna dapat melakukan eksplorasi data secara mandiri.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <h3>🛠 Teknologi</h3>
            <ul>
                <li>Tableau Public</li>
                <li>Streamlit</li>
                <li>Python</li>
                <li>GitHub</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# =============================
# DASHBOARD 1
# =============================
elif menu == "📌 Dashboard 1":
    st.markdown("<div class='section-title'>📌 Dashboard 1 – Pilihan Departemen & Divisi</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <p>
        Dashboard ini menampilkan distribusi pilihan departemen dan divisi berdasarkan preferensi responden.
        Urutan visualisasi disusun dari jumlah terbanyak hingga paling sedikit.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tableau-wrapper">
        <iframe 
            src="https://public.tableau.com/views/Dashboard1_17666440637870/Dashboard2?:showVizHome=no"
            width="100%"
            height="900"
            frameborder="0">
        </iframe>
    </div>
    """, unsafe_allow_html=True)

# =============================
# DASHBOARD 2
# =============================
elif menu == "📈 Dashboard 2":
    st.markdown("<div class='section-title'>📈 Dashboard 2 – Analisis Lanjutan</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <p>
        Dashboard ini menyajikan analisis lanjutan untuk mendukung pengambilan keputusan
        dengan pendekatan visual yang lebih eksploratif.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tableau-wrapper">
        <iframe 
            src="https://public.tableau.com/views/Dashboard2_17666439989780/Dashboard2?:showVizHome=no"
            width="100%"
            height="900"
            frameborder="0">
        </iframe>
    </div>
    """, unsafe_allow_html=True)
