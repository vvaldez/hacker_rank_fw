from hackerrank import HackerRankClient

import requests
from pypandoc import convert_file 
import json
from urlparse import urljoin
import os

# Begin Test Run
# Export your API key as an env var first
hr = HackerRankClient(token=os.environ.get('HR_KEY'))

all_tests = hr.get_tests_list()

instructions = convert_file('./description.md', 'html')
templates_q = convert_file('./ansible_templates.md', 'html')
setup_script = open('./test.sh', 'r').read()
tags = ["TALENT ACQUISITION", "CONSULTING SERVICES", "NA", "ANSIBLE", "AUTOMATION"]
n_tags = ['ANSIBLE TOWER']
put_data = dict( 
    instructions=instructions,
    tags = n_tags,
    duration = 130,
    sudorank_setupscript = setup_script,
)

print json.dumps(hr.get_all_questions(question_type='personal'), indent=2)
x

for test in all_tests['data']:
    if test['name'] == "Consulting Services, Automation Architect, Ansible (NA)":
        test_id = test['id']
        #result = hr.update_test(test_id, put_data, purge_tags=True)
        result = hr.update_test(test_id, put_data)
        try:
            print 'SUCCESS' 
        except TypeError:
            print result




#print json.dumps(all_tests, indent=2)


