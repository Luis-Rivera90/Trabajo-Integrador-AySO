# 🖥️ Trabajo Práctico Integrador – Arquitectura y Sistemas Operativos

## 📌 Descripción
Este proyecto corresponde al **Trabajo Práctico Integrador de la materia Arquitectura y Sistemas Operativos**.  
El trabajo aborda dos ejes principales:

1. **Virtualización con VirtualBox y Ubuntu Server 24.04.3 LTS**, incluyendo instalación, configuración de red en modo Bridge, uso de snapshots, clonación de máquinas y acceso remoto vía SSH con PuTTY.  
2. **Desarrollo en Python** de un programa simple para **registro de usuarios** y **saludo personalizado**, como ejercicio de programación y prueba de integración con Git y GitHub.  

---

## 👨‍💻 Integrantes
- Luis Mariano Rivera Ortiz  
- Gustavo Hernan Campestre  

Profesor: Emmanuel Avellaneda  
Fecha de entrega: 03/10/2025  

---

## ⚙️ Tecnologías Utilizadas
- **VirtualBox** (Hipervisor de tipo 2)  
- **Ubuntu Server 24.04.3 LTS** (Sistema operativo invitado)  
- **PuTTY** (Cliente SSH)  
- **Python 3** (Lenguaje de programación)  
- **Git & GitHub** (Control de versiones y colaboración)  

---

## 📂 Estructura del Proyecto
📦 TrabajoPracticoIntegradorAySO
┣ 📜 programa.py # Programa en Python para registro de usuarios
┣ 📜 README.md # Documentación del proyecto
┗ 📂 /docs # Informe técnico, capturas y notas

---

## 🐍 Programa en Python
El archivo `program.py` permite:
- Registrar usuarios mediante **nombre y apellido**.  
- Validar que solo se ingresen caracteres alfabéticos.  
- Mostrar la lista completa de usuarios registrados.  
- Seleccionar un índice de usuario para mostrar un saludo personalizado.  

### 🔧 Ejecución
```bash
python3 programa.py

=== Registro de usuarios ===
Ingrese el nombre: Luis
Ingrese el apellido: Rivera
¿Desea ingresar otro usuario? (s/n): s
Ingrese el nombre: Gustavo
Ingrese el apellido: Campestre
¿Desea ingresar otro usuario? (s/n): n

=== Lista de usuarios registrados ===
0: Luis Rivera
1: Gustavo Campestre

Ingrese el número de índice para saludar: 1
¡Hola Gustavo Campestre!


