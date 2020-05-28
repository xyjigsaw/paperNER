# Name: main
# Author: Reacubeth
# Time: 2020/5/28 12:27
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from paper2XML import PaperXML
from predictNER import ModelPredict
import time
import warnings

warnings.filterwarnings("ignore")


if __name__ == '__main__':
    model = ModelPredict('save')
    while True:
        file_path = input('input file path: ')
        start = time.time()
        paper = PaperXML(file_path)
        # print(paper.section_text)
        model.predict(paper.section_text)
        print(time.time() - start)
