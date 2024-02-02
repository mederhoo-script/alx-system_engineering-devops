# Add a custom HTTP header with Puppet

exec {'update':
  provider => shell,
  command => 'sudo apt-get -y update',
  before => Exec[]
}
