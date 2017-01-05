import scholar

#using Christian Kreibich google scholar parser called scholar.py, ty Christian!
def setup(citationformat, keywords,maxpage):
    querier = scholar.ScholarQuerier()
    settings = scholar.ScholarSettings()
    query = scholar.SearchScholarQuery()
    settings.set_citation_format(citationformat)
    querier.apply_settings(settings)
    query.set_words_some(keywords)
    query.set_num_page_results(maxpage)
    querier.send_query(query)
    results = open('results', 'w')
    for art in querier.articles:
        results.write(art.attrs["title"][0]+"\n")
    results.close()
    return querier.articles
    
def build_comparison_2d_array(list_names):
    map = [[0 for x in range(len(list_names))] for y in range(len(list_names))] 
    return map
def build_citation_map(list_articles):
    citationmap = {}
    for art in list_articles:
        citationmap[art.attrs["title"][0]] = art.attrs["url_citations"][0]
        print(art.attrs["title"][0] + " : " + art.attrs["url_citations"][0])
def print_2d_array(map):
    for row in map:
        for item in row:
            print(item,end="")
        print("\n")
def print_map(map):
    for key in map.keys():
        print(key +" : " + map[key])

articles = setup(scholar.ScholarSettings.CITFORM_BIBTEX, "physics",10)
map = build_citation_map(articles)
#print_map(map)



