import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    citation = []
    for par in results:
        try:
            all_para = par.find_all(
                'span', string=lambda text: 'citation' in text.lower())
            if all_para:
                for i in range(len(all_para)):
                    citation.append(all_para[i])
        except Exception as e:
            continue
    return len(citation)


def get_citations_needed_report(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    p_tags = []
    lines = []

    resultsss = results.find_all('p')
    for i in resultsss:
        try:
            para = i.find_all(
                'span', string=lambda text: 'citation' in text.lower())
            if para:
                for j in range(len(para)):

                    #  paragraph
                    p_tags.append(i.text)
                    # line
                    position = i.text.index('citation')
                    line = i.text[:position-1].split(". ")
                    lines.append(line[-1])

        except Exception as e:
            continue

    output = ''
    for p in range(len(p_tags)):
        output += f'cita Num: {p+1} \n'
        output += f'{p_tags[p]} \n'
        output += f'So , we need citation after the below line: \n'
        output += f'{lines[p]} \n'

    f = open("citation.txt", "w")
    f.write(output)
    f.close()
    return output
