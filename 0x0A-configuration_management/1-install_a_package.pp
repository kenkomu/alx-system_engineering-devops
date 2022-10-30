# install flask from pip3.
exec { 'install python packages':
    ensure  => '0.8.1',
    command => 'pip3 install flask flask_restful apiai',
    }