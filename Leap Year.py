year = int(input("Enter year: "))

def leap_year(p_year):
  if p_year % 4 == 0:
    if p_year % 100 == 0:
      if p_year % 400 == 0:
        return "Leap year."
      else:
        return "Not leap year."
    else:
      return "Leap year."
  else:
    return "Not leap year."  
  
 leap_year(year)
