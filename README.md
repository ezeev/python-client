# wavefront_client
<p>The Wavefront Public APIs are published for customers to use when interacting with Wavefront servers.  These APIs can be used to automate commonly executed operations such as tagging sourcesa utomatically.</p><p>Please note that you'll need to supply the X-AUTH-TOKEN header with a valid token.</p>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0.7
- Package version: 1.0.0
- Build date: 2016-04-29T10:20:25.454-07:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/wavefrontHQ/python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wavefrontHQ/python-client.git`)


If you are installing it on OS X El Capitan then you may have to ignore the ``six`` package installation as OS X El Capitan ships with six 1.4.1 installed already

```

sudo pip install --ignore-installed six git+https://github.com/wavefrontHQ/python-client.git

```


Then import the package:
```python
import wavefront_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wavefront_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint


# Configure HOST Url: host
wavefront_client.configuration.host = 'YOUR_INSTANCE_URL'  # example : 'https://metrics.wavefront.com'
# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'
# create an instance of the API class
api_instance = wavefront_client.AlertApi
name = 'name_example' # str | Descriptive name for the alert
condition = 'condition_example' # str | A query that will trigger the alert if non-zero results are observed for given number of minutes
minutes = 56 # int | Number of minutes for the query to return non-zero results before the alert fires. Must be 2 or higher
notifications = 'notifications_example' # str | Up to ten addresses can be listed, separated by commas. Notifications will be sent to all targets on the list. To trigger a PagerDuty incident, specify a \"pd:key\" target with the 32-digit hex API key you created. PagerDuty incidents will be automatically triggered, updated, and resolved.
severity = 'severity_example' # str | Severity
display_expression = 'display_expression_example' # str | An optional query that will be shown when the alert fires. Use this to show a more helpful chart, e.g. the underlying timeseries (optional)
resolve_minutes = 56 # int | Number of minutes for the query to return 0 as a result before the alert resolves. Defaults to the same as minutes to fire if not set. Must be 2 or higher (optional)
private_tags = 'private_tags_example' # str | Comma separated list of private tags to be associated with this alert (optional)
shared_tags = 'shared_tags_example' # str | Comma separated list of shared tags to be associated with this alert (optional)
additional_information = 'additional_information_example' # str | Any additional information to be included with this alert (optional)

