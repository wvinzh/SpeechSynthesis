# -*- coding: UTF-8 -*-
# Python 2.x 引入httplib模块
# import httplib
# Python 3.x 引入http.client模块
import http.client
# Python 2.x 引入urllib模块
# import urllib
# Python 3.x 引入urllib.parse模块
import urllib.parse
import json
# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def get_token():
    # 创建AcsClient实例
    client = AcsClient(
    "AccessKey ID",
    "AccessKey seceret",
    "cn-shanghai")
    # 创建request，并设置参数
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2018-05-18')
    request.set_uri_pattern('/pop/2018-05-18/tokens')
    response = client.do_action_with_exception(request)
    r_json = json.loads(response)
    token = r_json['Token']["Id"]
    # print(r_json['Token']["Id"])
    return token

def processPOSTRequest(appKey, token, text, format, sample_rate, speed, volume, pitch, voice_type):
    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 语音参数配置项

    # 设置HTTPS Headers
    httpHeaders = {
        'Content-Type': 'application/json'
    }
    # 设置HTTPS Body
    body = {'appkey': appKey, 'token': token, 'text': text,
            'format': format, 'sample_rate': sample_rate,
            'speech_rate': speed, "volume": volume,
            "pitch_rate": pitch, "voice": voice_type}

    body = json.dumps(body)
    # print('The POST request body content: ' + body)
    # Python 2.x 请使用httplib
    # conn = httplib.HTTPSConnection(host)
    # Python 3.x 请使用http.client
    conn = http.client.HTTPSConnection(host)
    conn.request(method='POST', url=url, body=body, headers=httpHeaders)
    # 处理服务端返回的响应
    response = conn.getresponse()
    # print('Response status and response reason:')
    # print(response.status, response.reason)
    contentType = response.getheader('Content-Type')
    # print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType:
        # with open(audioSaveFile, mode='wb') as f:
        #     f.write(body)
        # print('The POST request succeed!')
        conn.close()
        return (body, True)
    else:
        print('The POST request failed: ' + str(body))
        conn.close()
        return (body, False)

def ali_synthesis(text,voice="xiaoyun"):
    appKey = 'HhGKM6EAaHnp5PJl'
    # token = 'f5985568a0f0462a9765f7338b9e1d7b'
    token = get_token()
    # print(token)
    # # 小云	xiaoyun	标准女声	通用场景
    # # 小刚	xiaogang	标准男声	通用场景
    # # 小威	xiaowei	标准男声	通用场景
    # # 阿美	amei	甜美女声	客服场景
    # # 小雪	xiaoxue	温柔女声	客服场景
    # # 思琪	siqi	温柔女声	通用场景
    # # 思佳	sijia	标准女声	通用场景
    # # 若兮	ruoxi	温柔女声	通用场景
    # # 小梦	xiaomeng	标准女声	通用场景
    wav_params = {
        "speed": 0,  # 语速，范围是-500~500，默认是0
        "volume": 50,  # 音量，范围是0~100，默认50
        "pitch": 0,  # 语调，范围是-500~500，可选，默认是0
        "voice_type": voice,  # 发音人，默认是xiaoyun，其他发音人名称请在简介中选择
        "format": "wav",  # 音频编码格式，支持的格式：PCM、WAV、MP3，默认是PCM
        "sample_rate": 16000,  # 音频采样率，支持16000Hz、8000Hz，默认是16000Hz
    }
    wave_bin, success = processPOSTRequest(
        appKey, token, text, wav_params["format"], wav_params["sample_rate"],
        wav_params["speed"], wav_params["volume"], wav_params["pitch"], wav_params["voice_type"])
    # print(success)
    return (wave_bin, success)

# ali_synthesis("萨达撒撒反对施工规范和计划")



if __name__ =='__main__':
    ali_synthesis("沙发沙发")
    # get_token()
