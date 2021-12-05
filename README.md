# Echo-chamber
This repository is created to document the progress on the class PIC 16B project on quantifying the echo chamber which arise in the social media

## The Project Details
We obtained data from the author of *Political Discourse on Social Media: Echo Chambers, Gatekeepers, and the Price of Bipartisanship (2018)*, and conducted analysis on the **tweets data** (all tweets in June 22–29, 2015 that contains hashtag "obamacare") and the **user network data** (all users for the tweets with an edge (u → v) indicates that user u follows user v).\
In our analysis, we generated visualizations to explore the existance of echo chamber in this topic. Then we published our findings on a webapp. \
Specifically, we did the following in the analysis: 
1. Cleaned the **tweets dataset** and filtered it (only the tweets with quoted domains)
2. Calculated the political polarity scores of the users of these tweets (only the users with known polarity scores)
3. Identified clusterings of users based on Polarity Scores using Agglomerative Clustering, Spectral Clustering, and Heatmap
4. Identified communities of users based user **network data** using the modularity community detection method

We have the following findings: 
1. The clusterings we found based on the polarity scores and the user network are quite similar.
2. There is a **strong correlation** between the Twitter social network structures and derived polarity scores.
3. We hypothesize that, the Twitter Echo Chamber also makes people only follow those with the same polarity (i.e. what they want to hear).



## To See Our Results
We implemented a webapp with flask to 
1. give a short introduction of what echo chamber is
2. introduce the methods we used in this project
3. publish our findings with all the visualizations

All of our research results are posted on the webapp. To access it, you can do the following: 

1. Have flask installed on your computer; if you haven't done so, see [installation manual](https://flask.palletsprojects.com/en/2.0.x/installation/)
2. Save the `webapp` folder in your local directory.
3. In your commandline tool, navigate to the `webapp` folder (inside of it).
4. Type `flask run` to run flask on the webapp.
5. Now if you type `localhost:5000` in your browser, you should be able to use the webapp!


### Limitations
1. We filtered the **tweets data** when conducting the analysis, thus the results we found might be biased.
2. There might be the “amplification bias”, since many people tweet about the topic without hashtag.
3. Our method estimates the political polarity of a tweet using the domain it quotes from; however, when a person quotes from a domain, he/she is not necessarily agreeing with the quote.


## To See Our Analysis Process
We included all the code we used for the findings in `Echochamber_Project_Notebook.ipynb`. You can see the specific methods we used in this file. 

## Data
Since we obtained the data from Kiran Garimella et al., we're not able to publish the data on this repository. If you're interested in this topic and the data,  you can contact the author about it. 