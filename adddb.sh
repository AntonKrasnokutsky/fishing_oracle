#!/bin/bash
#echo "Adding new MySQL database and user"

SUDO=''
if (( $EUID != 0 )); then
    SUDO='sudo'
fi

echo "Имя базы: "
read MAINDB

# replace "-" with "_" for database username
MAINDB=${MAINDB//[^a-zA-Z0-9]/_}

echo "Имя пользователя: "
read USERNAME

echo "Пароль пользователя базы: "
read -s PASSWDDB

# If /root/.my.cnf exists then it won't ask for root password
if [ -f /root/.my.cnf ]; then
    mysql -e "CREATE DATABASE ${MAINDB} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE UTF8_BIN;"
    mysql -e "CREATE USER ${USERNAME}@localhost IDENTIFIED BY '${PASSWDDB}';"
    mysql -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${USERNAME}'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"

# If /root/.my.cnf doesn't exist then it'll ask for root password   
else
    ${SUDO} mysql -uroot -e "CREATE DATABASE ${MAINDB} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE UTF8_BIN;"
    ${SUDO} mysql -uroot -e "CREATE USER ${USERNAME}@localhost IDENTIFIED BY '${PASSWDDB}';"
    ${SUDO} mysql -uroot -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${USERNAME}'@'localhost';"
    ${SUDO} mysql -uroot -e "FLUSH PRIVILEGES;"
fi

echo ""
echo "Создана база данных '${MAINDB}' и пользователь '${USERNAME}'."
echo ""
