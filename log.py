#These are the definitions of the decorators
from Exception.APIException import APIException
import logging

logging.basicConfig(filename='LogFile.log', filemode = 'w', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

success_code = [200,201,202]

def log_json(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        if r.status_code in success_code:
            logging.info(f'Success [{r.content}]')
        else:
            logging.error(f'Failure [{r.status_code} : {r.content}]')
            raise APIException(r.status_code, r.content)
        return r.json()
    return wrapper

def log_text(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        if r.status_code in success_code:
            logging.info(f'Success [{r.content}]')
        else:
            logging.error(f'Failure [{r.status_code} : {r.content}]')
            raise APIException(r.status_code, r.content)
        return r.text
    return wrapper


def log_boolean(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        if r.status_code == 404:
            logging.error(f'Not Found [{r.status_code} {r.content}]')
            return False

        elif r.status_code not in success_code:
            logging.error(f'Failure [{r.status_code} {r.content}]')
            raise APIException(r.status_code, r.content)

        elif r.status_code in success_code:
            logging.info(f'Success [{r.status_code} {r.content}]')
            return True

    return wrapper
