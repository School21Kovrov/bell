hour_p = 8 #время начала урока(часы)
minute_p = 0 #время начала урока(минуты)
bell_count=0 #ключ
peremena_count = 27 #Количество звонков(По будням 27, в воскресенье 0, а в субботу 14-18)
hour = int(input()) #Текущий час
minute = int(input()) #Текущая минута
peremena_time = 10 #Время между звонками на перемене
urok_time=40#Время между звонками на уроке
prazdniki=0 #Если сокращённая смена, то значение должно равняться 5, если не сокращённая, то 0
for i in range(peremena_count):
    if (hour_p == 13) and (minute_p == 40) and (prazdniki==0):
        bell_count-=2
    if (hour_p == 13) and (minute_p == 50) and (prazdniki==0):
        bell_count+=1                                            #Дополнительные условия, связанные со звонками между сменами
    if ((hour == hour_p) and (minute <= minute_p)) or ((hour < hour_p) and (minute >= minute_p)): #условия
        next_bell = bell_count
        break
    if (hour_p == 13) and (minute_p == 50) and (prazdniki==0):
        urok_time = 40
    if (hour_p == 18) and (minute_p >= 0) and (prazdniki==0): #Укорачиваем перемену на 5 минут(Для звонка в (18:05)
        peremena_time-=5
    if (hour_p == 13) and (minute_p == 0) and (prazdniki==0):
        bell_count +=1
    if (hour_p == 13) and (minute_p == 10) and (prazdniki==0):
        urok_time = 30                                         #Дополнительные условия, связанные со звонками между сменами
    if bell_count % 2 == 0:
        time_full=hour_p*60+minute_p+urok_time-prazdniki
    if bell_count % 2 != 0:
        time_full=hour_p*60+minute_p+peremena_time  #смотрим, что сейчас, урок(40 минут) или перемена(10 минут) и прибавляем, чтобы узнать время следующего звонка
    hour_p=time_full//60 
    bell_count+=1
    minute_p=time_full%60 #находим время следующего звонка
    if (hour_p == 18) and (minute_p >= 6) and (prazdniki==0):
        peremena_time+=5   #Возвращаем перемене 5 минут(Для звонка в (18:05)
print(next_bell)
