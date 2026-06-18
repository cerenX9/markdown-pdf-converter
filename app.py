import streamlit as st
import markdown2
from weasyprint import HTML

st.set_page_config(
    page_title="Güvenli Markdown PDF Dönüştürücü",
    page_icon="📄",
    layout="wide"
)

# Arayüz Stili
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stButton>button {
        width: 100%;
        background-color: #059669;
        color: white;
        border-radius: 0.5rem;
        border: none;
        padding: 0.75rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Güvenli Markdown -> PDF Üretim Merkezi")
st.markdown("Yazılım Mühendisliği Standartlarında, CSS Paged Media Destekli Canlı Proje.")

default_markdown = """# Kurumsal Proje Raporu
## Tarih: 18 Haziran 2026
### Yazar: Yazılım Mühendisi Adayı

Bu sistem internet üzerinde tamamen güvenli bir şekilde çalışmaktadır.

---

### 1. Sistem Güvenliği
* **SSL/TLS Şifreleme:** Verileriniz transfer edilirken şifrelenir.
* **Sunucusuz Mimari:** Girdiğiniz metinler sunucuda kalıcı olarak saklanmaz, anlık üretilir.

### 2. Mühendislik Çıktısı
Bu dökümanın altında otomatik olarak sayfa numarası ve telif hakkı ibaresi yer almaktadır.
"""

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Markdown Editörü")
    user_markdown = st.text_area("İçeriğinizi yazın:", value=default_markdown, height=450)

with col2:
    st.subheader("🎨 PDF Stil Ayarları")
    accent_color = st.color_picker("Başlık Rengi", "#059669")
    bg_color = st.color_picker("Arka Plan Rengi", "#FFFFFF")
    
    st.markdown("---")
    st.subheader("🚀 Çıktı İşlemleri")
    
    if st.button("Güvenli PDF Oluştur"):
        html_body = markdown2.markdown(user_markdown)
        
        # Yenilenen CSS: Alt bilgi (footer) ve sayfa numarası eklendi
        full_html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                @page {{
                    size: A4;
                    margin: 25mm 20mm;
                    background-color: {bg_color};
                    @bottom-left {{
                        content: "© 2026 Tüm Hakları Saklıdır. | Güvenli Rapor Sistemi";
                        font-family: Arial, sans-serif;
                        font-size: 8pt;
                        color: #9CA3AF;
                    }}
                    @bottom-right {{
                        content: "Sayfa " counter(page) " / " counter(pages);
                        font-family: Arial, sans-serif;
                        font-size: 8pt;
                        color: #9CA3AF;
                    }}
                }}
                body {{
                    font-family: "Times New Roman", Times, serif;
                    color: #1F2937;
                    line-height: 1.6;
                    font-size: 11pt;
                }}
                h1, h2, h3 {{ color: {accent_color}; font-family: Arial, sans-serif; }}
                h1 {{ font-size: 24pt; border-bottom: 2px solid {accent_color}; padding-bottom: 8px; }}
            </style>
        </head>
        <body>
            {html_body}
        </body>
        </html>
        '''
        
        try:
            pdf_filename = "secure_output.pdf"
            HTML(string=full_html).write_pdf(pdf_filename)
            st.success("🎉 PDF Başatıyla Hazırlandı!")
            
            with open(pdf_filename, "rb") as f:
                pdf_bytes = f.read()
                
            st.download_button(
                label="📥 PDF'i Güvenli İndir",
                data=pdf_bytes,
                file_name="guvenli_muhendislik_raporu.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Hata: {e}")