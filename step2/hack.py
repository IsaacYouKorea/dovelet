# hack
# r 은 홍보를 하지 않을 경우의 수입
# e 는 홍보를 할 경우의 수입
# c 는 홍보 비용
r, e, c = map(int, input().split(" "))
result = "does not matter"

if(r > (e - c)):
  result = "do not advertise"
elif(r < (e -c )):
  result =  "advertise"

print(result)
#"advertise" : 홍보를 할 경우 유리한 경우
#"do not advertise" : 차라리 홍보를 하지 않을 경우 유리한 경우
#"does not matter" : 하던 , 안하던 수입이 같은 경우
