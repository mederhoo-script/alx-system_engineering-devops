# error 500 fixed by chaning phpp to php

exec { 'replacing_phpp_with_php':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
