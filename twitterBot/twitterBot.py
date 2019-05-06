from login import api
import requests
import datetime
from datetime import datetime as dt
import time
import requests
import shutil

def showLists(owner_name):
    for twilist in api.lists_all(screen_name=owner_name):
        print("slug="+twilist.slug)
        print("name="+twilist.name)

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def main():
#    showLists("lemontheta")
    tl = api.list_timeline('lemontheta', 'list', count=10)
    for status in tl:
        try :
            url=status.extended_entities['media'][0]['media_url']
            print(url)
            tdatetime = dt.now()
            filename='img/'+tdatetime.strftime('%Y%m%d%H%M%S')+'.jpg'  #"img"というサブフォルダに保存
            download_img(url,filename)
            time.sleep(1) #上書きされるので1秒待ってファイル名が変わるようにする
        except:
            pass #画像がないときはなにもしない
        # #見映えのため区切る
        # print('-------------------------------------------')
        # #ユーザ名表示
        # print('name:' + status.user.name)
        # #内容表示
        # print(status.text)


if __name__ == "__main__":
    main()
