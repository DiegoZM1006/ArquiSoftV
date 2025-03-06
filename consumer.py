from azure.servicebus import ServiceBusClient

# Configuración
CONNECTION_STR = "tu_connection_string"
QUEUES = ["high-priority-queue", "medium-priority-queue", "low-priority-queue"]

def receive_messages():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        for queue_name in QUEUES:  # Procesa primero High, luego Medium, luego Low
            with client.get_queue_receiver(queue_name) as receiver:
                for message in receiver.receive_messages(max_message_count=5, max_wait_time=5):
                    content = "".join([bytes(b).decode("utf-8") for b in message.body]) if hasattr(message.body, "__iter__") else str(message.body)
                    print(f"📩 Recibido de {queue_name}: {content}")
                    receiver.complete_message(message)  # Marcar mensaje como procesado

receive_messages()
