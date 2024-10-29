import pandas as pd
import pickle

class Article:
    def __init__(self, 
        self.uuid = uuid
        self.title = title
        self.lead_text = lead_text
        self.content = content
        self.related = related

class ArticleRecommendationFacade:
    def __init__(self, articles_path: str, recommendations_path: str):
        # Load articles data
        self.articles_df = pd.read_csv(articles_path)
        # Load recommendations data
        with open(recommendations_path, 'rb') as f:
            self.recommendations = pickle.load(f)

        # Optional caches for efficiency
        self.article_cache = {}
        self.recommendation_cache = {}

    def get_article(self, article_id: str) -> dict:
        """Retrieve article details by ID."""
        # Check cache first
        if article_id in self.article_cache:
            return self.article_cache[article_id]

        # Search for article in the DataFrame
        article_row = self.articles_df[self.articles_df['uuid'] == article_id]
        if not article_row.empty:
            article_data = article_row.iloc[0].to_dict()
            self.article_cache[article_id] = article_data  # Cache for future access
            return article_data
        else:
            return {}  # Return empty if not found

    def get_recommendations(self, article_id: str) -> list:
        """Retrieve recommendations for a given article ID."""
        # Check cache first
        if article_id in self.recommendation_cache:
            return self.recommendation_cache[article_id]

        # Find the recommendation dictionary for the article ID
        recommendation_dict = self._find_recommendation_dict(article_id)
        if recommendation_dict:
            recommended_articles = recommendation_dict.get('recommendations', [])
            self.recommendation_cache[article_id] = recommended_articles  # Cache
            return recommended_articles
        else:
            return []  # Return empty if no recommendations found

    def get_article_with_recommendations(self, article_id: str) -> dict:
        """Retrieve both article details and recommendations for the article ID."""
        article_data = self.get_article(article_id)
        recommendations = self.get_recommendations(article_id)

        # Combine data into a single dictionary
        return {
            "article": article_data,
            "recommendations": recommendations
        }

    def _find_recommendation_dict(self, article_id: str) -> dict:
        """Find the recommendation dictionary for a specific article ID."""
        for recommendation in self.recommendations:
            if recommendation.get('article id') == article_id:
                return recommendation
        return {}