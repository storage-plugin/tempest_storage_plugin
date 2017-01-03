
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    availability_zone_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    backups_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    capabilities_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    encryption_types_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    extensions_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    hosts_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    limits_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    qos_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    quotas_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    scheduler_stats_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    services_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    snapshots_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    types_client
from tempest_storage_plugin.tempest_plugin.tests.lib.services.volume.v3 import\
    volumes_client


class Manager(object):
    def __init__(self, auth_provider, service, region):

        params = {"auth_provider": auth_provider,
                  "service": service,
                  "region": region}
        self._set_cinder_v3_clients(params)

    def _set_cinder_v3_clients(self, params):
        self.availability_zone_v3_client = \
            availability_zone_client.AvailabilityZoneClient(**params)
        self.volumes_v3_client = volumes_client.VolumesClient(**params)
        self.backups_v3_client = backups_client.BackupsClient(**params)
        self.services_v3_client = services_client.ServicesClient(**params)
        self.volumes_extension_v3_client = \
            extensions_client.ExtensionsClient(**params)
        self.volume_limits_v3_client = limits_client.LimitsClient(**params)
        self.snapshots_v3_client = snapshots_client.SnapshotsClient(**params)
        self.scheduler_stats_v3_client = \
            scheduler_stats_client.SchedulerStatsClient(**params)
        self.volume_qos_v3_client = qos_client.QosSpecsClient(**params)
        self.volume_types_v3_client = types_client.TypesClient(**params)
        self.hosts_v3_client = hosts_client.HostsClient(**params)
        self.encryption_types_v3_client = \
            encryption_types_client.EncryptionTypesClient(**params)
        self.quotas_v3_client = quotas_client.QuotasClient(**params)
        self.capabilities_v3_client = \
            capabilities_client.CapabilitiesClient(**params)
