# create a manifest that kills a process named killmenow
exec { 'Kill':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
