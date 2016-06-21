from django.shortcuts import render

import urllib3
import json
from patato.models import Movie, Gene, MovieGene


def query_movie(request):
    q = ''
    movies = []
    if request.method == 'POST':
        q = request.POST['q']
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://api.douban.com/v2/movie/search', fields={"q": q})
        if r.status == 200:
            s = str(r.data.decode('utf-8'))
            data_list = json.loads(s)
            subjects = data_list['subjects']
            if subjects:
                for subject in subjects:
                    m_title = subject['title']
                    m_original_title = subject['original_title']
                    m_id = subject['id']
                    m_alt = subject['alt']
                    m_year = subject['year']
                    m_genres = subject['genres']
                    m = Movie(name=m_title, douban=m_id, year=m_year)
                    m.save()
                    if m_genres:
                        for gene_name in m_genres:
                            try:
                                gene = Gene.objects.get(name=gene_name)
                            except:
                                gene = Gene(name=gene_name)
                                gene.save()
                            mg = MovieGene(movie=m, gene=gene)
                            mg.save()
                    movies.append({m_id: m_title})
    else:
        pass

    context = {'q': q, 'movies': movies}
    return render(request, 'patato/query_movie.html', context)
