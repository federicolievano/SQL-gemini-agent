# 🗄️ SQL Query Assistant

Una aplicación simple y elegante que convierte preguntas en lenguaje natural a consultas SQL usando LangChain, Gemini y Streamlit.

## ✨ Características

- **Consulta en lenguaje natural**: Pregunta lo que quieras saber sobre tus datos
- **Generación automática de SQL**: Gemini convierte tu pregunta a consultas SQL
- **Ejecución directa**: Ejecuta las consultas en tu base de datos MySQL
- **Visualización de resultados**: Ve los datos en tablas interactivas
- **Descarga de resultados**: Exporta los datos a CSV
- **Información de esquema**: Explora la estructura de tu base de datos

## 🚀 Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno
Edita el archivo `config.py` con tu información:

```python
# En config.py, actualiza estos valores:
DB_PASSWORD = 'tu_contraseña_de_mysql'
GEMINI_API_KEY = 'tu_api_key_de_gemini'
```

### 3. Obtener API Key de Gemini
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea una nueva API key
3. Cópiala en `config.py`

## 🎯 Uso

### 1. Ejecutar la aplicación
```bash
streamlit run app.py
```

### 2. Hacer preguntas
- Escribe tu pregunta en lenguaje natural
- Ejemplo: "Muéstrame todos los actores de la película 'Jaws'"
- Haz clic en "Generate SQL Query"

### 3. Ejecutar consultas
- Revisa el SQL generado
- Haz clic en "Execute Query"
- Ve los resultados en la tabla

## 📊 Base de datos

La aplicación está configurada para usar la base de datos **Sakila** (incluida con MySQL). Si quieres usar otra base de datos:

1. Cambia `DB_NAME` en `config.py`
2. Ajusta el prompt en `app.py` para que conozca tu esquema

## 🔧 Estructura del proyecto

```
├── app.py              # Aplicación principal de Streamlit
├── database.py         # Funciones de conexión a base de datos
├── config.py           # Configuración y variables de entorno
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## 💡 Ejemplos de preguntas

- "¿Cuántas películas hay en cada categoría?"
- "Muéstrame los actores más populares"
- "¿Cuáles son las películas más rentadas?"
- "Encuentra clientes que han rentado más de 10 películas"

## 🛠️ Solución de problemas

### Error de conexión a MySQL
- Verifica que MySQL esté ejecutándose
- Confirma usuario y contraseña en `config.py`
- Asegúrate de que la base de datos exista

### Error de API Key
- Verifica que tu API key de Gemini sea válida
- Confirma que tienes créditos disponibles en tu cuenta

### Error de dependencias
- Ejecuta `pip install -r requirements.txt`
- Verifica que estés en el entorno virtual correcto

## 📱 Interfaz

La aplicación tiene una interfaz intuitiva con:
- **Panel izquierdo**: Información de la base de datos
- **Panel central**: Entrada de preguntas y resultados
- **Panel derecho**: SQL generado y botones de acción

## 🔒 Seguridad

- Nunca compartas tu API key
- Usa contraseñas seguras para MySQL
- Considera usar variables de entorno para producción

## 📈 Próximas mejoras

- [ ] Soporte para múltiples bases de datos
- [ ] Historial de consultas
- [ ] Gráficos automáticos de resultados
- [ ] Exportación a más formatos
- [ ] Autocompletado de preguntas

---

¡Disfruta explorando tus datos con lenguaje natural! 🎉 