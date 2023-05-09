Pasos para iniciar con esta API:

1. Construimos los contenedores con el comando docker-compose up -d --build
2. Revisamos que los contenedores de la db y la web esten arriba con el comando docker ps
3. Revisamos que el API este arriba en la siguiente IP http://0.0.0.0:8000/
4. Entramos al contenedor donde corre Django ---> docker exec -it docker-django-postgres-main_web_1
5. Generamos el archivo de migraciones con el comando ---> python manage.py makemigrations
6. Corremos las migraciones con el comando ---> python manage.py migrate
7. Adicional si queremos tener acceso al Admin de Django podemos correr el comando ---> python manage.py createsuperuser
8. Para correr los test usamos el siguiente comando ---> python manage.py test
9. Abrimos la colección de POSTMAN y a probar los endpoints  https://soyangiezuniga.postman.co/workspace/Team-Workspace~8133bb1e-ef63-4702-8f48-1acbbe76ba0f/collection/9397232-a5428212-095d-4efa-9ea3-fa1666379db2?action=share&creator=9397232

Models:

- Article
- OrderItem
- Order 

Endpoints:

- Get Articles 
- Get Articles By ID
- Create Article
- Update Article

- Get Order
- Get Order By ID
- Create Order
- Update Order


 