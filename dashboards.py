import requests

# Set your API and application keys here
API_KEY = ""
APP_KEY = ""

# Set the dashboard ID and widget ID of the table widget you want to retrieve
DASHBOARD_ID = "7ap-42e-ek8"
WIDGET_ID = '4783479830827492'

url = f"https://api.datadoghq.com/api/v1/dashboard/{DASHBOARD_ID}"

# Headers with authentication
headers = {
    "DD-API-KEY": API_KEY,
    "DD-APPLICATION-KEY": APP_KEY
}

try:
    # Get the specified dashboard
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    dashboard = response.json()
    print(dashboard)

    # Find the widget by its ID in the dashboard
    widget = next((w for w in dashboard["widgets"] if w.get("id") == WIDGET_ID), None)

    if widget and widget["type"] == "query_table":
        # Access the data rows of the query_table widget
        rows = widget["definition"]["requests"][0]["response_format"]["rows"]

        # Print the query_table data
        for row in rows:
            print(row)

    else:
        print("The widget is not a query_table or the specified widget ID is not found.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")