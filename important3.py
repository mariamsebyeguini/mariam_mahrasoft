from datetime import datetime,date,time,timedelta
maintenant=datetime.now()
print(maintenant)
ma_date=datetime(2006,2,22,14,30)
print(ma_date)
print(maintenant.strftime("%d/%m/%y/%H:%M"))
dans_une_semaine=maintenant+timedelta(days=7)
print(dans_une_semaine)

noel=datetime(2025,12,25)
difference=noel-maintenant
print(f"jours jusqu'a noel:{difference.days}")