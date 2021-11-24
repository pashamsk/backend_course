import json
import datetime as dt


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    my_dict = {"time": dt.datetime.now().isoformat(), "url": environ["PATH_INFO"]}
    res_json = json.dumps(my_dict, indent=4)
    return [res_json.encode('utf-8')]
