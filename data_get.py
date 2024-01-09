import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import classification_report

nltk.download('stopwords')
#######################################################################################################################################

messages2=pd.read_csv('spam_ham_dataset.csv')
messages=messages2[['label','text']]
lemmatizer=WordNetLemmatizer()

corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['text'][i])
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

#######################################################################################################################################

cv = CountVectorizer(max_features=99999999)
X = cv.fit_transform(corpus).toarray()

y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values

#######################################################################################################################################

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


spam_detect_model = MultinomialNB().fit(X_train, y_train)
y_pred=spam_detect_model.predict(X_test)

#######################################################################################################################################

score=accuracy_score(y_test,y_pred)
print(score)
print(classification_report(y_pred,y_test))

#######################################################################################################################################

def func_for_api(input_text):
    input_features = cv.transform(input_text)
    input_features = input_features.toarray()  
    input_features_2d = input_features.reshape(1, -1)


    predictions = spam_detect_model.predict(input_features_2d)
    # print(predictions)


    if predictions[0] == False:
        decision="HAM"
        return decision

    else:
        decision="SPAM"
        return decision
