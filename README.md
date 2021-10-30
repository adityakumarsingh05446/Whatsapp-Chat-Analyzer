
# Whatsapp Chat Analyzer

This is a streamlit based Whatsapp chat analysis project.

User is requested to export his/her chat "excluding media" into this application.

Based on some detail statistical analysis this application will provide necessary details of an "individual user" or "group of users" texting pattern.



## Statistical test done are as follows : 

- Unique users : Fetch unique users involved in chats.
- Two way analysis : Analysis is done both on individual user as well as on group level.
- Total Stats : Getting the count of "Total Messages" , "Total Words" , "Total Links" and "Total Media" shared during the chats.
- Monthly Timeline : Represents a visualization graph(Line chart) for monthly texting pattern for an individual or for a whole whatsapp group of individuals.
- Daily Timeline :  Represents a visualization graph for daily texting pattern for an individual or for a whole whatsapp group.
- Activity Map : Represents the "most busy day" and "most busy month" for entire chat flow.
- Weekly Activity Map : With the use of heatmap the most and least involvement days are shown.
- Most busy user : Represent a visualization graph of the top 5 user who are the most active in the chat process and their total message contribution in percentage.
- Word CLoud : Providing a graphical representations of word frequency that give greater prominence to words that appear more frequently in the texting process.
- Most Common Word Used : Represents the list of most Common words used in the conversation process.
- Emoji Analysis : Represents all the emojis used in a form of pie chart used in chats with their usage counts.
  
## Tools Used

Python , Pandas , NumPy , Seaborn , Matplotlib , streamlit , wordcloud , urlextract , RegEx , emoji , collections , Heroku.

## Installation Process
- Include all the files present in the repository.
- Install all the requirements listed in requirements.txt file
- Command to run streamlit based application is : streamlit run app.py

# Deployment Link
Live Project Link : https://whatsapp-chat-analyzer-demo.herokuapp.com/
(Please click the link to checkout the application.)
- Once the link is open Go to - > Browse File Option
- Export your whatsapp chat "WITHOUT MEDIA" into your local machine.
- Under Browse File Section -> Upload your whatsapp_chat.txt file
- Go to - > Show analysis based on users section on web app
- Either Select : < Overall > OR < Specific_User >
- Then select -> Show Analysis

## Future Work :
- Using the NLP techniques , will try to find out the sentiments for a selected user.
- Using more advance streamlit functions to make this web app more faster and more responsive.
- Will be trying to host this application on AWS.

## Related Usage :
- Can be used by parents on monthly basis to get their children track records , as this can help parents to get insights of their children quickly.
- Can be used for personal group analysis.
- Can be used for tracking the trends invloved by mischievous scammers involved in textual converstions. 

## Video
https://user-images.githubusercontent.com/83591758/139529208-a7502e57-7af5-4fa5-aa7d-c1cf478da29c.mp4


