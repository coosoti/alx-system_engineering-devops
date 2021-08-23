# Puppet Manifest to configure custom Nginx Response Header

package { 'nginx':
  ensure => 'installed',
}

file_line { 'add_header':
  ensure  => 'present',
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => 'add_header X-Served-By $HOSTNAME;',
  notify  =>  Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['add_header'],
}