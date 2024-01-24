import os

aws_directory = os.path.join(os.path.expanduser('~'), '.aws')
if not os.path.exists(aws_directory):
    os.makedirs(aws_directory)

credentials_path = os.path.join(aws_directory, 'credentials')

with open(credentials_path, 'w') as file:
    file.write('[default]\n')
    file.write('aws_access_key_id = access key aquí\n')
    file.write('aws_secret_access_key = secret access key aquí\n')

config_path = os.path.join(aws_directory, 'config')

with open(config_path, 'w') as file:
    file.write('[default]\n')
    file.write('region = sa-east-1\n')
