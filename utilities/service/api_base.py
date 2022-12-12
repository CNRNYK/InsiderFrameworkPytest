import allure
import requests


def service_get(api_url, header, response_code, params=None):
    response = requests.get(url=api_url,
                            headers=header,
                            params=params)
    verify_status(response, response_code)
    return response


def service_put(api_url, header, response_code, body=None):
    response = requests.put(url=api_url,
                            data=body,
                            headers=header)
    verify_status(response, response_code)
    return response


def service_post(api_url, headers, json_data,  response_code):
    response = requests.post(url=api_url,
                             headers=headers,
                             json=json_data)

    verify_status(response, response_code)
    return response


def service_patch(api_url, body, header, response_code):
    response = requests.patch(url=api_url,
                              data=body,
                              headers=header)
    verify_status(response, response_code)


def service_delete(api_url, header, response_code):
    response = requests.delete(url=api_url,
                               headers=header)
    verify_status(response, response_code)


def verify_status(response, expected_code):
    assert response.status_code == int(expected_code), \
        f'Expected status code:{expected_code},' \
        f' but was: {response.status_code} with body: {response.text} for {response.request.method} {response.url}'
    if response.status_code != int(expected_code):
        print(response)
