#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

cd superfluid

python manage.py collectstatic --no-input
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Godspower-Eze', 'Godspowereze260@gmail.com', 'Eminentfablous50')" | python manage.py shell


