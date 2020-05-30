# Name: readXML
# Author: Reacubeth
# Time: 2020/4/26 22:07
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from xml.dom.minidom import parse
from toolkit.pdf_parser import Parser
from os import path
import time
import re


class PaperXML:
    def __init__(self, file_path):
        """
        :param file_path: PDF file path
        """
        file_path = file_path.replace('.PDF', '.pdf')
        if not path.isfile('output/' + file_path[:file_path.index('.pdf')] + '.cermine.xml'):
            parser = Parser('cermine')
            parser.parse('text', file_path, 'output', 0)
        self.dom = parse('output/' + file_path[:file_path.index('.pdf')] + '.cermine.xml')
        # print('output/' + file_path[:file_path.index('.pdf')] + '.cermine.xml')
        self.data = self.dom.documentElement
        self.paper_title = self.get_paper_title()
        self.section_dict, self.section_text = self.get_secs()
        self.ref_dict = self.get_rf()
        self.paper_aff_dict = self.get_affiliation()
        self.paper_year = self.get_paper_year()
        self.author_dict = self.get_author()

    def get_paper_title(self):
        try:
            if self.paper_title:
                return self.paper_title
        except AttributeError:
            return self.data.getElementsByTagName('article-title')[0].childNodes[0].nodeValue

    def get_paper_year(self):
        try:
            if self.paper_year:
                return self.paper_year
        except AttributeError:
            try:
                return self.data.getElementsByTagName('article-meta')[0].getElementsByTagName('year')[0].childNodes[
                    0].nodeValue
            except IndexError as e:
                return '0000'

    def get_affiliation(self):
        try:
            if self.paper_aff_dict:
                return self.paper_aff_dict
        except AttributeError:
            data_range = self.data.getElementsByTagName('article-meta')[0].getElementsByTagName('contrib-group')[0]
            aff_ls = data_range.getElementsByTagName('aff')
            aff_dict = {}
            for item in aff_ls:
                aff_id = item.getElementsByTagName('label')[0].childNodes[0].nodeValue
                aff_name = item.getElementsByTagName('institution')[0].childNodes[0].nodeValue
                aff_dict[aff_id] = {'affiliationName': aff_name}
                if item.getElementsByTagName('addr-line'):
                    address = item.getElementsByTagName('addr-line')[0].childNodes[0].nodeValue
                    aff_dict[aff_id]['address'] = address
                if item.getElementsByTagName('country'):
                    country = item.getElementsByTagName('country')[0].childNodes[0].nodeValue
                    aff_dict[aff_id]['country'] = country
            return aff_dict

    def get_author(self):
        try:
            if self.author_dict:
                return self.author_dict
        except AttributeError:
            data_range = self.data.getElementsByTagName('article-meta')[0].getElementsByTagName('contrib-group')[0]
            author_ls = data_range.getElementsByTagName('contrib')
            author_dict = {}
            author_rank = 0
            for item in author_ls:
                author_name = item.getElementsByTagName('string-name')[0].childNodes[0].nodeValue
                if item.getElementsByTagName('email'):
                    email = item.getElementsByTagName('email')[0].childNodes[0].nodeValue
                    author_dict[str(author_rank)] = {'authorName': author_name, 'email': email}
                else:
                    author_dict[str(author_rank)] = {'authorName': author_name}
                affiliation = []
                xref_ls = item.getElementsByTagName('xref')
                for xref_item in xref_ls:
                    xref_val = xref_item.getAttribute('ref-type')
                    if xref_val == 'aff':
                        affiliation.append(xref_item.childNodes[0].nodeValue)
                author_dict[str(author_rank)]['affiliation'] = affiliation
                author_rank += 1
            return author_dict

    def get_rf(self):
        try:
            if self.ref_dict:
                return self.ref_dict
        except AttributeError:
            ref_ls = self.data.getElementsByTagName('ref')
            rf_rank = 0
            ref_dict = {}
            for item in ref_ls:
                try:
                    article_title = item.getElementsByTagName('mixed-citation')[0]. \
                        getElementsByTagName('article-title')[0].childNodes[0].nodeValue
                    article_year = item.getElementsByTagName('year')[0].childNodes[0].nodeValue
                    ref_dict[str(rf_rank)] = {'paperName': article_title, 'year': article_year}
                    rf_rank += 1
                except IndexError as e:
                    pass
                    # print('PaperXML.get_rf Error:', e)
            return ref_dict

    def get_secs(self):
        try:
            if self.section_dict:
                return self.section_dict, self.section_text
        except AttributeError:
            secs = self.data.getElementsByTagName('sec')
            section_dict = {}
            all_sec_text = ''
            sec_rank = 0
            for item in secs:
                sec_title = item.getElementsByTagName('title')[0].childNodes[0].nodeValue
                p_ls = item.getElementsByTagName('p')
                p_text = ''
                for p in p_ls:
                    p_val = str(p.childNodes[0].nodeValue).replace('\n', ' ').strip()
                    # p_val = re.findall('[a-zA-Z0-9\s+\t\.\!\/_,$%^*(+\"\'\-]+', p_val, re.S)
                    # p_val = "".join(p_val)
                    all_sec_text += p_val + '\n'
                    p_text += p_val + ' '
                if sec_title == '-':
                    sec_title = 'abstract'
                section_dict[str(sec_rank)] = {'sec_title': sec_title}
                section_dict[str(sec_rank)]['text'] = p_text
                sec_rank += 1
                # with open('all_sec_text.txt', 'w+') as f:
                #     f.write(all_sec_text)

            return section_dict, all_sec_text


if __name__ == '__main__':
    start = time.time()
    paper = PaperXML('ELG.pdf')
    print(paper.section_text)
    print(time.time() - start)
