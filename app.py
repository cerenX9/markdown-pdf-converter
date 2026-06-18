import streamlit as st
import markdown2
from xhtml2pdf import pisa
import io

st.set_page_config(
    page_title="Güvenli Markdown PDF Dönüştürücü",
    page_icon="📄",
    layout="wide"
)

st.title("🔐 Güvenli Markdown -> PDF Üretim Merkezi")
st.markdown("Yazılım Mühendisliği Standartlarında Yerel ve Canlı Uyumlu Proje.")

default_markdown = """# Kurumsal Proje Raporu
## Tarih: 18 Haziran 2026
### Yazar: Yazılım Mühendisi Adayı

Bu sistem internet üzerinde tamamen güvenli bir şekilde çalışmaktadır.

---

### 1. Sistem Güvenliği
* **SSL/TLS Şifreleme:** Verileriniz transfer edilirken şifrelenir.
* **Sunucusuz Mimari:** Girdiğiniz metinler sunucuda kalıcı olarak saklanmaz.

### 2. Mühendislik Çıktısı
Bu dökümanın altında otomatik olarak telif hakkı ibaresi yer almaktadır.
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
                }}
                body {{
                    font-family: Helvetica, Arial, sans-serif;
                    color: #1F2937;
                    line-height: 1.6;
                }}
                h1, h2, h3 {{ color: {accent_color}; }}
                h1 {{ font-size: 24pt; border-bottom: 1px solid {accent_color}; padding-bottom: 8px; }}
            </style>
        </head>
        <body>
            {html_body}
        </body>
        </html>
        '''
        
        try:
            # Bellekte (RAM) geçici bir sanal dosya oluşturuyoruz (Mühendislik yaklaşımı)
            pdf_buffer = io.BytesIO()
            pisa_status = pisa.CreatePDF(full_html, dest=pdf_buffer)
            
            if not pisa_status.err:
                st.success("🎉 PDF Başarıyla Hazırlandı!")
                pdf_bytes = pdf_buffer.getvalue()
                
                st.download_button(
                    label="📥 PDF'i Güvenli İndir",
                    data=pdf_bytes,
                    file_name="guvenli_muhendislik_raporu.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("PDF oluşturulurken bir hata oluştu.")
        except Exception as e:
            st.error(f"Hata: {e}")