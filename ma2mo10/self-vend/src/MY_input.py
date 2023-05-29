#入力関係のモジュール
from MY_return_change import changecalc, changedisplay
import MY_param as param

def input_money():
   '''入力金額を受け取る関数'''

   money = int(input("投入金額を投入して下さい"))

   #条件に合致する場合に例外処理を行う
   while True:
      if money > param.const.LIMIT_MONEY:
         money = int(input(f"{param.const.LIMIT_MONEY}円を超える金額は投入できません。再度投入金額を入力してください"))
      elif money % 2 != 0:
         money = int(input("1円玉、5円玉は使用できません。再度投入金額を入力してください"))
      elif money < param.const.MIN_PRICE:
         money = int(input(f"{money}円では購入できる商品がありません。再度投入金額を入力してください"))
      else:
         #moneyの値が正常ならmoneyをreturnする
         return money


def input_item(money:int) -> str:
   '''商品名の入力を受け取る関数'''
   item_name = input("何を購入しますか（商品名/cancel）")

   #cancelが入力された場合お釣りを返す
   while True:
      if item_name == "cancel":
         changedisplay(changecalc(money))
         return ""
      # 正しい商品が入力されなかった場合
      elif item_name not in param.const.item_dict:
         print("商品名が間違っています。正しい商品名を入力してください")
         item_name = input("何を購入しますか（商品名/cancel）")
      else:
         # 商品名を返す
         return item_name
   

def input_YorN() -> bool:
   '''YかNを受け取る関数'''
   while True:
      input_flag = input("続けて購入しますか（Y/N）")
      if input_flag == 'Y' or input_flag == "N":
         return input_flag
      else: 
         #Y/N以外が入力された際の例外処理
         print("(Y/N)だけを入力してください")