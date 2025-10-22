from imdb import Cinemagoer
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_series_details(series_name):
    pass

series_name = "Breaking Bad"

# Initialize Cinemagoer instance
ia = Cinemagoer()

# Search for the series
series_search = ia.search_movie(series_name)
if not series_search:
    logger.error(f"No series found with the name '{series_name}'")
    exit

# Assuming the first result is the correct series
series = series_search[0]
ia.update(series, 'main')

# Print series details
logger.info(f"Title: {series.get('title')}")
logger.info(f"Year: {series.get('year')}")
logger.info(f"Plot: {series.get('plot outline')}")
logger.info(f"Genres: {', '.join(series.get('genres', []))}")
logger.info(f"Rating: {series.get('rating')}")

# Get full cast and crew
ia.update(series, 'full credits')

# Print directors
# directors = series.get('directors')
# if directors:
#     logger.info("Directors:")
#     for director in directors:
#         logger.info(f"  {director['name']}")

# Print actors
# actors = series.get('cast')
# if actors:
#     logger.info("Actors:")
#     for actor in actors[:10]:  # Limiting to first 10 actors for brevity
#         logger.info(f"  {actor['name']} as {actor.currentRole}")

# Update the series with the number of seasons available
ia.update(series, 'episodes')

# Get episodes for each season using update_series_seasons
if 'seasons' in series:
    seasons_num = series['seasons']
    logger.info(f"seasons_num:{seasons_num}")

"""
    >>> list(series.keys())
['title', 'year', 'imdbIndex', 'kind', 'cover url', 'original title', 'localized title', 'cast', 'genres', 'runtimes', 'countries', 'country codes', 'language codes', 'color info', 'aspect ratio', 'sound mix', 'certificates', 'number of seasons', 'rating', 'votes', 'imdbID', 'videos', 'plot outline', 'languages', 'series years', 'akas', 'seasons', 'writer', 'production companies', 'distributors', 'special effects', 'other companies', 'director', 'producer', 'composer', 'cinematographer', 'editor', 'casting director', 'production design', 'art direction', 'set decoration', 'costume designer', 'make up', 'production manager', 'assistant director', 'art department', 'sound crew', 'visual effects', 'stunt performer', 'camera and electrical department', 'casting department', 'costume department', 'editorial department', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous crew', 'thanks', 'number of episodes', 'canonical title', 'long imdb title', 'long imdb canonical title', 'smart canonical title', 'smart long imdb canonical title', 'full-size cover url']
>>> 
"""
for season in range(seasons_num):
    ia.update_series_seasons(series, season, override=1)
    episodes = series['episodes'].get(season, {})
    logger.info(f"\nSeason {season}:")
    for episode_num, episode in episodes.items():
        logger.info(f"  Episode {episode_num}: {episode['title']}")
        logger.info(f"    Air Date: {episode.get('original air date')}")
        logger.info(f"    Plot: {episode.get('plot outline')}")
        logger.info(f"    Rating: {episode.get('rating')}")

# Example usage
# get_series_details("Breaking Bad")
