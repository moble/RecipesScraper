# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    package_data = {'project': [
        'sitemap/get_and_parse_sitemap.py',
        'sitemap/seed_lists/*.txt',
        'sitemap/xml/*.xml'
    ]},
    entry_points = {'scrapy': ['settings = RecipesScraper.settings']},
)
