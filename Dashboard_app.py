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
# CUSTOM CSS
# =============================
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1f2937;
    }
    .sub-title {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 20px;
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.06);
        margin-bottom: 30px;
    }
    iframe {
        border-radius: 14px;
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
    st.markdown("<div class='sub-title'>Visualisasi data interaktif berbasis Tableau Public yang diintegrasikan ke dalam website menggunakan Streamlit.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
            <h3>🎯 Tujuan</h3>
            <p>
            Website ini bertujuan untuk menyajikan hasil analisis data dalam bentuk dashboard interaktif,
            sehingga pengguna dapat melakukan eksplorasi data secara mandiri.
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
        Visualisasi disusun dari yang paling banyak hingga paling sedikit dipilih.
        </p>
    </div>
    """, unsafe_allow_html=True)

    dashboard1 = """
    <iframe src="https://public.tableau.com/views/Dashboard1_17666440637870/Dashboard2?:showVizHome=no"
            width="100%"
            height="850">
    </iframe>
    """

    st.components.v1.html(dashboard1, height=900)

# =============================
# DASHBOARD 2
# =============================
elif menu == "📈 Dashboard 2":
    st.markdown("<div class='section-title'>📈 Dashboard 2 – Analisis Lanjutan</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <p>
        Dashboard ini menyajikan analisis tambahan yang mendukung pengambilan keputusan
        dengan pendekatan visual yang lebih eksploratif.
        </p>
    </div>
    """, unsafe_allow_html=True)

    dashboard2 = """
    <iframe src="https://public.tableau.com/views/Dashboard2_17666439989780/Dashboard2?:showVizHome=no"
            width="100%"
            height="850">
    </iframe>
    """

    st.components.v1.html(dashboard2, height=900)
