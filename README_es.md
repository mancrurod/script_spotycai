# 🎵 Spotycai Song Downloader

**Spotycai Song Downloader** es una herramienta de automatización basada en Python que permite descargar álbumes completos desde Spotycai, extraer metadatos e incrustar carátulas en archivos MP3, todo desde un único script.

Este proyecto utiliza **Selenium WebDriver** para navegar por la web de Spotycai, automatizar descargas y etiquetar archivos MP3 con `eyeD3`. Está pensado para usuarios que quieren organizar su biblioteca musical de forma eficiente y sin esfuerzo manual.

---

## 🚀 Funcionalidades

- 🔎 Raspado automatizado de páginas de álbumes en Spotycai
- 💽 Descarga masiva de MP3 por álbum
- 🖼️ Inserción de carátulas y metadatos (etiquetado ID3)
- 📁 Organización en carpetas por artista y nombre de álbum
- 🧑‍💻 Modo headless (sin interfaz) para ejecución silenciosa

---

## 🧰 Tecnologías utilizadas

- `Python 3.10+`
- `Selenium` para automatización de navegador
- `eyeD3` para etiquetado de archivos MP3
- `requests`, `os`, `time`, `re` y librerías estándar

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/mancrurod/script_spotycai.git
cd script_spotycai
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Instala [ChromeDriver](https://sites.google.com/chromium.org/driver/) y asegúrate de que coincida con tu versión de Chrome.

---

## ⚙️ Cómo usar

1. Ejecuta el script:

```bash
python script.py
```

2. Introduce la URL del álbum de Spotycai cuando se te solicite.

3. Espera a que finalice el proceso de descarga y etiquetado.

> Nota: Asegúrate de que el sitio web está disponible en tu región y que Chrome esté correctamente configurado.

---

## 📁 Estructura de salida

```
downloads/
└── Nombre del Artista/
    └── Nombre del Álbum/
        ├── 01 - Nombre de pista.mp3
        ├── 02 - Nombre de pista.mp3
        └── cover.jpg
```

---

## 📌 Notas

- Esta herramienta está pensada para uso educativo y personal.
- Spotycai es un sitio web de terceros. Usa la herramienta de forma responsable y respeta las leyes de derechos de autor.

---

## 👨‍💻 Autor

Desarrollado por **Manuel Cruz Rodríguez**  
[LinkedIn](https://www.linkedin.com/in/mancrurod/) · [GitHub](https://github.com/mancrurod)

---

## 📘 Licencia

Este proyecto está bajo la licencia MIT.