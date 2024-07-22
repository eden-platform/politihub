#!/bin/bash
set -e
cd ~ || exit

echo "Setting Up Bench..."

pip install frappe-bench
bench -v init frappe-bench --skip-assets --python "$(which python)"
cd ./frappe-bench || exit

bench -v setup requirements

echo "Setting Up PolitiHub App..."
bench get-app politihub "${GITHUB_WORKSPACE}"

echo "Setting Up Sites & Database..."

mkdir ~/frappe-bench/sites/politihub.test
cp "${GITHUB_WORKSPACE}/.github/helper/site_config.json" ~/frappe-bench/sites/politihub.test/site_config.json

mariadb --host 127.0.0.1 --port 3306 -u root -p123 -e "SET GLOBAL character_set_server = 'utf8mb4'";
mariadb --host 127.0.0.1 --port 3306 -u root -p123 -e "SET GLOBAL collation_server = 'utf8mb4_unicode_ci'";

mariadb --host 127.0.0.1 --port 3306 -u root -p123 -e "CREATE DATABASE test_politihub";
mariadb --host 127.0.0.1 --port 3306 -u root -p123 -e "CREATE USER 'test_politihub'@'localhost' IDENTIFIED BY 'test_politihub'";
mariadb --host 127.0.0.1 --port 3306 -u root -p123 -e "GRANT ALL PRIVILEGES ON \`test_politihub\`.* TO 'test_politihub'@'localhost'";

mariadb --host 127.0.0.1 --port 3306 -u root -p123 -e "FLUSH PRIVILEGES";


echo "Setting Up Procfile..."

sed -i 's/^watch:/# watch:/g' Procfile
sed -i 's/^schedule:/# schedule:/g' Procfile

echo "Setting up redisearch module..."
echo "loadmodule ${GITHUB_WORKSPACE}/.github/helper/redisearch.so" >> ./config/redis_cache.conf
chmod +x "${GITHUB_WORKSPACE}/.github/helper/redisearch.so"
cat ./config/redis_cache.conf

echo "Starting Bench..."

bench start &> bench_start.log &

CI=Yes bench build &
build_pid=$!

bench --site politihub.test reinstall --yes
bench --site politihub.test install-app politihub
bench --site politihub.test execute politihub.search.build_index_if_not_exists

# wait till assets are built succesfully
wait $build_pid
