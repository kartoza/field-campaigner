# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("1") do |config|
	# v1 configs...
	# I cant find the proper way to set up bridged networking in the v2 docs
	config.vm.network :bridged, :bridge => "eth0"
end

Vagrant.configure("2") do |config|
	# v2 configs...
	config.vm.box = "Ubuntu precise 64"
	config.vm.hostname = "osm-reporter"
	config.vm.network :public_network
	config.vm.network :forwarded_port, guest: 80, host: 9000
	config.vm.box_url = "http://files.vagrantup.com/precise64.box"

end
