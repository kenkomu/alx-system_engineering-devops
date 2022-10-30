# install flask from pip3.
exec { 'install python packages':
    ensure  => '0.8.1',
    path    => ['/usr/bin/'],
    unless  => '/usr/bin/test -f /usr/local/lib/python3.4/dist-packages/flask/app.py'

    command => 'pip3 install flask flask_restful apiai',
    }