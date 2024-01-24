# Puppet manifest to kill a process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  refreshonly => true,
  unless      => 'pgrep -f killmenow',
  path        => ['/usr/bin/pkill']
}
