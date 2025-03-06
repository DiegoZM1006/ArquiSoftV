from azure.servicebus import ServiceBusClient


CONNECTION_STR = "tu_connection_string"
QUEUES = ["high-priority-queue", "medium-priority-queue", "low-priority-queue"]

def receive_messages():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        for queue_name in QUEUES:
            with client.get_queue_receiver(queue_name) as receiver:
                while True:  
                    messages = receiver.receive_messages(max_message_count=5, max_wait_time=5)
                    if not messages:
                        break
                    for message in messages:
                        content = "".join([bytes(b).decode("utf-8") for b in message.body]) if hasattr(message.body, "_iter_") else str(message.body)
                        print(f"📩 Recibido de {queue_name}: {content}")
                        receiver.complete_message(message) 
receive_messages()
