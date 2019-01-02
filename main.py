from wutong_speech import WutongSpeech
import threading
import concurrent
from concurrent.futures import ThreadPoolExecutor
import os

# 新线程执行的代码:


def loop(text, voice_index):
    _, _, _, symbol, sentence = text.split()
    save_path = './speech'
    w_speech = WutongSpeech()
    api_name, voice = w_speech.voice[voice_index]
    save_name = '%s_%s_%s.wav' % (symbol, api_name, voice)
    save_full_path = os.path.join(save_path, save_name)
    if os.path.exists(save_full_path):
        return
    success, content, _, _ = w_speech.synthesis(sentence, voice_index)
    if success:
        with open(save_full_path, 'wb') as f:
            f.write(content)
    return success

# URLS = ['a','b','c']


def main():
    # read the txt file
    text_file = "sentence_text.txt"

    with open(text_file, 'r', encoding='utf-8') as f:
        text_list = f.readlines()
    # We can use a with statement to ensure threads are cleaned up promptly
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(
            loop, text, i): text for text in text_list for i in range(0, 18)}
        for future in concurrent.futures.as_completed(future_to_url):
            text = future_to_url[future]
            try:
                success = future.result()
            except Exception as exc:
                pass
                # print('%r generated an exception: %s' % (text, exc))
            else:
                # print(text,success)
                if not success:
                    print(text)


if __name__ == '__main__':
    main()
