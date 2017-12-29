import datetime
import Tkinter as tk
from PIL import Image, ImageTk

# this will open a window using Tkinter
window = tk.Tk()
window.geometry("300x200")
window.title("Age Calculator App")

label = tk.Label(text = 'Name')
label.grid(column = 0 , row = 1)


label1 = tk.Label(text = 'Year')
label1.grid(column = 0 , row = 2)


label2 = tk.Label(text = 'Month')
label2.grid(column = 0 , row = 3)

label3 = tk.Label(text = 'Day')
label3.grid(column = 0 , row = 4)

name_entry = tk.Entry()
name_entry.grid(column = 1, row = 1)

year_entry = tk.Entry()
year_entry.grid(column = 1, row = 2)

month_entry = tk.Entry()
month_entry.grid(column = 1, row = 3)

day_entry = tk.Entry()
day_entry.grid(column = 1, row =4 )

# this functiom will print age and name in text box
def calculate_age():
    person = Person(str(name_entry.get()),datetime.date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get())))
    text_answer = tk.Text(master = window, height =20, width =30)
    text_answer.grid(column = 1, row = 5)
    answer_text = "{name} is {age} years old".format(name =person.name,age =person.age())
    text_answer.insert(tk.END, answer_text)

calculate_button = tk.Button(window, text = 'submit', command = calculate_age)
calculate_button.grid(column = 1, row = 5)



# this class will calculate age
class Person:

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def age(self):
        today = datetime.date.today()
        age  = today.year - self.birth_date.year
        return age

image = Image.open('/home/krish/age.jpg')
image.thumbnail((100,100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image = photo)
label_image.grid(column = 1, row = 0)

# this is used to keep the window
window.mainloop()
