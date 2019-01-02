

from aliyun.wutong_ali import ali_synthesis
from baiduyun.wutong_baidu import baidu_synthesis
from xunfei.wutong_xunfei import xunfei_synthesis
from tengxunyun.wutong_tencent import tencent_synthesis


class WutongSpeech(object):

    def __init__(self):
        # assert api_name in ['baidu', 'ali', 'xunfei',
        #                     'tencent'], "%s not supported yet" % api_name
        # self.api_name = api_name
        self.voice = self.init_voice_api_pair()

    def init_voice_api_pair(self):
        xunfei_voice = ["xiaoyan"]  # xiaoyan
        baidu_voice = [0, 1, 3, 4]  # default 0
        tencent_voice = [0, 1, 2]  # default 0
        ali_voice = ["xiaoyun", "xiaogang", "xiaowei", "amei",
                     "xiaoxue", "siqi", "ruoxi", "sijia", "xiaomeng"]  # xiaoyun
        voice_dict = {
            "xunfei": xunfei_voice,
            "baidu": baidu_voice,
            "ali": ali_voice,
            "tencent": tencent_voice
        }
        res = []
        for api_name, voice_list in voice_dict.items():
            for voice_name in voice_list:
                res.append((api_name, voice_name))
        return res

    def get_client(self, api_name):
        function_name = '{}_synthesis'.format(api_name)
        return eval(function_name)

    def get_voice(self, api_name):
        xunfei_voice = ["xiaoyan"]  # xiaoyan
        baidu_voice = [0, 1, 3, 4]  # default 0
        tencent_voice = [0, 1, 2]  # default 0
        ali_voice = ["xiaoyun", "xiaogang", "xiaowei", "amei",
                     "xiaoxue", "siqi", "ruoxi", "sijia", "xiaomeng"]  # xiaoyun
        voice_dict = {
            "xunfei": xunfei_voice,
            "baidu": baidu_voice,
            "ali": ali_voice,
            "tencent": tencent_voice
        }
        return voice_dict[api_name]

    def synthesis(self, text, voice_index=0):
        assert isinstance(voice_index, int) and voice_index >= 0 and voice_index < len(
            self.voice), "voice should be int and between %d--%d" % (0, len(self.voice))
        api_name, voice = self.voice[voice_index]
        # print(api_name,voice)
        synthesis_client = self.get_client(api_name)
        content, success = synthesis_client(text, voice=voice)

        return (success, content, api_name, str(voice))


if __name__ == '__main__':
    # r,success = tencent_synthesis("沙发沙发")
    # api_name = 'xunfei'
    wutong_speech = WutongSpeech()
    for i in range(len(wutong_speech.voice)):
        success, r, api_name, voice_name = wutong_speech.synthesis(
            "今天天气真不错", voice_index=i)
        if success:
            print(success)
            with open('%s_%s.wav' % (api_name, voice_name), 'wb') as f:
                f.write(r)
