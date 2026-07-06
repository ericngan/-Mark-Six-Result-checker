import requests


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
            "content-type": "application/json",
            "accept-encoding": "gzip, deflate, br, zstd",
            "priority": "u=1, i",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site"    
           }
data={"operationName":"marksixDraw","variables":{},"query":"fragment lotteryDrawsFragment on LotteryDraw {\n  id\n  year\n  no\n  openDate\n  closeDate\n  drawDate\n  status\n  snowballCode\n  snowballName_en\n  snowballName_ch\n  lotteryPool {\n    sell\n    status\n    totalInvestment\n    jackpot\n    unitBet\n    estimatedPrize\n    derivedFirstPrizeDiv\n    lotteryPrizes {\n      type\n      winningUnit\n      dividend\n    }\n  }\n  drawResult {\n    drawnNo\n    xDrawnNo\n  }\n}\n\nquery marksixDraw {\n  timeOffset {\n    m6\n    ts\n  }\n  lotteryDraws {\n    ...lotteryDrawsFragment\n  }\n}"}
url="https://info.cld.hkjc.com/graphql/base/"
response=requests.post(url, headers=headers, json=data)

marksix_draws=response.json()
攪出號碼=marksix_draws["data"]["lotteryDraws"][0]["drawResult"]["drawnNo"]
特別號碼=marksix_draws["data"]["lotteryDraws"][0]["drawResult"]["xDrawnNo"]
##Check if the user input is valid
while True:
    input_numbers=input("請輸入你想檢查的號碼(用空格分隔): ")
    input_numbers_list=input_numbers.strip().split() # 將輸入的號碼字串拆分成一個列表
    try:
        numbers = []  
        for x in input_numbers_list:
            num = int(x)
            numbers.append(num)
    except ValueError:
        print("輸入無效，請重新輸入。")
        continue
    for n in numbers:
        if n < 1 or n > 49:
            print("號碼必須在1到49之間，請重新輸入。")
            continue
    if len(numbers) != len(set(numbers)):  #Set會移除重複的元素，如果長度不一樣，表示有重複的號碼
        print("號碼不能重複，請重新輸入。")
        continue
    input_numbers_list= numbers 
    break
###

#Check how many numbers match the drawn numbers
normalhit_count=0
specialhit=False
for i in range(len(input_numbers_list)):
    for j in 攪出號碼:
        if input_numbers_list[i] == j:
            normalhit_count+=1
            break
    if input_numbers_list[i] == 特別號碼:
        specialhit=True
##

print (f"攪出號碼: {攪出號碼}")
print (f"特別號碼: {特別號碼}")
if normalhit_count==6:
    print("****恭喜你中了頭獎！****")
elif normalhit_count==5 and specialhit:
    print("****恭喜你中了二獎！****")
elif normalhit_count==5:
    print("****恭喜你中了三獎！****")
elif normalhit_count==4 and specialhit:
    print("****恭喜你中了四獎！****")
elif normalhit_count==4:
    print("****恭喜你中了五獎！****")
elif normalhit_count==3 and specialhit:
    print("****恭喜你中了六獎！****")
elif normalhit_count==3:
    print("****恭喜你中了七獎！****")
else:
    print("很遺憾，你沒有中獎。")