from aws_cdk.core import Stack
from aws_cdk.aws_elasticsearch import Domain, ElasticsearchVersion, CapacityConfig, ZoneAwarenessConfig, EbsOptions
from aws_cdk.aws_ec2 import EbsDeviceVolumeType

from b_cfn_elasticsearch_index.resource import ElasticsearchIndexResource

class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'TestingStack',
            stack_name=f'TestingStack'
        )

        domain = Domain(
            scope=self,
            id="TestingElasticsearchDomain",
            version=ElasticsearchVersion.V7_7,
            capacity=CapacityConfig(
                # Use the cheapest instance available.
                data_node_instance_type="t3.small.elasticsearch",
                data_nodes=1,
                master_nodes=None,
            ),
            zone_awareness=ZoneAwarenessConfig(enabled=False),
            ebs=EbsOptions(enabled=True, volume_size=10, volume_type=EbsDeviceVolumeType.GP2),
        )

        ElasticsearchIndexResource(
            scope=self,
            name="TestingElasticsearchIndex",
            elasticsearch_domain=domain,
            index_prefix="testing_index",
        )
