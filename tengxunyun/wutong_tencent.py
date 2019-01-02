from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.aai.v20180522 import aai_client, models
import base64


def tencent_synthesis(text,voice = 0):
    try:
        cred = credential.Credential(
            "SecretId", "SecretKey")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "aai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = aai_client.AaiClient(cred, "ap-shanghai", clientProfile)

        req = models.TextToVoiceRequest()
        # src_txt = ""
        # params2 = '{"Text":"2012年12月，港星周秀娜澄清男友陈伟成被杂志指跟嫩模罗彩玲回家过夜，并否认男友自夸下体镶珠。","SessionId":"wutong_speech_901","ModelType":1,"VoiceType":0}'
        params = {
            "Text": text,
            "SessionId": "wutong_tencent_901", ### 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复
            "Volume": "0", ### 音量大小，范围：[0，10]，分别对应10个等级的音量，默认为0
            "Speed": "0", ### 语速，范围：[-2，2]，分别对应不同语速：0.6倍，0.8倍，1.0倍，1.2倍，1.5倍，默认为0
            "ModelType": 1, ### 模型类型，1-默认模型
            "VoiceType": voice, ### 音色 0-女声1，亲和风格(默认) 1-男声1，成熟风格 2-男声2，成熟风格
            "SampleRate": 16000 ### 音频采样率，16000：16k，8000：8k，默认16k
        }
        req.from_json_string(str(params).replace('\'','\"'))
        resp = client.TextToVoice(req)
        audio = base64.b64decode(resp.Audio)

    except TencentCloudSDKException as err:
        print(err)
        return (audio,False)
    
    return (audio,True)


if __name__ == "__main__":
    tencent_synthesis("分别对应不同语")