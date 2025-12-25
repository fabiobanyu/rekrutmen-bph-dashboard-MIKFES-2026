import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman agar lebar (wide mode)
st.set_page_config(page_title="Dashboard Rekrutmen BPH", layout="wide")

st.title("📊 Visualisasi Data Rekrutmen BPH 2024")
st.markdown("---")

# Menggunakan kolom untuk menampilkan 2 dashboard berdampingan
col1, col2 = st.columns(2)

# Embed Code Dashboard 1
with col1:
    st.subheader("📌 Dashboard 1: Analisis Departemen")
    html_temp_1 = """
    <div class='tableauPlaceholder' id='viz1766645026234' style='position: relative'>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='Dashboard1_17666440637870/Dashboard1' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Da/Dashboard1_17666440637870/Dashboard1/1.png' /> 
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1766645026234');
        var vizElement = divElement.getElementsByTagName('object')[0];
        vizElement.style.width='100%';vizElement.style.height='800px';
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(html_temp_1, height=800)

# Embed Code Dashboard 2
with col2:
    st.subheader("📌 Dashboard 2: Analisis Divisi")
    html_temp_2 = """
    <div class='tableauPlaceholder' id='viz1766645104693' style='position: relative'>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='Dashboard2_17666439989780/Dashboard2' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Da/Dashboard2_17666439989780/Dashboard2/1.png' /> 
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1766645104693');
        var vizElement = divElement.getElementsByTagName('object')[0];
        vizElement.style.width='100%';vizElement.style.height='800px';
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(html_temp_2, height=800)

st.markdown("---")
st.caption("Data disajikan secara real-time dari Tableau Public.")