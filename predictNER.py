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

    def predict(self, sentence, clear=False):
        sentence = sentence.strip()
        texts = self.text2array_en(sentence)
        ners = self.model.predict_entities(texts)
        output = {"texts": []}
        for i in ners:
            if not i['labels'] and clear:
                continue
            if len(i['text']) < 3 and clear:
                continue
            print('--------------------------------')
            print('text:', i['text'])
            print('labels', i['labels'])
            ner_ls = []
            for label in i['labels']:
                if label['entity'] != '[PAD]':
                    if clear:
                        punctuation = '.!,;:?"“”()（）\''
                        label['value'] = re.sub(r'[{}]+'.format(punctuation), '', label['value'])
                        if len(label['value']) < 2:
                            continue
                        print('\tvalue:', label['value'], '\t', label['entity'])
                        ner_ls.append({"entity": label['value'], "tag": label['entity']})
                    else:
                        print('\tvalue:', label['value'], '\t', label['entity'])
                        ner_ls.append({label['value']: label['entity']})
            output["texts"].append({"sentence": i['text'], "labels": i['labels'], "NER": ner_ls})

        return output


if __name__ == '__main__':
    model = ModelPredict('save')
    model.predict('Start parsing text of pdf files using cermine.')
