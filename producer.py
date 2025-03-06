from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Configuración
CONNECTION_STR = "tu_connection_string"

QUEUES = {
    "1": "high-priority-queue",
    "2": "medium-priority-queue",
    "3": "low-priority-queue"
}

def send_message():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        while True:
            print("\n📩 ¿A qué cola quieres enviar el mensaje?")
            print("1. 🔴 Alta Prioridad")
            print("2. 🟡 Media Prioridad")
            print("3. 🟢 Baja Prioridad")
            print("4. 🚪 Salir")

            choice = input("Selecciona una opción (1-4): ").strip()

            if choice == "4":
                print("👋 Saliendo...")
                break
            elif choice not in QUEUES:
                print("❌ Opción no válida. Intenta de nuevo.")
                continue
            
            message_content = input("Escribe el mensaje: ").strip()
            queue_name = QUEUES[choice]

            sender = client.get_queue_sender(queue_name)
            message = ServiceBusMessage(message_content)
            sender.send_messages(message)
            print(f"📤 Enviado a {queue_name}: {message_content}")

if __name__ == "__main__":
    send_message()
