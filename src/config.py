from os import environ as env

rabbit_protocol = env.get('RABBITMQ_PROTOCOL', 'amqp')
rabbit_host = env.get('RABBITMQ_HOST', 'localhost')
rabbit_port = env.get('RABBITMQ_PORT', '5672')
rabbit_user = env.get('RABBITMQ_USERNAME', 'guest')
rabbit_pass = env.get('RABBITMQ_PASSWORD', 'guest')
rabbit_url = f'{rabbit_protocol}://{rabbit_user}:{rabbit_pass}@{rabbit_host}:{rabbit_port}'

batch_size = int(env.get('BATCH_SIZE', '100'))
worker_0_process_time = int(env.get('WORKER_0_PROCESS_TIME', '5'))
worker_1_process_time = int(env.get('WORKER_1_PROCESS_TIME', '10'))
worker_2_process_time = int(env.get('WORKER_2_PROCESS_TIME', '5'))
