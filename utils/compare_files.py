import re
import requests

path = '/home/ffeller/repo/cfa-myo/'

def read_file(file_name, base_path = path):
    full_path = base_path + file_name
    file = open(full_path, "r")
    content = set(file.read().split("\n"))
    content.remove('')
    content = filter(lambda x: not x.startswith('#'), content)
    content = map(lambda x: re.sub(r"\s+=\s+", "=", x), content)
    content = set(content)
    content = map(lambda x:(x.split('=')[0].strip(), x.split('=')[1].strip()), content)
    return dict(content)


def calculate_intersaction(list):
    a = None
    for x in list:
        xset = set(x.keys())
        if a is None:
            a = xset
        a = a.intersection(xset)
    return a


def read_service(url):
    r = requests.get(url)
    return r.json()


def compare(domain, all):
    for key in domain:
        all_values = set(map(lambda x:x[key], all))
    all_values.add(domain[key])
    if (len(all_values) > 1):
        print("{}: {}".format(key, all_values))


new_prod = read_file('new_prod_environment.properties', '/home/ffeller/Downloads/')
old_prod = read_file('old_prod_environment.properties', '/home/ffeller/Downloads/')

domain = read_file('domain.properties', '/home/ffeller/Downloads/')
prod = read_file('support/prod/conf/env/environment.properties')
beta = read_file('support/beta/conf/env/environment.properties')
ic = read_file('support/ic/conf/env/environment.properties')
rc = read_file('support/rc/conf/env/environment.properties')
int_test = read_file('cfa-myo-test-integration/src/test/resources/conf/env/environment.properties')
main = read_file('cfa-myo-domain/src/main/resources/conf/env/environment.properties')

all = [prod, beta, ic, rc, int_test, main]




for key in old_prod:
    if not (key in new_prod):
        if not (key in domain):
            print(key)