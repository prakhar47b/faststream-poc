from os import environ as env

rabbit_protocol = env.get('RABBITMQ_PROTOCOL')
rabbit_host = env.get('RABBITMQ_HOST')
rabbit_port = env.get('RABBITMQ_PORT')
rabbit_user = env.get('RABBITMQ_USERNAME')
rabbit_pass = env.get('RABBITMQ_PASSWORD')
rabbit_url = f'{rabbit_protocol}://{rabbit_user}:{rabbit_pass}@{rabbit_host}:{rabbit_port}'
