from datetime import datetime, timedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    metrics_api = MetricsApi(api_client)

    current_time = datetime.now()
    last_5mins = current_time - timedelta(minutes=5)
    end_time = int(current_time.timestamp())

    query = "dcgm.power_usage{*}"

    response = metrics_api.query_metrics(
        _from=int(last_5mins.timestamp()),
        to=end_time,
        query=query,
    )

    # Extract usernames and power usage from response
    series = response.get('series', [])
    usernames_and_power = []

    for item in series:
        print("Item:", item)
        if isinstance(item, dict):
            tags = item.get('scope', {}).get('hpcuser', '')
            power_usage = item.get('pointlist', [])

            print("Tags:", tags)
            print("Power Usage:", power_usage)

            if tags and power_usage:
                username = tags.split(',')[0]  # Extract the username from the tags
                total_power_usage = sum(point[1] for point in power_usage)  # Calculate total power usage

                usernames_and_power.append((username, total_power_usage))

    # Print the list of usernames and their power usage
    for username, power_usage in usernames_and_power:
        print(f"Username: {username}, Power Usage: {power_usage}")





