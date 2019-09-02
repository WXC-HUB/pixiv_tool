import sys
import requests
import json

# main() will be invoked when you invoke this action.
#
# When enabled as a web action, use the following URL to invoke this action:
# https://{APIHOST}/api/v1/web/{QUALIFIED ACTION NAME}?location=Austin
#
# For example:
# https://openwhisk.ng.bluemix.net/api/v1/web/myusername@us.ibm.com_myspace/get-resource/weather?location=Austin
#
# In this case, the params variable will look like:
# { "location": "Austin" }

def requests_call( method, url, headers={}, params=None, data=None, stream=False):
    if (method == 'GET'):
        return requests.get(url, params=params, headers=headers, stream=stream)
    elif (method == 'POST'):
        return requests.post(url, params=params, data=data, headers=headers, stream=stream)
    elif (method == 'DELETE'):
        return requests.delete(url, params=params, data=data, headers=headers, stream=stream)


def main(params):
    tt = json.loads(params['__ow_body'])

    #r = requests.get(url,headers)
    r = requests_call(tt['method'],tt['url'],tt['headers'],tt['params'],tt['data'],tt['stream'])
    return {
            'statusCode': r.status_code,
            'headers': str(r.headers),
            'body': json.dumps(r.json())
        }

