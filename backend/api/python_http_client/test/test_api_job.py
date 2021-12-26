# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kfp_server_api
from kfp_server_api.models.api_job import ApiJob  # noqa: E501
from kfp_server_api.rest import ApiException

class TestApiJob(unittest.TestCase):
    """ApiJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kfp_server_api.models.api_job.ApiJob()  # noqa: E501
        if include_optional :
            return ApiJob(
                id = '0', 
                name = '0', 
                description = '0', 
                pipeline_spec = kfp_server_api.models.api_pipeline_spec.apiPipelineSpec(
                    pipeline_id = '0', 
                    pipeline_name = '0', 
                    workflow_manifest = '0', 
                    pipeline_manifest = '0', 
                    parameters = [
                        kfp_server_api.models.api_parameter.apiParameter(
                            name = '0', 
                            value = '0', )
                        ], 
                    runtime_config = kfp_server_api.models.pipeline_spec_runtime_config.PipelineSpecRuntimeConfig(
                        parameters = {
                            'key' : kfp_server_api.models.api_value.apiValue(
                                int_value = '0', 
                                double_value = 1.337, 
                                string_value = '0', )
                            }, 
                        pipeline_root = '0', ), ), 
                resource_references = [
                    kfp_server_api.models.api_resource_reference.apiResourceReference(
                        key = kfp_server_api.models.api_resource_key.apiResourceKey(
                            type = 'UNKNOWN_RESOURCE_TYPE', 
                            id = '0', ), 
                        name = '0', 
                        relationship = 'UNKNOWN_RELATIONSHIP', )
                    ], 
                service_account = '0', 
                max_concurrency = '0', 
                trigger = kfp_server_api.models.api_trigger.apiTrigger(
                    cron_schedule = kfp_server_api.models.cron_schedule_allow_scheduling_the_job_with_unix_like_cron.CronSchedule allow scheduling the job with unix-like cron(
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        cron = '0', ), 
                    periodic_schedule = kfp_server_api.models.periodic_schedule_allow_scheduling_the_job_periodically_with_certain_interval.PeriodicSchedule allow scheduling the job periodically with certain interval(
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        interval_second = '0', ), ), 
                mode = 'UNKNOWN_MODE', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = '0', 
                error = '0', 
                enabled = True, 
                no_catchup = True
            )
        else :
            return ApiJob(
        )

    def testApiJob(self):
        """Test ApiJob"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
