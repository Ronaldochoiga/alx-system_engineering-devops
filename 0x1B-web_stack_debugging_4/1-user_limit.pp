# This is a puppet script that allows to make changes on login to holberton

exec {'/usr/bin/env sed -i "s/holberton/foo" /etc/security/limits.config': }