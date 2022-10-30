#create a file in /tmp.

file { '/tmp/school':
  ensure => symlink,
  target => /tmp/school,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744',
  info   => 'I love Puppet'
}