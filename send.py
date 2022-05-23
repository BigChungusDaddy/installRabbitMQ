import pika
import sys

credential = pika.PlainCredentials('node1', 'thisisnode1')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.2',credentials=credential))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable = True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
exchange='', 
routing_key='task_queue', 
body=message, 
properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

print(" [x] Sent %r" % message)
connection.close()


