from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
from datetime import datetime, timedelta
import time 
import sys
import networkx as nx
import matplotlib.pyplot as plt

# Initialize a WebClient using the Slack API token
client = WebClient(token="xoxp-4722272326211-4746079437552-4735141885857-60d03e26d00030111a3e8a54542199e9")

try:

    #var dms = list of all conversation IDs of 1-1 DMs with messages in the last 60 days 
    dms = []
    convos = client.conversations_list(types = "im")
    convos = convos["channels"]
    print(len(convos)) 

    for convo in convos:
        id = convo["id"]
        sixty_days_ago = datetime.now() - timedelta(days = 60)
        sixty_days_ago = sixty_days_ago.strftime("%s")
        messages = client.conversations_history(channel = id, oldest = sixty_days_ago)
        messages = messages["messages"]
        if len(messages)>0:
            dms.append(convo["id"])



    #get all unique pairs of user IDs from these 1-1 conversations in a list (pairs)
    pairs = []
    for dm in dms:
        duos = client.conversations_members(channel = dm)
        duos = duos["members"]  
        for index,i in enumerate(duos):
            name = client.users_info(user = i)
            name = name["user"]["name"]
            duos[index] = name
        pairs.append(duos)

    G = nx.Graph()
    G.add_edges_from(pairs)
    print("nodes:")
    print(G.number_of_nodes())
    print("edges:")
    print(G.number_of_edges())
    nx.draw_networkx(G)
    plt.show()

    


except SlackApiError as e:
    print("Error : {}".format(e))


