dict = {
    1:690,
    2:420,
    3:530,
    4:330
    }
result= 0
i = int(input('Anda ingin memasukkan berapa sapi? ')) 
kata = []
while i > 0:
    print('masukan kata: ',end='')
    o = int(input())
    kata.append(o)
    i-=1
print(kata)
for i in kata:
    result += dict[i]
print(result)
year =result//365
month=(result-year*365)//30
day=(result-year*365- month*30)
print(f"Jumlah hari yang diperlukan ialah : {year} Tahun, {month} Bulan, dan {day}Hari")
