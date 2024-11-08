from flask import Flask, render_template, request
from utils import ArticleRecommendationFacade

# Initialize the facade with the provided paths
facade = ArticleRecommendationFacade('data/combined_articles_recommendations.csv', 'data/articles_big_dataset.csv')

app = Flask(__name__)

@app.route('/')
def home():
    # Use the facade to get the list of articles
    articles_list = facade.testset_articles_df[['uuid', 'title']].to_dict('records')
    return render_template('home.html', articles=articles_list)

@app.route('/article/<string:article_id>')
def article_recommendations(article_id):
    # Use the facade to get article details and recommendations
    result = facade.get_article(article_id)
    recommendations = facade.get_recommendations(article_id)
    return render_template('article.html', article=result, recommendations=recommendations)

@app.route('/recommendation/<string:article_id>/<string:recommendation_id>')
def recommendation(article_id, recommendation_id):
    # Use the facade to get article details and recommendations
    article = facade.get_article(article_id)
    recommendations = facade.get_recommendations(article_id)

    # Find the recommendation with the matching recommendation_id
    recommendation = next((rec for rec in recommendations if rec.uuid == recommendation_id), None)

    return render_template('recommendation.html', article=article, recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)