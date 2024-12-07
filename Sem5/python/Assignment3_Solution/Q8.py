def days_in_month(month):
    month = month.lower()
    match month:
        case 'january' | 'march' | 'may' | 'july' | 'august' | 'october' | 'december':
            return "31 days"
        case 'april' | 'june' | 'september' | 'november':
            return "30 days"
        case 'february':
            return "28/29 days"
        case _:
            return "Invalid month name"


print(days_in_month('FebrUary')) 
