import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def infer_strengths_weaknesses(user_info):
    # Process psychometric test results to infer strengths and weaknesses
    strengths = []
    weaknesses = []
    
    # Example logic based on hypothetical test scores
    if user_info['verbal_score'] > 70:
        strengths.append('Verbal Reasoning')
    if user_info['quant_score'] < 50:
        weaknesses.append('Quantitative Reasoning')
    
    return strengths, weaknesses

def recommend_courses(user_info, learning_data):
    # Example recommendation logic using KMeans clustering on learning data
    features = ['score_math', 'score_programming', 'score_analytics']
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(learning_data[features])
    
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(scaled_data)
    
    user_cluster = kmeans.predict(scaler.transform([user_info[features]]))[0]
    recommended_courses = learning_data[learning_data['cluster'] == user_cluster]
    
    return recommended_courses['course_name'].tolist()
