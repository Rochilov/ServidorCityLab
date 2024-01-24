# CityLabServer
Servidor intermediario entre S3 y aplicacion Android

1. Configuración del entorno virtual:
python -m venv server

3. Activar el entorno virtual
-En Windows: server\Scripts\activate
-En macOS y Linux: source server/bin/activate

5. Instalar dependencias:
pip install -r requirements.txt

4. Iniciar servidor:
uvicorn main:app --reload

5. Para ingresar las credenciales, edita 'configuracion.py' y reemplaza las credenciales en 'file.write('aws_access_key_id = access key aquí\n')' y file.write('aws_secret_access_key = secret access key aquí\n'), luego ejecuta
