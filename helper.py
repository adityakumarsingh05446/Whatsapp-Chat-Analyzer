# This file contains all the required functions

from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

#<---------------------------------------STATS AREA OF CODE------------------------------------------------>
def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
    # 1. Extracting number of messages for selected user
        df = df[df['user'] == selected_user]
    num_messages = df.shape[0]

    # 2. Extracting number of words for selected user
    words = []
    for message in df['message']:
        words.extend(message.split())

    # 3. Extracting the count of media messages shared
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # 4. Extract the count of number of links shared
    num_links = []

    for message in df['message']:
        num_links.extend(extract.find_urls(message))

    return num_messages, len(words) , num_media_messages , len(num_links)

#<-----------------------------------END OF STATS AREA OF CODE------------------------------------------------>

# 5. Finding the busiest user in the group : Will only work at <Group level>
def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Username', 'user': 'Percentage'})
    return x,df
# <------------------------------------------------------------------------------------------------------------->

# 6. Word Cloud formation
def create_wordcloud(selected_user,df):

    # File reading section
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Removing group notification and media omitted words
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Nested functions
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    # Properties for word cloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')

    # Here applying the nested function
    temp['message'] = temp['message'].apply(remove_stop_words)

    # Generate image for word cloud
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

# <------------------------------------------------------------------------------------------------------------->

# 7. Most Common Words used
def most_common_words(selected_user,df):

    # File reading section
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Removing group notification and media omitted words
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

# <------------------------------------------------------------------------------------------------------------->

# 8. Emoji Analysis : Extracting the count of maximum used emojis

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

# <---------------------------------------------------------------------------------------------------------------->

# 9. Monthly TimeLine

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

# <---------------------------------------------------------------------------------------------------------------->

# 10. Daily Timeline
def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

# <---------------------------------------------------------------------------------------------------------------->

# 11. Weekly Timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap

















"""
    if selected_user == 'Overall':
        # 1. Extracting number of messages overall
        num_messages = df.shape[0]
        # 2. Extracting number of words overall
        words = []
        for message in df['message']:
            words.extend(message.split())
        return num_messages,len(words)
    else:
        # 1. Extracting number of messages for selected user
        new_df = df[df['user'] == selected_user]
        num_messages = new_df.shape[0]
        # 2. Extracting number of words for selected user
        words = []
        for message in new_df['message']:
            words.extend(message.split())
        return num_messages,len(words)
"""