import boto3
from botocore.exceptions import NoCredentialsError

try:
    # Crear un cliente S3 utilizando las credenciales y la configuración por defecto
    s3_client = boto3.client('s3')
    
    # Listar los buckets para verificar la conexión
    buckets = s3_client.list_buckets()
    
    # Si la llamada es exitosa, imprimir los nombres de los buckets
    print("Buckets S3 disponibles:")
    for bucket in buckets['Buckets']:
        print(f"- {bucket['Name']}")
except NoCredentialsError:
    print("No se pudieron encontrar las credenciales. Verifica tu configuración.")
except Exception as e:
    print(f"Se produjo un error: {e}")
