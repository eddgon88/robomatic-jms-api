import pika


class Sender:
    @staticmethod
    def sendqueue(config):        
        try:
            params = pika.URLParameters(f'{config["engine"]}://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}')
            params.socket_timeout = 5

            connection = pika.BlockingConnection(params) # Connect to CloudAMQP
            channel = connection.channel() # start a channel
            channel.queue_declare(queue=config['queueName']) # Declare a queue
            # send a message

            channel.basic_publish(exchange='', routing_key=config['queueName'], body=str(config['message']))
            print ("[x] Message sent to consumer")
            connection.close()
        except Exception as e:
            print(e.with_traceback)
            print(format(e))
            return str(format(e))
        return "Queue sended succesfuly"