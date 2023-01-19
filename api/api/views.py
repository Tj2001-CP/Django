from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests

class CountryInfoView(views.APIView):
    def get(self, request, country_name):
        url = f'https://en.wikipedia.org/wiki/{country_name}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        flag_link = soup.select_one('td > a > img')['src']
        capital = soup.select_one('td > a[title*="capital"]')
        if capital:
            capital = capital.get_text()
        largest_city = soup.select_one('td > a[title*="largest city"]')
        if largest_city:
            largest_city = largest_city.get_text()
        official_languages = soup.select_one('td > a[title*="official languages"]')
        if official_languages:
            official_languages = official_languages.get_text()
        area_total = soup.select_one('td > a[title*="area"]')
        if area_total:
            area_total = area_total.get_text()
        population = soup.select_one('td > a[title*="population"]')
        if population:
            population = population.get_text()
        GDP_nominal = soup.select_one('td > a[title*="GDP"]')
        if GDP_nominal:
            GDP_nominal = GDP_nominal.get_text()

        data = {
            'flag_link': flag_link,
            'capital': capital,
            'largest_city': largest_city,
            'official_languages': official_languages,
            'area_total': area_total,
            'population': population,
            'GDP_nominal': GDP_nominal,
        }

        return Response(data)
