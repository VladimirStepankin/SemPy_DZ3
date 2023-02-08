points = { 'AEIOULNSTRАВЕИНОРСТ':1, 'DGДКЛМПУ':2, 'BCMPБГЁЬЯ':3, 'FHVWYЙЫ':4, 'KЖЗХЦЧ':5, 'JZШЭЮ':8, 'QZФЩЪ':10}
text = input().upper()
summ = 0
for i in text:
    for k, v in points.items():
        if i in k:
            summ += v
print(summ)