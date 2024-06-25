#------------------------------------------------------------------------------
# Розраховує кількість днів між заданою датою і поточною датою
# Приймає 'PPPP-MM-DD', повертає ціле число
# Якщо задана дата пізніша за поточну, результат є від'ємним
# Має впоратися з неправильним форматом вхідних даних
#------------------------------------------------------------------------------
# мабуть, в прикладі все ж таки -157, а не 157 - жовтень пізніше травня

def get_days_from_today(date):
    from datetime import datetime
    try:
        given_datetime = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(f"{date} isn't in format PPPP-MM-DD")
        return
    current_datetime = datetime.now()
    days_since = current_datetime.toordinal() - given_datetime.toordinal()
    return days_since

print(get_days_from_today("2000-01-01"))
