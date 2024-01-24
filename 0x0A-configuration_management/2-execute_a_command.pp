# Puppet manifest to kill a process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  path        => ['/usr/bin/pkill']
}
