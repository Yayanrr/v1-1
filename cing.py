import websocket, json, time, datetime, requests
from datetime import datetime

import time, requests, random
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()

txtid = input('Masukan Link Live : ')
response = requests.get(txtid)
urlo = response.url
slink = urlo[34:-59]
socketstring = ("wss://id-heimdallr.spooncast.net/" + slink)
print(socketstring)
botauthtoken2 = 'a3cc3362f31d0a17e1da4ff9a2b7e2c34d965090' #token lu disini
mypesan = '{"live_id":'+slink+',"token":"'+botauthtoken2+'","event":"live_join","appversion":"4.3.16","useragent":"Android"}'###### end


def on_message(ws, message):
        global judul
        global nama
        global response3
        global status
        global timeh
        global timehl2
        global xz
        global z
        chat = json.loads(message)
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        kesurupan = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Hallo..All Of You How To The Good News Ia Always Yes!!😣"}'
        if 1 == 1:
            if z == 0:
                ws.send(kesurupan)
                z = 1
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
            print(chat['data']['author']['tag'])
        emot = [
         '🤭🤭🤭', '🙄🙄🙄', '😝😝😝', '😇😇😇', '😌😌😌', '😔😔😔', '🥺🥺🥺']
        ya = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"YA ' + nick + random.choice(emot) + '"}'
        tidak = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"TIDAK ' + nick + random.choice(emot) + '"}'
        bisajadi = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"SOKAP IH ' + nick + random.choice(emot) + '"}'
        bodoamat = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"ANDA KEPO ' + nick + random.choice(emot) + '"}'
        listjawaban = [
         ya, tidak, bisajadi, bodoamat]
        if evn == 'live_message' and psn[:1].lower() == 'a' and psn[-1:] == '?':
            kambeng = random.choice(listjawaban)
            print(kambeng)
            ws.send(kambeng)
        sapa = [' .Wellcome You😊 ',' .How Are You😋 ',' .Use Your Earphone For Qouality Music🎧 ',' .We Wish You Always Heppiness☺️ ',' .Dont Forget To Love Big Sis❣ ',' .Always Smiling !! Ya😊 ',' .Youre Funny Big Sis😁 ',' .How Is Today?☺️ ',' .Take Care Of Your Health🤭',' .You Are Cute😁']
        ljoin = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" |USER|. ' + nick + random.choice(sapa) + '"}'
        lsjoin = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"' + nick + ' Open The Spoon Radio Application Dont Fores Bro!! So 👻|GHOST|"}'
        likee = [' .Thenks For Teplove❣️',' .Thank You For Sprinkling Love☺️❣ ',' .Thank You The Fake Love😁❣ ',' .Uwu Thank You For Wanting To Love😳❣ ']
        llike = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":" |USER|.' + nick + random.choice(likee) + '"}'
        tidur = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"l Take A Break Yeah !! 😳"}'
        bangun = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"Hello Everyone.How Are You? I Came To Help !! 😳"}'
        likes = '{"appversion":"4.3.16","event":"live_messge","token":" ",useragent","Android","message":"I Help You With A Tap Love Yeah!!!😊"}'
        ping = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"HAHAHAHAHAHAHAHAHAHA !! 😂😂"}'
        makasih = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + ' Waalaikumsalam Wr. Wb. !! 😇"}'
        jawab = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Pagi Juga ' + nick + 'Jangan Lupa Sarapan Ya kak !! 😋"}'
        sokap = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Siang Juga  ' + nick + 'Jangan Lupa Bahagia Selalu Ya !! 😳"}'
        sendiri = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Sore Juha ' + nick + ' Jangan Lupa Mandi Ya !!😒"}'
        jee = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Hai Juga Akak ' + nick + ' Jangan Lupa Pencet Kado Kiri Paling bawah Buat Gift😳"}'
        ljee = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Malam Juga  ' + nick + ' Jangan Bergadang Yaa Jaga Kesehatan Akak !! 😇"}'
        promot = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" Apa Sih Uwu Uwu Akak ' + nick + 'Kek Orang Gila !!😳"}'
        rank = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"|INFO| Rank Has Been Updated ' + nick + ' Beloved 😚"}'
        if evn == 'live_message' and (psn == '!status' or psn == '!durasi' or psn == '!info'):
         headers2 = {'User-Agent': 'Mozilla/5.0'}
         response2 = requests.get(('https://id-api.spooncast.net/lives/' + slink + ''), headers=headers2)
         createdl = response2.json()['results'][0]['created']
         tanggal = datetime.today()
         cre = createdl[:-17]
         crea = createdl[11:-8]
         creat = cre + ' ' + crea
         creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
         selisih = tanggal - creatdt
         s1 = '07:00:00'
         s2 = str(selisih)[:-7]
         formatss = '%H:%M:%S'
         timehl2 = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
         ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"|INFO|ROOM THIS HASS BEEN BROADCAST FOR:🔥🔥'+ str(timehl2) +'🔥🔥' + ' "}')
        if evn == 'live_join':
            if status == 'bangun':
                ws.send(ljoin)
        if evn == 'live_shadowjoin':
            if status == 'bangun':
                ws.send(lsjoin)
        if evn  ==  'live_like'  and  status  ==  'bangun' :
            ws . send ( llike )
        if evn == 'live_message' and psn == '!off' and status == 'bangun':
            status = 'tidur'
            ws.send(tidur)
        if evn == 'live_message' and psn == '!rank':
            headers3 = {'User-Agent': 'Mozilla/5.0'}
            response3 = requests.get('https://id-api.spooncast.net/lives/popular/', headers=headers3)
            ws.send(rank)
        if evn == 'live_message' and psn[:-3] == '!rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"|INFO|Rank ' + str(xz + 1) + '  Name: ' + nama + ' Title: ' + judul + '  Duration -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn[:-2] == '!rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"|INFO|rank ' + str(xz + 1) + '  Name: ' + nama + ' Title: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn == '!me':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = tag
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"|INFO|Username ' + nn + ' The date the account was created -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn[:4] == '!cek':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = psn[5:]
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"|INFO|Username ' + nn + ' The date the account was created -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn == '!on' and status == 'tidur':
            status = 'bangun'
            ws.send(bangun)
        if evn == 'live_message' and psn[:1].lower() == 'wkwkwk':
            ws.send(ping)
        if evn == 'live_message' and psn == 'uwu':
            ws.send(promot)
        if evn == 'live_message' and psn == 'hai':
            ws.send(jee)
        if evn == 'live_message' and psn == 'malam':
            ws.send(ljee)
        if evn == 'live_message' and psn == 'assalamualaikum':
                ws.send(makasih)
        if evn == 'live_message' and psn == 'pagi':
            ws.send(jawab)
        if evn == 'live_message' and psn == 'siang':
            ws.send(sokap)
        if evn == 'live_message' and psn == 'sore':
            ws.send(sendiri)
        if evn == 'live_message':
            if psn == 'non keluar' and uid == '210900010':
                ws.close()
def on_close(ws): #on close of the bot.
    print ("### closed ###")
    
def on_open(ws): #when the bot initially connects.
 print ("open")
 time.sleep(1)
 ws.send(mypesan)
 time.sleep(1)
 gblk = """
 Connected
 """
 print(gblk)
 time.sleep(1)

if __name__ == "__main__":
 
 websocket.enableTrace(True)
 ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,                                           
                              on_message = on_message,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever()
