from time import sleep
import time
import requests
import json
# requests移除告警
import urllib3
from playwright.sync_api import Page

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check_order_status(page: Page, order_number):
    """檢查訂單狀態"""
    # 獲取當前登錄token
    session_storage = json.loads(page.evaluate("() => JSON.stringify(sessionStorage)"))
    token = session_storage['token']
    url = 'https://172.30.22.169/api/cso-server/queryOrdersNew'
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": token
    }
    body = {
        "pageNum": 1,
        "pageSize": 10,
        "orderStatus": "-1,0,1,2,3,5,6,7,8,10",
        "serviceType": "",
        "serviceActions": "",
        "shopCodes": "",
        "orderNumber": order_number,
        "customerName": "",
        "serviceNumber": "",
        "lastHandlerName": "",
        "onlyShowMySuspendOrder": False,
        "isShowSuspendOrderToday": False,
        "accountNumber": "",
        "identityNumber": "",
        "contactTelephone": "",
        "onlyShowMyCompletedOrder": False,
        "isShowCompletedOrderToday": False,
        "fuzzySearchFlag": False,
        "finishedDateStart": "",
        "finishedDateEnd": ""
    }
    # 輪詢10分鐘調接口查詢訂單狀態，已完成返true，超過10分鐘沒有完成則false
    # 輪詢時間(秒)
    polling_duration = 10 * 60  # 10分鐘
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= polling_duration:
            return False
        else:
            re = requests.request('get', url, headers=header, params=body, verify=False)
            result = re.json()
            if result['data']['list'][0]['orderStatus'] == 6:
                return True
        sleep(15)
