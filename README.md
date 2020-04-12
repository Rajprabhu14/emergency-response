# emergency-response
This Backend app for helping the people who's on need due to lockdown with the help of the Volunteers.
This Backend app build with help of
1. [Django](https://www.djangoproject.com/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)
3. [Django Rest Auth](https://github.com/Tivix/django-rest-auth)
4. [MapMyIndia](https://www.mapmyindia.com/)


### Prerequisites

```
Install Python 3.6/3.7
```

### Installing

Create a virtual environment

```
virtualenv env
```

Activate the Virtual Environment in Windows

```
env\Scripts\activate
```

Install project dependancies using pip

```
pip install -r requirements.txt
```

## API V1
Description| URL | Allowed Verbs |
| :--- | :--- | :--- |
Create Request for Delivery | /api/v1/customer | `POST` |
Action perform on Delivery Request | /api/v1/customer/:uid | `GET`, `PUT`, `PATCH`, `DELETE` |
Create Customer or Volunteer | /api/v1/volunteer/ | `POST` |
Action perform on Volunteer or Customer | /api/v1/volunteer/ | `GET`, `PUT`, `PATCH`,`DELETE` |
Update Password| /api/v1/volunteer/update/:uid | `PUT`|
Get the ist of Delivery based on location| /api/v1/help/ | `GET` |
Get the list of Helped Customer| /help/customer/| `GET`|
Login Access Token| /api/token/ | `post` |
refresh Token| /api/token/refresh/| `post` |
## Status Codes

Standard status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 204 | `NO CONTENT` |
| 400 | `BAD REQUEST` |
| 401 | `UNAUTHORIZED` |
| 404 | `NOT FOUND` |
| 405 | `METHOD NOT ALLOWED` |
| 417 | `EXPECTATION FAILED` |
| 422 | `VALIDATION ERROR` |
| 500 | `INTERNAL SERVER ERROR` |

## Custom Success Codes


| Status Code | Description |
| :--- | :--- |
| 15001 | `Customer Registration` |
| 15002 | `Volunteer Registration` |
| 15003 | `Password Updated` |
| 15004 | `Customer Retrieved based on location` |
| 15005 | `Success customer help request` |

## Custom Failure Codes
| Status Code | Description |
| :--- | :--- |
| 19001 | `VALIDATION_ERROR` |
| 19002 | `MAP_API_ERROR` |
| 19003 | `CUSTOMR_NOT_PRESENT` |
| 19004 | `INCORRECT_VOLUNTEER_UID` |
| 19005 | `INCORRECT_CUSTOMER_UID` |
| 19006 | `NO_ORDER_TAKEN` |
| 19007 | `METHOD_NOT_aLLOWED` |
| 19008 | `URL_NOT_FOUND` |
| 19009 | `UNAUTHORIZED` |
