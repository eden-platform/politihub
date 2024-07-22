#!bin/bash

if [ -d "/home/frappe/frappe-bench/apps/frappe" ]; then
    echo "Bench already exists, skipping init"
    cd frappe-bench
    bench start
else
    echo "Creating new bench..."
fi

bench init --skip-redis-config-generation frappe-bench

cd frappe-bench

# Use containers instead of localhost
bench set-mariadb-host mariadb
bench set-redis-cache-host redis:6379
bench set-redis-queue-host redis:6379
bench set-redis-socketio-host redis:6379

# Remove redis, watch from Procfile
sed -i '/redis/d' ./Procfile
sed -i '/watch/d' ./Procfile

bench get-app politihub

bench new-site politihub.localhost \
    --force \
    --mariadb-root-password 123 \
    --admin-password admin \
    --no-mariadb-socket

bench --site politihub.localhost install-app politihub
bench --site politihub.localhost set-config developer_mode 1
bench --site politihub.localhost clear-cache
bench --site politihub.localhost set-config mute_emails 1
bench --site politihub.localhost add-user alex@example.com --first-name Alex --last-name Scott --password 123 --user-type 'System User' --add-role 'Gameplan Admin'
bench use politihub.localhost

bench start
