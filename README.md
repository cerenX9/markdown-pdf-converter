# 📄 Gelişmiş Markdown to PDF Dönüştürücü

Metin işleme (parsing), dinamik stil yönetimi ve yazdırılabilir döküman standartlarını (CSS Paged Media) barındıran full-stack bir otomasyon aracıdır.

🚀 **Canlı Demo Linki:** [http://172.20.10.8:8501]

---
--------------------------------------------------------------------------------------------------------
# 🚀🚀🚀🚀LİNK İLE UYGULAMAYA GİRİŞ YAP 🚀🚀🚀🚀

https://markdown-pdf-converter-ezn3i95izf832goz5zstt6.streamlit.app/

--------------------------------------------------------------------------------------------------------
---

## 🛠️ Kullanılan Teknolojiler ve Araçlar

* **Dil:** Python 3.x
* **Arayüz (Frontend):** [Streamlit](https://streamlit.io/) (Hızlı ve reaktif web arayüz bileşenleri için)
* **Metin İşleme (Parser):** [Markdown2](https://github.com/trentm/python-markdown2) (Markdown formatını standart HTML yapılarına dönüştürmek için)
* **PDF Motoru (Rendering):** [WeasyPrint](https://weasyprint.org/) (HTML + CSS kodlarını A4 standartlarında yüksek kaliteli PDF'e dönüştürmek için)
* **Tasarım Standartları:** CSS Paged Media (`@page` kuralları, dinamik sayfa numaralandırma ve footer yönetimi)

---

## 💡 Kazanılan Yazılım Mühendisliği Yetkinlikleri

Bu projeyi geliştirirken aşağıdaki mimari ve mühendislik pratikleri uygulanmıştır:
1.  **Modüler Sistem Tasarımı:** Kullanıcı girdisi (Markdown), stil parametreleri (CSS) ve çıktı motorunun (WeasyPrint) birbirinden bağımsız ve uyumlu çalışması sağlandı.
2.  **CSS Paged Media Standartları:** Dijital dökümanların matbaa/yazdırma standartlarına uygun hale getirilmesi için `@page` seçicileri, `counter(page)` ile dinamik sayfa numaralandırma ve alt bilgi (footer) yönetimi uygulandı.
3.  **Bulut Dağıtımı (Deployment) & Güvenlik:** Proje GitHub entegrasyonu ile Streamlit Community Cloud üzerinde canlıya alınmış, **HTTPS (SSL/TLS)** sertifikası ile güvenli veri transferi sağlanmıştır.

---

## 💻 Projeyi Yerel Bilgisayarınızda Çalıştırın

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/KULLANICI_ADIN/markdown-pdf-converter.git](https://github.com/KULLANICI_ADIN/markdown-pdf-converter.git)
cd markdown-pdf-converter
