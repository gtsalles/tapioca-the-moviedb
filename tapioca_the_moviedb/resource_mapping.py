# coding: utf-8
# flake8: noqa

RESOURCE_MAPPING = {
    'discover_movie': {
        'resource': 'discover/movie',
        'docs': 'https://developers.themoviedb.org/3/discover/movie-discover'
    },
    'discover_tv': {
        'resource': 'discover/tv',
        'docs': 'https://developers.themoviedb.org/3/discover/tv-discover'
    },
    'genre_movie': {
        'resource': 'genre/movie/list',
        'docs': 'https://developers.themoviedb.org/3/genres/get-movie-list'
    },
    'genre_tv': {
        'resource': 'genre/tv/list',
        'docs': 'https://developers.themoviedb.org/3/genres/get-tv-list'
    },
    'movie': {
        'resource': 'movie/{movie_id}',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-details'
    },
    'movie_account_states': {
        'resource': 'movie/{movie_id}/account_states',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-account-states'
    },
    'movie_alternative_titles': {
        'resource': 'movie/{movie_id}/alternative_titles',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-alternative-titles'
    },
    'movie_changes': {
        'resource': 'movie/{movie_id}/changes',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-changes'
    },
    'movie_credits': {
        'resource': 'movie/{movie_id}/credits',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-credits'
    },
    'movie_external_ids': {
        'resource': 'movie/{movie_id}/external_ids',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-external-ids'
    },
    'movie_images': {
        'resource': 'movie/{movie_id}/images',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-images'
    },
    'movie_keywords': {
        'resource': 'movie/{movie_id}/keywords',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-keywords'
    },
    'movie_release_dates': {
        'resource': 'movie/{movie_id}/release_dates',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-release-dates'
    },
    'movie_videos': {
        'resource': 'movie/{movie_id}/videos',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-videos'
    },
    'movie_translations': {
        'resource': 'movie/{movie_id}/translations',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-translations'
    },
    'movie_recommendations': {
        'resource': 'movie/{movie_id}/recommendations',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-recommendations'
    },
    'movie_similar': {
        'resource': 'movie/{movie_id}/similar',
        'docs': 'https://developers.themoviedb.org/3/movies/get-similar-movies'
    },
    'movie_reviews': {
        'resource': 'movie/{movie_id}/reviews',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-reviews'
    },
    'movie_lists': {
        'resource': 'movie/{movie_id}/lists',
        'docs': 'https://developers.themoviedb.org/3/movies/get-movie-lists'
    },
    'movie_rating': {
        'resource': 'movie/{movie_id}/rating',
        'docs': 'https://developers.themoviedb.org/3/movies/rate-movie'
    },
    'movie_latest': {
        'resource': 'movie/latest',
        'docs': 'https://developers.themoviedb.org/3/movies/get-latest-movie'
    },
    'movie_now_playing': {
        'resource': 'movie/now_playing',
        'docs': 'https://developers.themoviedb.org/3/movies/get-now-playing'
    },
    'movie_popular': {
        'resource': 'movie/popular',
        'docs': 'https://developers.themoviedb.org/3/movies/get-popular-movies'
    },
    'movie_top_rated': {
        'resource': 'movie/top_rated',
        'docs': 'https://developers.themoviedb.org/3/movies/get-top-rated-movies'
    },
    'movie_upcoming': {
        'resource': 'movie/upcoming',
        'docs': 'https://developers.themoviedb.org/3/movies/get-upcoming'
    },
    'search_companies': {
        'resource': 'search/company',
        'docs': 'https://developers.themoviedb.org/3/search/search-companies'
    },
    'search_collection': {
        'resource': 'search/collection',
        'docs': 'https://developers.themoviedb.org/3/search/search-collections'
    },
    'search_keywords': {
        'resource': 'search/keyword',
        'docs': 'https://developers.themoviedb.org/3/search/search-keywords'
    },
    'search_movie': {
        'resource': 'search/movie',
        'docs': 'https://developers.themoviedb.org/3/search/search-movies'
    },
    'search_multi': {
        'resource': 'search/multi',
        'docs': 'https://developers.themoviedb.org/3/search/multi-search'
    },
    'search': {
        'resource': 'search/multi',
        'docs': 'https://developers.themoviedb.org/3/search/multi-search'
    },
    'search_person': {
        'resource': 'search/person',
        'docs': 'https://developers.themoviedb.org/3/search/search-people'
    },
    'search_tv': {
        'resource': 'search/tv',
        'docs': 'https://developers.themoviedb.org/3/search/search-tv-shows'
    },
    'tv': {
        'resource': 'tv/{tv_id}',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-details'
    },
    'tv_account_states': {
        'resource': 'tv/{tv_id}/account_states',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-account-states'
    },
    'tv_alternative_titles': {
        'resource': 'tv/{tv_id}/alternative_titles',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-alternative-titles'
    },
    'tv_changes': {
        'resource': 'tv/{tv_id}/changes',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-changes'
    },
    'tv_content_ratings': {
        'resource': 'tv/{tv_id}/content_ratings',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-content-ratings'
    },
    'tv_credits': {
        'resource': 'tv/{tv_id}/credits',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-credits'
    },
    'tv_episode_groups': {
        'resource': 'tv/{tv_id}/episode_groups',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-episode-groups'
    },
    'tv_external_ids': {
        'resource': 'tv/{tv_id}/external_ids',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-external-ids'
    },
    'tv_images': {
        'resource': 'tv/{tv_id}/images',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-images'
    },
    'tv_keywords': {
        'resource': 'tv/{tv_id}/keywords',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-keywords'
    },
    'tv_recommendations': {
        'resource': 'tv/{tv_id}/recommendations',
        'docs': 'https://developers.themoviedb.org/3/tvs/get-tv-recommendations'
    },
    'tv_reviews': {
        'resource': 'tv/{tv_id}/reviews',
        'docs': 'https://developers.themoviedb.org/3/tvs/get-tv-reviews'
    },
    'tv_screened_theatrically': {
        'resource': 'tv/{tv_id}/screened_theatrically',
        'docs': 'https://developers.themoviedb.org/3/tv/get-screened-theatrically'
    },
    'tv_similar': {
        'resource': 'tv/{tv_id}/similar',
        'docs': 'https://developers.themoviedb.org/3/tv/get-similar-tv-shows'
    },
    'tv_translations': {
        'resource': 'tv/{tv_id}/translations',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-translations'
    },
    'tv_videos': {
        'resource': 'tv/{tv_id}/videos',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-videos'
    },
    'tv_rating': {
        'resource': 'tv/{tv_id}/rating',
        'docs': 'https://developers.themoviedb.org/3/tv/rate-tv-show'
    },
    'tv_latest': {
        'resource': 'tv/latest',
        'docs': 'https://developers.themoviedb.org/3/tv/get-latest-tv'
    },
    'tv_airing_today': {
        'resource': 'tv/airing_today',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-airing-today'
    },
    'tv_on_the_air': {
        'resource': 'tv/on_the_air',
        'docs': 'https://developers.themoviedb.org/3/tv/get-tv-on-the-air'
    },
    'tv_popular': {
        'resource': 'tv/popular',
        'docs': 'https://developers.themoviedb.org/3/tv/get-popular-tv-shows'
    },
    'tv_top_rated': {
        'resource': 'tv/top_rated',
        'docs': 'https://developers.themoviedb.org/3/tv/get-top-rated-tv'
    },
    'tv_seasons': {
        'resource': 'tv/{tv_id}/season/{season_number}',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-details'
    },
    'tv_season_changes': {
        'resource': 'tv/season/{season_id}/changes',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-changes'
    },
    'tv_season_account_states': {
        'resource': 'tv/{tv_id}/season/{season_number}/account_states',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-account-states'
    },
    'tv_season_credits': {
        'resource': 'tv/{tv_id}/season/{season_number}/credits',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-credits'
    },
    'tv_season_external_ids': {
        'resource': 'tv/{tv_id}/season/{season_number}/external_ids',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-external-ids'
    },
    'tv_season_images': {
        'resource': 'tv/{tv_id}/season/{season_number}/images',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-images'
    },
    'tv_season_videos': {
        'resource': 'tv/{tv_id}/season/{season_number}/videos',
        'docs': 'https://developers.themoviedb.org/3/tv-seasons/get-tv-season-videos'
    },
}
