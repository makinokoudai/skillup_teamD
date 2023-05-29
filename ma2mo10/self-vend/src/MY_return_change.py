#お釣り関係のモジュール
from typing import Dict

def changecalc(change:int) -> Dict[str, int]:
    '''お釣りを計算する'''

    #貨幣の数をカウントする変数
    ten_thousand_cnt = 0
    five_thousand_cnt = 0
    thousand_cnt = 0
    five_handred_cnt = 0
    handred_cnt = 0
    fifty_cnt = 0
    ten_cnt = 0

    #お釣りの計算
    
    #1万円札の枚数カウント
    if change % 10000 == 0:
        change -= 10000
        ten_thousand_cnt += 1

    
    #5千円札の枚数カウント
    while change >= 5000:
        change -= 5000
        five_thousand_cnt += 1

    #千円札の枚数カウント
    while change >= 1000:
        change -= 1000
        thousand_cnt += 1

    #5百円玉の枚数カウント
    while change >= 500:
        change -= 500
        five_handred_cnt += 1

    #百円玉の枚数カウント
    while change >= 100:
        change -= 100
        handred_cnt += 1

    #五十円玉の枚数カウント
    while change >= 50:
        change -= 50
        fifty_cnt += 1

    #十円玉の枚数カウント
    while change >= 10:
        change -= 10
        ten_cnt += 1
    
    #お釣りを貨幣の種類ごとに格納した辞書を生成
    change_dict = {"1万円札":ten_thousand_cnt, "5千円札":five_thousand_cnt, "千円札":thousand_cnt, 
                   "五百円玉":five_handred_cnt, "百円玉":handred_cnt, "五十円玉":fifty_cnt, "十円玉":ten_cnt}
    return change_dict

#求めたお釣りを表示
def changedisplay(change_dict:Dict[str, int]) -> None:
    '''お釣りの表示'''
    print("おつり")
    for change in change_dict:
        if change_dict[change] > 0:
            print(f"{change}：{change_dict[change]}")
            
