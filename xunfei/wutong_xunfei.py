
# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import random



class XunfeiSpeech():
    def __init__(self,param):
        self.URL = "http://api.xfyun.cn/v1/service/v1/tts"
        self.AUE = "raw"
        self.APPID = "APPID"
        self.API_KEY = "API_KEY"
        self.param = param
		
    def getHeader(self):
        curTime = str(int(time.time()))
        # ttp=ssml
        # param = "{\"aue\":\""+AUE+"\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
        # param = {"aue":"raw","auf":"audio/L16;rate=16000","voice_name":"xiaoyan","engine_type":"intp65"}
        # param = {
        #     "auf": "audio/L16;rate=16000", ### 音频采样率，可选值：audio/L16;rate=8000，audio/L16;rate=16000
        #     "aue": "raw", ### 音频编码，可选值：raw（未压缩的pcm或wav格式），lame（mp3格式）
        #     "voice_name": "xiaoyan",###发音人，可选值：详见发音人列表
        #     "speed": "50", ### 语速，可选值：[0-100]，默认为50
        #     "volume": "50", ### 音量，可选值：[0-100]，默认为50
        #     "pitch": "50", ### 音高，可选值：[0-100]，默认为50
        #     "engine_type": "intp65", ### 引擎类型，可选值：aisound（普通效果），intp65（中文），intp65_en（英文），mtts（小语种，需配合小语种发音人使用），x（优化效果），默认为intp65
        # }
        
        # print(param)
        # print("param:{}".format(param))

        paramBase64 = str(base64.b64encode(self.param.encode('utf-8')), 'utf-8')
        # print("x_param:{}".format(paramBase64))

        m2 = hashlib.md5()
        m2.update((self.API_KEY + curTime + paramBase64).encode('utf-8'))

        checkSum = m2.hexdigest()
        # print('checkSum:{}'.format(checkSum))

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.APPID,
            'X-CheckSum': checkSum,
            'X-Real-Ip': '127.0.0.1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        # print(header)
        return header


    def getBody(self,text):
        data = {'text': text}
        return data


def xunfei_synthesis(text,voice = "xiaoyan"):

    param = {
        "auf": "audio/L16;rate=16000", ### 音频采样率，可选值：audio/L16;rate=8000，audio/L16;rate=16000
        "aue": "raw", ### 音频编码，可选值：raw（未压缩的pcm或wav格式），lame（mp3格式）
        "voice_name": voice,###发音人，可选值：详见发音人列表
        "speed": "50", ### 语速，可选值：[0-100]，默认为50
        "volume": "50", ### 音量，可选值：[0-100]，默认为50
        "pitch": "50", ### 音高，可选值：[0-100]，默认为50
        "engine_type": "intp65", ### 引擎类型，可选值：aisound（普通效果），intp65（中文），intp65_en（英文），mtts（小语种，需配合小语种发音人使用），x（优化效果），默认为intp65
    }
    param = str(param).replace('\'','\"')
    xunfei_speech = XunfeiSpeech(param)
    r = requests.post(xunfei_speech.URL, headers=xunfei_speech.getHeader(), data=xunfei_speech.getBody(text))

    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        return (r.content,True)
    else:
        print(r.content)
        return (r.content,False)


if __name__=='__main__':
    xunfei_synthesis("爱上打算大师傅")
