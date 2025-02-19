#!/bin/bash

set -e

# Espera a que PostgreSQL esté disponible
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_SERVER" -U "$POSTGRES_USER" -c '\q'; do
    echo "Esperando a que PostgreSQL esté listo..."
    sleep 3
done

# Espera a que la base de datos "lyrics" esté creada
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_SERVER" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
    echo "Esperando a que la base de datos 'lyrics' esté disponible..."
    sleep 3
done

echo "Base de datos lista, ejecutando migraciones..."

python manage.py makemigrations
python manage.py migrate
# Creación de un superusuario
# DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username=admin --email=admin@admin.com --noinput

# Creación de un superusuario (si no existe)
if ! python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='admin').exists())" | grep -q 'True'; then
    DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username=admin --email=admin@admin.com --noinput
fi

python manage.py runserver 0.0.0.0:8000