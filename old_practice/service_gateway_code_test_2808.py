import oci
import datadog
from datetime import datetime, timedelta
from oci.config import from_file
from oci.monitoring.models import metric_data_details
from datadog import initialize, api
import json
from json import dumps
import base64
import os
import io
import json
import logging
from datetime import timezone
print("start")

def send_metrics_to_datadog(api_key, compartment_id, region, timestamp, data, service_metric_name, app_key):
    metrics="bytesFromService[1m].mean()"
    tenancy_name='oracletrcosell'
    alias_name='tr-oci-sgw-tenancy'
    hostname='205257-sgw-metrics-pre-prod-ashburn'
    region='us-ashburn-1'
    datadog_options={"api_key": api_key,
         "app_key": app_key,
         "host_name": hostname}
    initialize(**datadog_options)

    datadog_tags = [
        f"OCI_Alias_Name:{alias_name}",
        f"compartment_id:{compartment_id}",
        f"OCI_Region:{region}",
        f"app_name:oci_ServiceGW_test_monitor",
        f"timestamp:{timestamp}",
        f"service_metric_name:{service_metric_name}"
    ]

    resp = api.Metric.send(
        metric='oci_service_gateway.bytes_from_service',
        points=[(timestamp,data)],
        type="gauge",
        tags=datadog_tags
    )
    print(resp)
    print(f"Sent data to Datadog: {datadog_tags}, data: {data}")

def handler():
    print("handler")
    try:
        print("inside handler")
        api_key = "YOUR_DD_API_KEY"  # get_Secrets.get("DD_API_KEY")
        app_key = "YOUR_DD_APP_KEY"  # get_Secrets.get("DD_APP_KEY")
        alias_name = "tr-oci-sgw-tenancy"
        regions = ["us-ashburn-1", "us-phoenix-1", "eu-frankfurt-1", "ap-mumbai-1"]
        tenancy_list = ['ocid1.tenancy.oc1..aaaaaaaagnwk3n3plk2o5almwjoqr4h2zbjcvigcimmq4lafbhmvkyv53kaq']

        for tenancy_id in tenancy_list:
            print("===============Tenancy ID==========")
            print(tenancy_id)
            config = oci.config.from_file("config4.conf")
            resource_search_client = oci.resource_search.ResourceSearchClient(config)
            monitoring_client = oci.monitoring.MonitoringClient(config)
            query_list = ["bytesFromService[1m].mean()"]
            for region in regions:
                print("===========Inside region loop =============")
                monitoring_client.base_client.set_region(region)
                resource_search_client.base_client.set_region(region)  
                compartments = []  
                compartment_search = oci.pagination.list_call_get_all_results(
                    oci.identity.IdentityClient(config).list_compartments,
                    compartment_id=tenancy_id,
                    compartment_id_in_subtree=True
                ).data  
                for c in compartment_search:
                    compartments.append(c.id)
                print(f"Regions and Compartments: {region} - {compartments}")

                for compartment_id in compartments:
                    for q in query_list:
                        print("======Inside query loop==============")
                        bytes_from_service = monitoring_client.summarize_metrics_data(
                            compartment_id=compartment_id,
                            summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
                                namespace="oci_service_gateway",
                                query=q,
                                start_time=datetime.now(timezone.utc) - timedelta(days=7),
                                end_time=datetime.now(timezone.utc),
                                resolution='1m'
                            )
                        )

                        if bytes_from_service.data:
                            for metric_data in bytes_from_service.data:
                                resource_id = metric_data.dimensions['resourceId']
                                for item in metric_data.aggregated_datapoints:
                                    timestamp = item.timestamp
                                    data = item.value
                                    send_metrics_to_datadog(api_key, compartment_id, region, timestamp, data, q, app_key)

    except Exception as e:
        print(e)

handler()
