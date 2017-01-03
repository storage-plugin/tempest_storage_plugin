Tempest Integration of storage tests - cinder , glance , nova, swift and ceph

This directory contains Tempest tests to cover the StorageTest project.

Setup steps:

Prerequisites:

# git clone tempest upstream code

git clone https://github.com/openstack/tempest.git

cd tempest

# git clone plugin code

git clone https://github.com/bkopilov/tempest_storage_plugin.git

cd tempest_storage_plugin/tempest_plugin

# install python packages

sudo pip install --upgrade -e .


# Verify testr list-tests and run:

cd tempest/

testr init

testr list-tests | grep -i storage

testr run [test_name]


