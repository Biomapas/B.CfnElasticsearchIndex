from aws_cdk.core import Stack
from aws_cdk.aws_elasticsearch import Domain, ElasticsearchVersion

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
        )

        ElasticsearchIndexResource(
            scope=self,
            name="TestingElasticsearchIndex",
            domain=domain,
            index_prefix="testing_index",
        )
