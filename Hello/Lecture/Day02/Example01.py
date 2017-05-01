# 19920822를 년월일로 구분하시오
birth = 19920822
year = birth//10000
print("year : " , year)
month = birth//100%100
print("month : ", month )
month = birth%10000//100
print("month : ", month )
date = birth%100
print("date : ", date )
