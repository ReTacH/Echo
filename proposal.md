# PROJECT PROPOSAL: Echo Chamber in Social Media
This repository is created to document the progress on the class PIC 16B project on quantifying the echo chamber which arise in the social media

# Abstract
Echochamber is a situation where one only considers opinions that agree with their own. Such situations have been observed in multiple social platforms, especially in the context of politics where people only believed in the words of their own chosen political party. Here, building upon the models of polarity by Garimella et al., we investigate the formation of echochamber in social media, particularly in Twitter, using complex visualizations in Python. In addition we plan to reduce the bias of the datasets by considering a sentimental analysis to see whether a person tweets in a positive or negative way and to implement machine learning models to quantitatively separate each echo chamber aparts rigorously.

# Planned Deliverables
## Platform
For Full Success, we aim to build a webpage that informs the general public about the echo chamber by including our findings of the project, hosting on Jupyter notebook, and other literatures that points to the existence of the echo-chamber.

For Partial Success, we aim to compile a Jupyter notebook, hosting on the repository, consisting of our computations and findings.
## Full Success
We try to implement the following ideas in order:
1. While the results obtained by Garimella et al. provide a nice visualization of the users' polarity scores as a scatter plot which observed, by eye, two major clusters corresponding to the echo-chambers, it does not provide a rigorous means to actually *quantify* these clusters. Here, we aim to deploy machine learning models and other techniques in data science, such as k-means, spectral clustering, etc. on the **Full** dataset to create more complex visualizations that segregate each echo-chamber apart. Note that we expected to create our own model of polarity scores, but alternatively, we could use the polarity scores which the authors kindly provided for us as well. In addition, we will compare the clustering obtained via the polarity scores with the clustering algorithm on the Twitter's social network structures, i.e. Girvan-Newmann/Louvain, to see their dependency on each others.    
2. The author quantified each user's biasedness using quotes of certain domains, but what if there's a user who only quotes from a score-1 domain just to diss it? By the original method of computation, this would make me have leaningness close to 1, while in fact it should be close to 0. We wish to address this issue by cleaning the datasets and performing a sentimental analysis on each tweet to gather the *sentimental coefficients*. We expect to incorporate these coefficients to create new model of polarity calculation and improve the overall accuracy of the echochamber prediction. 
3. The dataset selected tweets that contain the corresponding hashtag for each topic during the month of June 2016. However, in our life experience, most people who don't have a strong political affiliation don't tweet with hashtag of the topic. In fact, most of the tweets about the topic we see on our timeline are subtle complaints/praises about the topic without the hashtag. From our assumption, people with no strong political affiliation are more influenced by the echo chamber (as they didn't start with a strong opinion on the topic, but the opinion gets strengthed by the content they see). Here, we intend to investigate how the polarity scores changes with respect to time. For example, we might consider how the echo-chamber *attracts* or *repels* each users away by considering the change in variance of the polarity score in each chamber. 
4. Build a webpage to deliver the original study and our findings to the general public. 

## Partial Success
1. In parallel to the first goal in the Full Success, we may not be able to fully utilize the **Full** dataset provided due to restriction in the computational power. In this case, we may resort to using only **Partial** dataset by sampling only parts of the whole dataset, either by naively truncating the dataset, sampling based on a small time-gap, or sampling based on ego randomization (pick a node, and follows its branching). In addition, we could still use the already-computed polarity scores in which the authors provided for us. We expected that we could still do a thorough machine learning-heavy analysis on clustering and study its dependency on the network structures using the two alternative methods we described: partial datasets or author-provided datasets.   
2. Notice that our main difficulty in the project lies on the cleaning for the twitter data provided by the authors. If necessary, we may predict the echo-chamber with the combination of author-provided followers data and parts of the twitter data by focusing on the intrinsic *Social Network Structure* using methods in Network Science, such as centrality measurement or community structure analysis. By mixing both the author-provided data and our analysis, we hope to provide meaningful findings even if we were not able to successfully come up with our own polarity scores calculations. 


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


