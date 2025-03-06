# 📌 Priority Queue en la Nube con Azure Service Bus


🔗 [Acceder a la presentación en Canva](https://www.canva.com/design/DAGgrCQiCF0/-4B5w9wrXoAJoxkRpjvd6g/edit?utm_content=DAGgrCQiCF0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


## 📖 Introducción

En aplicaciones distribuidas, es común que los mensajes deban ser procesados en función de su importancia. Para ello, implementamos un sistema basado en Priority Queue utilizando Azure Service Bus.

Este patrón de diseño garantiza que los mensajes de alta prioridad sean procesados primero, optimizando la eficiencia del sistema. En este proyecto, desarrollamos un productor (producer.py) que envía mensajes a diferentes colas según su prioridad y un consumidor (consumer.py) que procesa los mensajes en orden de prioridad.

🎯 Objetivos

* Implementar un sistema de mensajería basado en prioridades.
* Utilizar Azure Service Bus para gestionar las colas.
* Garantizar que los mensajes más urgentes sean procesados antes.
* Demostrar la correcta funcionalidad del patrón de diseño Priority Queue.

## 🚀 Cómo Ejecutar el Proyecto

### 🔧 Prerrequisitos

1. Tener instalado Python 3.8+.

2. Instalar las dependencias necesarias ejecutando:

    ```bash
    pip install azure-servicebus
    ```

3. Contar con una instancia de Azure Service Bus y configurar correctamente las colas.

4. Configurar la conexión a Azure Service Bus:

    * En los archivos producer.py y consumer.py, ubica la variable CONNECTION_STR.
    * Reemplázala con la cadena de conexión de tu instancia de Azure Service Bus:
    ```bash
    CONNECTION_STR = "tu_cadena_de_conexion_a_azure"
    ```


### Paso 1: Ejecutar el Productor

El productor envía mensajes a la cola seleccionada según su prioridad:

```bash
python producer.py
```

El script te pedirá elegir la prioridad del mensaje:

```
📩 ¿A qué cola quieres enviar el mensaje?
1. 🔴 Alta Prioridad
2. 🟡 Media Prioridad
3. 🟢 Baja Prioridad
4. 🚪 Salir
```

Luego, escribe el contenido del mensaje y este será enviado a la cola correspondiente en Azure Service Bus.

### Paso 2: Ejecutar el Consumidor

El consumidor procesa los mensajes en el siguiente orden:

* **1️** Alta Prioridad
* **2️** Media Prioridad
* **3️** Baja Prioridad

Para iniciar el consumidor, ejecuta:

```bash
python consumer.py
```

El sistema leerá y procesará los mensajes en función de su prioridad, asegurando que los más urgentes sean atendidos primero.

## 🔍 Funcionalidades del Sistema

### 📨 Productor (producer.py)

* ✅ Permite enviar mensajes a tres colas de prioridad.
* ✅ Garantiza que cada mensaje se asigne a la cola correcta.
* ✅ Facilita la interacción con el usuario mediante un menú intuitivo.

### 📥 Consumidor (consumer.py)

* ✅ Procesa los mensajes de alta prioridad antes que los de menor prioridad.
* ✅ Maneja múltiples colas de forma eficiente.
* ✅ Confirma la recepción y procesamiento de cada mensaje en Azure Service Bus.

## 📌 Beneficios del Patrón Priority Queue

* **Optimización del rendimiento**: Procesa primero las tareas críticas.
* **Escalabilidad**: Puede manejar una gran cantidad de mensajes sin afectar el rendimiento.
* **Fiabilidad**: Usa Azure Service Bus para asegurar la entrega y procesamiento de mensajes.
* **Flexibilidad**: Se puede integrar fácilmente en arquitecturas distribuidas.

## 🎯 Conclusión

Este proyecto demuestra cómo implementar el patrón Priority Queue en la nube utilizando Azure Service Bus. Gracias a esta arquitectura, los sistemas pueden priorizar tareas de manera eficiente y escalable.