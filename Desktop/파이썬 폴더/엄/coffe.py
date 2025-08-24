gasu=10
coffeone=300
while 1:
    money=int(input("돈을 넣어주세요 (커피 한잔 300원) 종료하려면 q를 입력하세요."))
    remove=int(input("커피를 몇잔 사실건가요? (개)"))
    if money =="q":
        break
    else:
        if coffeone*remove > money:
            print("돈이 부족합니다. 커피 한잔은 300원 입니다.")
            print(f"남은 커피는{gasu} 입니다.")
        else:
            if gasu==0:
                print(" 커피가 모두 소진되었습니다. 자판기를 종료합니다.")
                break
            elif gasu<remove:
                print(f"커피가 {gasu}잔밖에 남지 않았습니다. {gasu}잔을 제공합니다.")
                print(f"거스름돈 {money-(gasu*remove)}원입니다.")
                gasu-=remove
                print(f"남은 커피는 {gasu}개입니다")
            else:
                print(f"커피 {gasu}잔을 제공되었습니다.")
                print(f"거스름돈 {money-(gasu*remove)}원입니다.")
                gasu-=remove
                print(f"남은 커피는 {gasu}개입니다")




'''
문제------------------------------------------------------------------------------------------------
#while문을 이용한 커피 자판기 프로그램.
커피의 갯수는 10개이고, 커피한잔은 300원.
사용자에게 금액을 입력받아 커피를 판매하고 q를 누르면 프로그램 종료.
사용자문구 : 돈을 넣어주세요 (커피 한잔 300원) 종료하려면 q를 입력하세요:

커피 재고보다 더 많이 주문한 경우 
	커피가 x잔밖에 남지 않았습니다. x잔을 제공합니다.
	거스름돈 x원입니다.
	남은 커피는 x개입니다.
충분한 커피가 있을 경우
	커피 x잔이 제공되었습니다. 거스름돈 x원입니다
	남은 커피는 x개입니다.

	
사용자가 q를 입력했을때 '자판기를 종료합니다.' 문구 출력'''