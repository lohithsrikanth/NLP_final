# Cuisine Compass: A Restaurant Recommendation System Utilizing Sentiment Analysis

### Packages used:

Our project makes use of the following packages:

- nltk
- spacy
- sklearn
- tensorflow
- numpy
- matplotlib
- transformers
- datasets
- wordcloud
- plotly
- streamlit
- textblob
- accelerate
- ipywidgets

Refer to the requirements.txt file for all the packages. This file was generated using the command:

```bash
pip freeze > requirements.txt
```

### Guidelines on running the project

All our backend code files are in the directory named "Code". In this directory, there is another directory named "preprocessing" which contains code that was used to preprocess the original data file. The preprocessed file named "Yelp_Restaurant_Reviews.csv" is the file that is used by all the models.

The original data file was retrieved from here: https://www.kaggle.com/datasets/farukalam/yelp-restaurant-reviews?resource=download

The 'Code' directory contains the following files:

- EDA.ipynb => This file does the Exploratory Data Analysis for our project.
- LogisticRegression_RandomForest.ipynb => This file contains code that uses the Logistic Regression and Random Forest models to do sentiment analysis.
- SVM2.ipynb => This file contains code that uses the Support Vector Machine to perform sentiment analysis.
- YelpNeuralNetwork.ipynb => This file contains code that uses Neural Networks to do sentiment analysis.
- Sentiment_analysis_using_transformers.ipynb => This file contains the code that uses the pretrained DistilBERT transformers model to perform sentiment analysis. This file also contains the implementation of the Recommendation system using the SentimentIntensityAnalyzer. Some portion of the code does the evaluation of the recommendation system with the transformers model. Finally, a restaurant.json file is created that the user interface can use to render the top rated restaurants, ratings, top reviews and must-try foods. In order to get the trained transformers model, follow this link: https://drive.google.com/file/d/1Y4mxZ7-hzlQi9OL1U0IbVYcaYBIJL85N/view?usp=sharing
- food_recommendations.pkl => This is a pickle file containing the must-try foods at each restaurant. This pickle file is used by the Sentiment_analysis_using_transformers.ipynb file.
- Yelp_Restaurant_Reviews.csv => This is the preprocessed data file which is subsequently used by all the models.
- restaurants.json => This file is used to render restaurants for the UI

#### User Interface

To run the UI, please navigate to the directory named 'UI' and run the command:

```bash
streamlit run app.py
```

Note: Ensure that the streamlit module has been installed (included in the requirements.txt file).
