#!/usr/bin/env python
# coding: utf-8
import requests
import urllib
import re
import sys
import time
import hashlib
import requests
import json
import random
import os
from collections import defaultdict
import numpy as np
import codecs
import copy
import pickle


# 文件夹路径
finetune_result_path = "/Users/yuan/MyDocument/workspace/Python/US_Project/xyq/script_yuan/indicator/fight_highlight/finetune_ouput"
file_name="commentator_test_results.jsonl"
finetune_result = os.path.join(finetune_result_path, file_name)

write_list=[]
for i, line in enumerate(open(finetune_result)):
    cur_dict={}
    zhanbao_json=json.loads(line)
    input=zhanbao_json['input']
    output=zhanbao_json['original_output']
    cur_dict['question']=input
    cur_dict['answer']=output
    write_list.append(cur_dict)

output_path='/Users/yuan/MyDocument/workspace/Python/chatglm-finetune/data/comentator_lora.json'
with open(output_path, 'w') as f:
    # 使用json模块的dump函数将字典的列表转为json格式并保存到文件
    json.dump(write_list, f,ensure_ascii=False)


