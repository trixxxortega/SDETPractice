# Usa una imagen base compatible con ARM64
FROM --platform=linux/arm64 python:3.11-slim

# Evita prompts de instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    gnupg \
    ca-certificates \
    chromium \
    chromium-driver \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Configura el alias para Chromium como si fuera Google Chrome
RUN ln -s /usr/bin/chromium /usr/bin/google-chrome

# Copia el archivo de requerimientos e instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu código al contenedor
COPY . /app
WORKDIR /app

# Comando por defecto al iniciar el contenedor (ajustalo si usás otro)
CMD ["python", "tu_script.py"]