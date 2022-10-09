'''You're working at a company that sells second-hand cars. Your company
constantly collects feedback in the form of customer reviews. Your manager 
asks you to take those reviews (saved as .txt files) and display them on your 
company's website. To do this, you'll need to write a script 
to convert those .txt files and process them into Python dictionaries,
then upload the data onto your company's website (currently using Django).'''


import os
import requests


feedbacks_dir = '//Users/vicky/Desktop/Desktop/CodePracticePython/IT_Authomation/proj2/'
url = 'http://35.184.161.79/feedback/' 

files = os.listdir(feedbacks_dir)
infor =['title', 'name', 'date','feedback']; d={}
for file in files:
  if file !='responce_post.py':
        i = 0
        with open(os.path.join(feedbacks_dir,file),'r') as infile:
            for line in infile:
                d[infor[i]] = line.rstrip()
                i +=1
        responce = requests.post(url, data = d)
        print(responce)
          
          


# feedbacks_dir = '//Users/vicky/Desktop/Desktop/CodePracticePython/IT_Authomation/proj2/'
# url = 'http://35.184.161.79/feedback/' 

# files = os.listdir(feedbacks_dir)

# for file in files:
#   if file !='responce_post.py':
#     file_obj = open(os.path.join(feedbacks_dir, file), 'r')

#     lines = [ line.replace('\n', '') for line in file_obj ]

#     feedback_dict = { "title": lines[0], "name": lines[1], "date": lines[2], "feedback": lines[3] }

#     res = requests.post(url, data=feedback_dict)

#   if not res.status_code == 201:
#     print('Something went wrong')

#   file_obj.close()


                    
                    
                