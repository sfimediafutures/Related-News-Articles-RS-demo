from flask import Flask, render_template, request
from utils import ArticleRecommendationFacade

# Initialize the facade with the provided paths
facade = ArticleRecommendationFacade('data/test_set_articles.csv', 'data/recommendations.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    # Use the facade to get the list of articles
    articles_list = facade.articles_df[['uuid', 'title']].to_dict('records')
    return render_template('home.html', articles=articles_list)

@app.route('/article/<string:article_id>')
def article_recommendations(article_id):
    # Use the facade to get article details and recommendations
    result = facade.get_article_with_recommendations(article_id)
    return render_template('article.html', article=result['article'], recommendations=result['recommendations'])

if __name__ == "__main__":
    app.run(debug=True)