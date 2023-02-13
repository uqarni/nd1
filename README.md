# nd1
network diagram using slack API

This first queries Slack to generate all 1-1 DMS.
Then it filters for only those with messages in the last 60 days.
Then it saves participants as pairs of users in a list of pairs. 

That list is used to generate a network model via networkx. 
Which is then visualized in matplotlib. 
