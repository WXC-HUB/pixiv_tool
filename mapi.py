import requests
from requests.models import Request, Response, PreparedRequest
import json
from pixivpy3 import *
from pixivpy3.api import BasePixivAPI
from pixivpy3.utils import PixivError, JsonDict
from time import ctime,sleep,mktime,strptime
import os
import shutil


class MyPixivAPI(AppPixivAPI):

    MyServerURL = ''

    def download(self, url, prefix='', path=os.path.curdir, name=None, replace=False, referer='https://app-api.pixiv.net/'):
        print(123123)

        if not name:
            name = prefix + os.path.basename(url)
        else:
            name = prefix + name

        img_path = os.path.join(path, name)
        if (not os.path.exists(img_path)) or replace:
            # Write stream to file
            #response = self.requests_call('GET', url, headers={ 'Referer': referer }, stream=True)
            response = requests.get(url, headers={ 'Referer': referer }, stream=True)
            with open(img_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

    def requests_call(self, method, url, headers={}, params=None, data=None, stream=False):
        if(self.MyServerURL == ''):
            print('no target URL!')
            return
        print('request call: '+method+' ' + url)
        headers.update(self.additional_headers)
        mydata = {}
        mydata['method'] = method
        mydata['url'] = url
        mydata['headers'] = headers
        mydata['data'] = data
        mydata['stream'] = stream
        mydata['params'] = params

        t = requests.post(self.MyServerURL,None,json.dumps(mydata))
        t = json.loads(t.content)
        final = Response()
        final.status_code = t['statusCode']
        final._content = bytes(t['body'], 'utf-8')
        final.headers = t['headers']
        final.encoding = 'utf-8'
        tt = mydata
        return(final)
