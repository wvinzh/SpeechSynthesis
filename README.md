# SpeechSynthesis
speech synthesis using ali,baidu,tencent,xunfei api  

语音合成工具  

### 介绍

这是一个简单的语音合成api代码封装，包括了目前国内主流的语音合成接口，包括讯飞，阿里，百度，腾讯。仅供测试学习使用。

### 依赖

腾讯的接口依赖：
```
pip install tencentcloud-sdk-python
```
阿里的接口依赖：
```
pip install aliyun-python-sdk-core
```

### 使用
- 克隆repo
```
git clone https://github.com/wvinzh/SpeechSynthesis.git
```
- 将代码目录放置你的代码目录下
```
from wutong_speech import WutongSpeech
wutong_speech = WutongSpeech()
```

- 参数说明
```
wutong_speech.synthesis(
            "今天天气真不错", voice_index=i)
```
voice_index代表声音索引，本项目供支持17钟不同的人声发音。

- 声音对照
```
print(wutong_speech.voice)
##output##  
[('xunfei', 'xiaoyan'), ('baidu', 0), ('baidu', 1), ('baidu', 3), ('baidu', 4), ('ali', 'xiaoyun'), ('ali', 'xiaogang'), ('ali', 'xiaowei'), ('ali', 'amei'), ('ali', 'xiaoxue'), ('ali', 'siqi'), ('ali', 'ruoxi'), ('ali', 'sijia'), ('ali', 'xiaomeng'), ('tencent', 0), ('tencent', 1), ('tencent', 2)]
```

- 代码示例

```
from wutong_speech import WutongSpeech
wutong_speech = WutongSpeech()
    for i in range(len(wutong_speech.voice)):
        success, r, api_name, voice_name = wutong_speech.synthesis(
            "今天天气真不错", voice_index=i)
        if success:
            print(success)
            with open('%s_%s.wav' % (api_name, voice_name), 'wb') as f:
                f.write(r)
```
