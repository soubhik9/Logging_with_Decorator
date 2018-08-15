import requests
import configparser
import logging
from log import log_json,log_text

config = configparser.ConfigParser()
path = r'C:\PycharmProjects\Proj1\config'
config.read(f'{path}\Config.ini')

logging.basicConfig(filename='LogFile.log', filemode = 'w', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

session = requests.Session()
session.trust_env = False	#To bypass proxy. This step is optional

def initApi(baseUri, key):
    global api_key
    global api_base
    global url
    global headers

    api_key = key
    api_base = baseUri

    url = config['Customer']
    headers = {'x-api-key': api_key}




@log_json		#As return type is json, we are calling log_json decorator
def get_cluster_summary_details():
    res = session.get(api_base + url.get('SummaryDetails'), headers = headers)
    return res



@log_text 		#As return type is string, we are calling log_text decorator
def get_compute_node_summary(id):
    u = api_base + url.get('SummaryDetails') + '/' + id
    res = session.get(u, headers = headers)
    return res
