# Name: predict
# Author: Reacubeth
# Time: 2020/5/27 22:18
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

import kashgari
import re


class ModelPredict:
    def __init__(self, model_path):
        self.model = kashgari.utils.load_model(model_path)

    def text2array_zh(self, text, sequence_length):
        textArr = re.findall('.{' + str(sequence_length) + '}', text)
        # print('1', textArr)
        textArr.append(text[(len(textArr) * sequence_length):])
        # print(text[(len(textArr) * sequence_length):])
        return [[c for c in text] for text in textArr]

    def text2array_en(self, text):
        sentences = text.split('.')
        sentences = [i + '.' for i in sentences]
        return [x.split() for x in sentences if x != '.']

    def predict(self, sentence):
        sentence = sentence.strip()
        texts = self.text2array_en(sentence)
        ners = self.model.predict_entities(texts)
        for i in ners:
            print('--------------------------------')
            print('text:', i['text'])
            print('labels', i['labels'])
            for label in i['labels']:
                print('\tvalue:', label['value'], '\t', label['entity'])


if __name__ == '__main__':
    model = ModelPredict('save')
    model.predict('Start parsing text of pdf files using cermine.')