try:
    # Create an alert
    api_response = api_instance.create_alert_from_parts(name, condition, minutes, notifications, severity, display_expression=display_expression, resolve_minutes=resolve_minutes, private_tags=private_tags, shared_tags=shared_tags, additional_information=additional_information)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->create_alert_from_parts: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertApi* | [**create_alert_from_parts**](docs/AlertApi.md#create_alert_from_parts) | **POST** /api/alert/create | Create an alert
*AlertApi* | [**get_active_alerts**](docs/AlertApi.md#get_active_alerts) | **GET** /api/alert/active | Get Active Alerts
*AlertApi* | [**get_alert**](docs/AlertApi.md#get_alert) | **GET** /api/alert | Retrieve a list of alerts for a particular view. (Deprecated: Retrieve a single alert by its id (creation time))
*AlertApi* | [**get_alerts**](docs/AlertApi.md#get_alerts) | **GET** /api/alert/all | Get All Alerts
*AlertApi* | [**get_alerts_affected_by_maintenance**](docs/AlertApi.md#get_alerts_affected_by_maintenance) | **GET** /api/alert/affected_by_maintenance | Get In Maintenance Alerts
*AlertApi* | [**get_invalid_alerts**](docs/AlertApi.md#get_invalid_alerts) | **GET** /api/alert/invalid | Get Invalid Alerts
*AlertApi* | [**get_snoozed_alerts**](docs/AlertApi.md#get_snoozed_alerts) | **GET** /api/alert/snoozed | Get Snoozed Alerts
*AlertApi* | [**get_specific_alert**](docs/AlertApi.md#get_specific_alert) | **GET** /api/alert/{created} | Retrieve a single alert by its id (creation time)
*AlertApi* | [**update_alert_from_parts**](docs/AlertApi.md#update_alert_from_parts) | **POST** /api/alert/{alertId} | Update an alert
*DashboardApi* | [**clone_dashboard**](docs/DashboardApi.md#clone_dashboard) | **POST** /api/dashboard/{id}/clone | Clones a dashboard
*DashboardApi* | [**create_dashboard**](docs/DashboardApi.md#create_dashboard) | **POST** /api/dashboard/{id}/create | Creates an empty dashboard
*DashboardApi* | [**dashboard_history**](docs/DashboardApi.md#dashboard_history) | **GET** /api/dashboard/{id}/history | Returns version history about a dashboard
*DashboardApi* | [**dashboards**](docs/DashboardApi.md#dashboards) | **GET** /api/dashboard | Lists dashboards
*DashboardApi* | [**delete_dashboard**](docs/DashboardApi.md#delete_dashboard) | **POST** /api/dashboard/{id}/delete | Deletes the dashboard at {id}
*DashboardApi* | [**get_dashboard**](docs/DashboardApi.md#get_dashboard) | **GET** /api/dashboard/{id} | Returns data about a dashboard, the latest version
*DashboardApi* | [**get_dashboard_version**](docs/DashboardApi.md#get_dashboard_version) | **GET** /api/dashboard/{id}/{version} | Returns data about a dashboard, a specific version
*DashboardApi* | [**save_dashboard**](docs/DashboardApi.md#save_dashboard) | **POST** /api/dashboard | Saves or creates a JSON-specified dashboard.
*DashboardApi* | [**undelete_dashboard**](docs/DashboardApi.md#undelete_dashboard) | **POST** /api/dashboard/{id}/undelete | Undeletes the dashboard at {id}
*EventsApi* | [**close_ongoing_event**](docs/EventsApi.md#close_ongoing_event) | **POST** /api/events/close | Close an event
*EventsApi* | [**create_new_event**](docs/EventsApi.md#create_new_event) | **POST** /api/events | Create a new event
*EventsApi* | [**delete_event**](docs/EventsApi.md#delete_event) | **DELETE** /api/events/{startTime}/{name} | Delete an event. Can only delete non-system events. System events include alert firings, error events, and maintenance windows
*MaintenanceWindowApi* | [**close**](docs/MaintenanceWindowApi.md#close) | **POST** /api/alert/maintenancewindow/{id}/close | Close a currently active maintenance window
*MaintenanceWindowApi* | [**create_from_parts**](docs/MaintenanceWindowApi.md#create_from_parts) | **POST** /api/alert/maintenancewindow/create | Create a new maintenance window
*MaintenanceWindowApi* | [**delete**](docs/MaintenanceWindowApi.md#delete) | **DELETE** /api/alert/maintenancewindow/{id} | Delete a specific maintenance window
*MaintenanceWindowApi* | [**extend**](docs/MaintenanceWindowApi.md#extend) | **POST** /api/alert/maintenancewindow/{id}/extend | Extend a currently active maintenance window by specified number of seconds
*MaintenanceWindowApi* | [**get_all**](docs/MaintenanceWindowApi.md#get_all) | **GET** /api/alert/maintenancewindow/all | Get a list of every maintenance window
*MaintenanceWindowApi* | [**get_summary**](docs/MaintenanceWindowApi.md#get_summary) | **GET** /api/alert/maintenancewindow/summary | Get a filtered list of maintenance windows
*MaintenanceWindowApi* | [**update_from_parts**](docs/MaintenanceWindowApi.md#update_from_parts) | **POST** /api/alert/maintenancewindow/{id} | Update a maintenance window
*ManagementApi* | [**get_host_details**](docs/ManagementApi.md#get_host_details) | **GET** /api/manage/source/{source} | Return applied tags and description for a source/host
*ManagementApi* | [**get_hosts**](docs/ManagementApi.md#get_hosts) | **GET** /api/manage/source | Request a subset of sources
*ManagementApi* | [**remove_all_source_tags**](docs/ManagementApi.md#remove_all_source_tags) | **DELETE** /api/manage/source/{source}/tags | Remove all tags from a source/host
*ManagementApi* | [**set_source_description**](docs/ManagementApi.md#set_source_description) | **POST** /api/manage/source/{source}/description | Set description for a source/host
*ManagementApi* | [**tag_source**](docs/ManagementApi.md#tag_source) | **POST** /api/manage/source/{source}/tags/{tag} | Tag a source/host
*ManagementApi* | [**un_tag_source**](docs/ManagementApi.md#un_tag_source) | **DELETE** /api/manage/source/{source}/tags/{tag} | Remove tag from a source/host
*QueryApi* | [**chart**](docs/QueryApi.md#chart) | **GET** /chart/api | Perform a charting query against Wavefront servers which returns the appropriate points in the specified time window and granularity
*QueryApi* | [**raw_query**](docs/QueryApi.md#raw_query) | **GET** /chart/raw | Perform a raw data query against Wavefront servers which returns second granularity points grouped by tags
*UserApi* | [**create_user_rest**](docs/UserApi.md#create_user_rest) | **POST** /api/user/create | Creates a new user
*UserApi* | [**delete_user_rest**](docs/UserApi.md#delete_user_rest) | **DELETE** /api/user/{id} | Deletes a user identified by {id}
*UserApi* | [**get_all_users_rest**](docs/UserApi.md#get_all_users_rest) | **GET** /api/user/all | Get all users
*UserApi* | [**get_user_rest**](docs/UserApi.md#get_user_rest) | **GET** /api/user/{id} | Retrieves a user by identifier (email addr)
*UserApi* | [**grant_user_rest**](docs/UserApi.md#grant_user_rest) | **POST** /api/user/{id}/grant | Grants a specific user permission
*UserApi* | [**revoke_user_rest**](docs/UserApi.md#revoke_user_rest) | **POST** /api/user/{id}/revoke | Revokes a specific user permission


## Documentation For Models

 - [Alert](docs/Alert.md)
 - [Chart](docs/Chart.md)
 - [ChartSettings](docs/ChartSettings.md)
 - [ChartSource](docs/ChartSource.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardHistory](docs/DashboardHistory.md)
 - [DashboardMetadata](docs/DashboardMetadata.md)
 - [DashboardSection](docs/DashboardSection.md)
 - [DashboardSectionRow](docs/DashboardSectionRow.md)
 - [HostLabelPair](docs/HostLabelPair.md)
 - [MaintenanceWindow](docs/MaintenanceWindow.md)
 - [MonitoringTarget](docs/MonitoringTarget.md)
 - [Point](docs/Point.md)
 - [QueryKeyContainer](docs/QueryKeyContainer.md)
 - [QueryResult](docs/QueryResult.md)
 - [ReportEvent](docs/ReportEvent.md)
 - [StatsModel](docs/StatsModel.md)
 - [SummaryOfMaintenanceWindows](docs/SummaryOfMaintenanceWindows.md)
 - [TaggedSource](docs/TaggedSource.md)
 - [TaggedSourceBundle](docs/TaggedSourceBundle.md)
 - [Tags](docs/Tags.md)
 - [Timeseries](docs/Timeseries.md)
 - [User](docs/User.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-AUTH-TOKEN
- **Location**: HTTP header


## Author



