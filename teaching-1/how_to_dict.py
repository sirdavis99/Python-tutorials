# Assessment 

# Question 1
# create a dictionary of 9 variables (
#     photo_url, name, age, gender, class, buisness, 
#     best_color, no_of_children, address
# )

info = {
      'Name':'Buraimoh Motunrayo',
      'Age': '25',
      'Gender':'female',
      'No_of_children': '2',
      'class':'400 level', 
      'photo_url':'https://image.shutterstock.com/z/stock-photo-a-picture-of-the-behttps://image.shutterstock.com/z/stock-photo-a-picture-of-the-beautiful-view-of-birds-1836263689.jpgautiful-view-of-birds-1836263689.jpg'
}
  

# Question 2
# create a function that changes each value of a variable in the dictionary of question 1
# eg: change('name', 'Julius Berger') which will change the value of name in the dictionary 
# variable created before
def change(variable, new_value):
      info[variable] = new_value

      
change('Name', 'David Echu')   

print(info['Name'])  