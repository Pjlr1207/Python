API de Frutas 🥭🍓 - Proyecto básico con Flask

Esta es una pequeña API creada con Python y Flask que permite guardar frutas con un ID único y mostrar la lista en formato JSON. Es ideal para practicar desarrollo web básico y entender cómo funcionan las rutas en una API.

Lo que hace:
------------
- Muestra un mensaje de bienvenida en la ruta raíz "/"
- Permite agregar frutas usando "/agregar/nombre"
- Devuelve la lista completa en "/lista"

Ejemplos de uso:
----------------
1. Abres tu terminal y ejecutas:

   python app.py

2. En tu navegador, vas a:

   - http://127.0.0.1:5000/ → mensaje de bienvenida
   - http://127.0.0.1:5000/agregar/kiwi → añade una fruta llamada "kiwi"
   - http://127.0.0.1:5000/lista → muestra todas las frutas que agregaste

Cada fruta se guarda con un ID que aumenta automáticamente cada vez que se agrega una nueva.

Tecnologías usadas:
-------------------
- Python
- Flask
- Formato JSON para respuestas

Ideas para mejorarlo:
---------------------
- Guardar frutas en una base de datos (como SQL Server)
- Poder eliminar o editar frutas por ID
- Agregar seguridad o validaciones
- Conectar con un frontend para hacerlo visual

Autor:
------
Creado por Pablojavier con el apoyo de Microsoft Copilot 😄