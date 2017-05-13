# -*- coding: utf-8 -*-
import pip
pip.main(['install', 'googletrans'])

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import utils

datas_path = '../dataset-amazon-review/test.csv'
#datas_path = 'dataset-amazon-review/train.csv'
utils.translete_data_from(datas_path, name_seved_datas='translations/translete_train.csv', 
          dump_sentence_not_translation='translations/sentence_not_translation_train.p')