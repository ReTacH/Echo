# PROJECT PROPOSAL: Echo Chamber in Social Media
This repository is created to document the progress on the class PIC 16B project on quantifying the echo chamber which arise in the social media

# Abstract
Echochamber is a situation where one only considers opinions that agree with their own. Such situations have been observed in multiple social platforms, especially in the context of politics where people only believed in the words of their own chosen political party. Here, building upon the models of polarity by Garimella et al., we investigate the formation of echochamber in social media, particularly in Twitter, using complex visualizations in Python. In addition we plan to reduce the bias of the datasets by considering a sentimental analysis to see whether a person tweets in a positive or negative way and to implement machine learning models to quantitatively separate each echo chamber aparts rigorously.

# Planned Deliverables
## Full Success
Using techniques from data science and scientific computing, we are able to quantify and create complex visualizations of the formation of echochamber in social media. We are able to successfully deploy machine learning models, such as k-means or spectral clustering, to segregate each chamber apart and analyze its dependency on the social network structures created from the dataset. In addition, we are able to reduce the biases in the dataset by cleaning the datasets with the help of natural language processing models. We expect that most of the projects will be done on a jupyter notebook.

## Partial Success
We are able to create a simple visualization that observed two different clusters representing the two chambers for the polarity in the voting systems; in the process of such visualization, we first need to construct a social network from the datasets and deploy a simple natural language processing model to extract the data from a tweet. The project will be mostly done on a jupyter notebook.

# Resources Required
We have gotten the dataset from the authors in the following paper: [Political Discourse on Social Media: Echo Chambers, Gatekeepers, and the Price of Bipartisanship (arxiv.org)](https://arxiv.org/pdf/1801.01665.pdf) This papers consider 10 datasets ranging from tweets about gun control to tweets about Game of throne discussions. In our cases, we focus on the three datasets: obamacare, abortion and foodporn.

# Tools and Skills Required
- Complex visualizations based on Python modules such as Matplotlib and Seaborn
- Natural language processing tools from Python/Tensorflow to extract the sentiments on each tweets
- Creation of large social networks and simple community detection methods from NetworkX modules in Python
- Clustering-based machine learning models such as K-means clustering and Spectral clustering which could be done using Scikit-learn in Python 

# What You Will Learn
- Ability to acquire data (research, directly ask, etc)
- Techniques to deal with small snippets of text data
- Knowledge of math in quantifying abstract ideas/phenomenons (in this case echo chamber), and in categorizing based on quantified value (for example, not just whether it’s smaller than delta, but more advanced technique)
- Danger of social media for creating echo chamber

# Risks
1. The datasets that we are considering contain the number of tweets ranging from 20 million (on gun control) to 40 million (on Obamacare); this is considered pretty large as each tweet also contains a couple sentences as well. Such large data may require extensive computational power to deploy machine learning models than is available on our local machine. However, we could still extract only a fraction of the datasets to be used as well; though, more consideration is needed to consider which subset of the datasets is important to our analysis.
2. While the authors in the paper we described in the Resources Required section demonstrate that they observed the echo chamber in their datasets; it might actually be the results of hand-picking the datasets which contain a lot of polarity in itself. In this sense, if we test our identical models on different datasets, we may or may not be able to observe the formation of echo chambers anymore. Thus, more thorough investigations are needed in this direction.

# Ethics

- What groups of people have the potential to benefit from the existence of our product?
	- People who are open to different opinions can benefit from acknowledging the echo chamber among them, because so that they can make changes in their lives in accordance with the research result.
- What groups of people have the potential to be harmed from the existence of our product?
	- Twitter and other social media platforms might be harmed by the research result, because it points out a huge flaw of obtaining information through social media. Their employees and stockholders might be harmed.
	- If we do a sentiment analysis on the languages to make the leaningness calculation more precise, it might be limited to English. But this is ignoring a large community of Spanish speaking population (13% of population, 41.8 million according to the 2019 survey), and some other languages’ population. Among the Spanish speakers, around 12 million are bilingual, but we don’t know whether they use Spanish as their primary language (especially when tweeting in this scenario).
- Will the world become an overall better place because of the existence of our product? Describe at least 2 assumptions behind your answer.
	- Echo chamber can be quantified based on what news agency people quote from
	- The world is a better place when people realize that they’re only hearing one voice that agrees with theirs


