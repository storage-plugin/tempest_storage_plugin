# Copyright 2016 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ... import base
from tempest import test


class VolumePoolsAdminV3TestsJSON(base.BaseVolumeAdminTest):

    @classmethod
    def setup_clients(cls):
        super(VolumePoolsAdminV3TestsJSON, cls).setup_clients()
        cls.admin_volume_client = cls.admin_volumes_v3_client
        cls.volumes_client = cls.volumes_v3_client

    @classmethod
    def resource_setup(cls):
        super(VolumePoolsAdminV3TestsJSON, cls).resource_setup()
        # Create a test shared volume for tests
        cls.volume = cls.create_volume()

    def _assert_host_volume_in_pools(self, with_detail=False):
        volume_info = self.admin_volume_client.show_volume(
            self.volume['id'])['volume']
        cinder_pools = self.admin_volume_client.show_pools(
            detail=with_detail)['pools']
        self.assertIn(volume_info['os-vol-host-attr:host'],
                      [pool['name'] for pool in cinder_pools])

    @test.idempotent_id('0248a46c-e226-4933-be10-ad6fca8227e7')
    def test_get_pools_without_details(self):
        self._assert_host_volume_in_pools()

    @test.idempotent_id('d4bb61f7-762d-4437-b8a4-5785759a0ced')
    def test_get_pools_with_details(self):
        self._assert_host_volume_in_pools(with_detail=True)
