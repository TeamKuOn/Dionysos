import sys, time, requests, json

def main():
    interval_sec = 5 

    while(True):
        start_time = time.time()
        
        print('Data sending ...')
        
        try:
            request = requests.post('http://harvest.soracom.io', data=json.dumps(payload), headers=headers, timeout=5)
            print(request)
        except requests.exceptions.ConnectTimeout:
            print('ERROR: 接続がタイムアウトしました。"connect_air.sh" は実行していますか？')
            if request.status_code == 400:
                print('ERROR: データ送信に失敗しました。Harvest が有効になっていない可能性があります。')
        
        wait_time = start_time + interval_sec - start_time
        if wait_time > 0:
            time.sleep(wait_time)
            
if __name__ == '__main__':
    main()