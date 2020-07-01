#!/bin/bash
#echo "Adding new MySQL database and user"

SUDO=''
if (( $EUID != 0 )); then
    SUDO='sudo'
fi

echo "Имя базы: "
#read MAINDB
MAINDB=h9d1v8

# replace "-" with "_" for database username
MAINDB=${MAINDB//[^a-zA-Z0-9]/_}

echo "Имя пользователя: "
#read USERNAME
USERNAME=h7dhr

echo "Пароль пользователя базы: "
#read -s PASSWDDB
PASSWDDB=h6iHjLc4

# If /root/.my.cnf exists then it won't ask for root password
if [ -f /root/.my.cnf ]; then
    mysql -e "REVOKE ALL PRIVILEGES, GRANT OPTION FROM ${USERNAME}@localhost;"
    mysql -e "DROP USER ${USERNAME}@localhost;"
    mysql -e "DROP DATABASE ${MAINDB};"
    mysql -e "CREATE DATABASE ${MAINDB} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE UTF8_BIN;"
    mysql -e "CREATE USER ${USERNAME}@localhost IDENTIFIED BY '${PASSWDDB}';"
#    mysql -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${USERNAME}'@'localhost';"
    mysql -e "GRANT ALL PRIVILEGES ON *.* TO '${USERNAME}'@'loca
lhost';"
    mysql -e "FLUSH PRIVILEGES;"

# If /root/.my.cnf doesn't exist then it'll ask for root password   
else
    ${SUDO} mysql -uroot -e "REVOKE ALL PRIVILEGES, GRANT OPTION FROM ${USERNAME}@localhost;"
    ${SUDO} mysql -uroot -e "DROP USER ${USERNAME}@localhost;"
    ${SUDO} mysql -uroot -e "DROP DATABASE ${MAINDB};"
    ${SUDO} mysql -uroot -e "CREATE DATABASE ${MAINDB} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE UTF8_BIN;"
    ${SUDO} mysql -uroot -e "CREATE USER ${USERNAME}@localhost IDENTIFIED BY '${PASSWDDB}';"
#    ${SUDO} mysql -uroot -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${USERNAME}'@'localhost';"
    ${SUDO} mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO '${USERNAME}'@'localhost';"
    ${SUDO} mysql -uroot -e "FLUSH PRIVILEGES;"
fi

echo ""
echo "Создана база данных '${MAINDB}' и пользователь '${USERNAME}'."
echo ""
