#!/usr/bin/env python
import pika
import time
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def printHello():
    time.sleep()
    return "Hello world from function"

channel.basic_publish(exchange='', routing_key='hello', body=printHello())
connection.close()