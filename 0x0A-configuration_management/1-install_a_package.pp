package { 'python3-flask':
  ensure   => installed,
  provider => 'pip3',
  require  => Package['python3::pip'],
  version  => '2.1.0',
}
