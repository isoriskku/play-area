import requests
import json

# change input addr to official addr
def ChangeAddr(addr):
    host = 'https://dapi.kakao.com'
    path = '/v2/local/search/address.json'
    url = host + path

    headers = {'Authorization': 'KakaoAK 4947680dbf018a91dee06ef53217bc61'}
    params = {'query': addr}    # input addr

    res = requests.get(url, headers=headers, params=params)

    if(res.status_code == 200):
        result = json.loads(str(res.text))
        if(result['meta']['total_count'] > 0):
            # region names, it is official addr
            region_1depth_name = result['documents'][0]['address']['region_1depth_name']
            region_2depth_name = result['documents'][0]['address']['region_2depth_name']
            region_3depth_name = result['documents'][0]['address']['region_3depth_name']
            address_name = region_1depth_name + ' ' + region_2depth_name + ' ' + region_3depth_name

            return address_name
        else:
            return 'Invalid address'
    else:
        return 'The input parameter value is not in the service area'

# change latitude, longtitude to official addr
def getAddr(latitude, longtitude):
    host = 'https://dapi.kakao.com'
    path = '/v2/local/geo/coord2address.json'
    url = host + path

    headers = {'Authorization': 'KakaoAK 4947680dbf018a91dee06ef53217bc61'}
    params = {'x': longtitude, 'y': latitude}   # input

    res = requests.get(url, headers=headers, params=params)

    if(res.status_code == 200):
        result = json.loads(str(res.text))
        # region names, it is official addr
        region_1depth_name = result['documents'][0]['address']['region_1depth_name']
        region_2depth_name = result['documents'][0]['address']['region_2depth_name']
        region_3depth_name = result['documents'][0]['address']['region_3depth_name']
        address_name = region_1depth_name + ' ' + region_2depth_name + ' ' + region_3depth_name

        return address_name
    else:
        return 'The input parameter value is not in the service area'

def setPlayArea():
    while(True):
        playAddr = input('Set play area: ')
        addr = ChangeAddr(playAddr) # change input to official

        if(addr != 'Invalid address'):
            break
        print('check your input address')
        
    f = open('play_area.txt', 'a')
    f.write(addr + '\n')
    f.close()


def delPlayArea():
    f = open('play_area.txt', 'r')

    addrs = []
    for x in f.readlines():
        addrs.append(x[:-1])

    # select deleting addr
    while(True):
        sel = int(input('select address number: '))
        if(0 <= sel and sel < len(addrs)):
            del addrs[sel - 1]
            break
        print('check your input number')

    f.close()

    # after delete addr, save remaning addr to file
    f = open('play_area.txt', 'w')
    for x in addrs:
        f.write(x + '\n')
    f.close()


# print play area list
def showPlayArea():
    f = open('play_area.txt', 'r')
    cnt = 0
    addrs = []
    print('-' * 10, 'play area list', '-' * 10)
    for x in f.readlines():
        print(str(cnt + 1) + '. ' +  x[:-1])
        addrs.append(x[:-1])
        cnt += 1
    print('-' * 36)
    f.close()


# return play area list
def getPlayArea():
    f = open('play_area.txt', 'r')
    addrs = []
    for x in f.readlines():
        addrs.append(x[:-1])
    f.close()

    return addrs


def CheckArea(gps_la, gps_lo):
    addrs = getPlayArea()
    findAddr = getAddr(gps_la, gps_lo)

    #print(addr)
    #print(findAddr)

    for addr in addrs:
        if(addr == findAddr):   # True return if current addr is inside at least one play area
            print(addr + ' 안에 있음')
            return True
    return False # False return if current addr is out of all play area
