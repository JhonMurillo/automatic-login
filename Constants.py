import json
INST_USER= INST_PASS= USER= PASS= HOST= DATABASE= POST_COMMENTS= ''
LIKES_LIMIT= DAYS_TO_UNFOLLOW= CHECK_FOLLOWERS_EVERY= 0
PATH_CHROME= URL_LOGIN= URL_SCREENSHOT= HASHTAGS= [] 

def init(path):
    global INST_USER, INST_PASS, USER, PASS, HOST, DATABASE, LIKES_LIMIT, DAYS_TO_UNFOLLOW, CHECK_FOLLOWERS_EVERY, HASHTAGS, URL_LOGIN, PATH_CHROME, URL_SCREENSHOT
    # read file
    data = None
    with open(path+'settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    INST_USER = obj['credential']['user']
    INST_PASS = obj['credential']['pass']
    URL_LOGIN = obj['credential']['url_login']
    USER = obj['db']['user']
    HOST = obj['db']['host']
    PASS = obj['db']['pass']
    DATABASE = obj['db']['database']
    LIKES_LIMIT = obj['config']['likes_over']
    CHECK_FOLLOWERS_EVERY = obj['config']['check_followers_every']
    HASHTAGS = obj['config']['hashtags']
    DAYS_TO_UNFOLLOW = obj['config']['days_to_unfollow']
    PATH_CHROME = obj['config']['path_chrome']
    URL_SCREENSHOT= path+obj['config']['url_screenshot']