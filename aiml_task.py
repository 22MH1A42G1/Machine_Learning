
######################################Bar-Graph-1
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\spotify-2023.csv", encoding='latin1')

released_year = data['released_year'] 
in_spotify_playlists = data['in_spotify_playlists'] 

plt.plot(released_year, in_spotify_playlists, c='b', linestyle="solid", linewidth=3)
plt.title("Most Famous Songs and Released Years")
plt.barh(released_year, in_spotify_playlists, color='r')
plt.xlabel("in_spotify_playlists")
plt.ylabel("released_year")
plt.show()



##############################################pie chart-1
##import matplotlib.pyplot as plt
##import pandas as pd
##
##data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\spotify-2023.csv", encoding='latin1')
##
##labels = data['released_year']  
##sizes = data['in_spotify_playlists'] 
##
##
##plt.figure(figsize=(8, 8))
##plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
##plt.title("Most Famous Songs and Released Years")
##plt.show()

############################################BarGraph-2

##import matplotlib.pyplot as plt
##import pandas as pd
##
##data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\spotify-2023.csv", encoding='latin1')
##
##released_year = data['released_year'] 
##in_spotify_playlists = data['in_spotify_playlists'] 
##
##plt.bar(released_year, in_spotify_playlists, color='yellow')
##plt.title("Most Famous Songs and Released Years",color='red',fontsize=20)
##plt.xlabel("Released Year",color='blue',fontsize=18)
##plt.ylabel("in_spotify_playlists",color='blue',fontsize=18)
##plt.show()

############################################BarGraph-3

##import matplotlib.pyplot as plt
##import pandas as pd
##
##data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\spotify-2023.csv", encoding='latin1')
##
##released_year = data['in_deezer_charts'] 
##in_spotify_playlists = data['released_month'] 
##
##plt.bar(released_year, in_spotify_playlists, color='g')
##plt.title("Most Famous Songs and Released Years",color='red',fontsize=20)
##plt.xlabel("in_deezer_charts",color='blue', fontsize=18)
##plt.ylabel("released_month",color='blue', fontsize=18)
##plt.show()














