# 1. Base Image: Python 3.9'un hafif sürümü
FROM python:3.9-slim

# 2. Çalışma dizinini ayarla
WORKDIR /app

# 3. Önce requirements dosyasını kopyala (Cache optimizasyonu için)
COPY requirements.txt .

# 4. Kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kalan proje dosyalarını kopyala
COPY . .

# 6. Flask'in çalıştığı portu dışarıya bildir
EXPOSE 5000

# 7. Uygulamayı başlat
CMD ["python", "app.py"]
