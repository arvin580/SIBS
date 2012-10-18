import mechanize


br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0')]
br.set_handle_robots(False)


def nature(url):
    br.open(url)
    rsp = br.follow_link(text_regex=r'.*PDF.*')
    pdf = rsp.geturl()
    filename = rsp.geturl().split('/')[-1]
    br.retrieve(pdf, filename)


def science(url):
    br.open(url)
    rsp = br.follow_link(text_regex=r'.*PDF.*')
    pdf = rsp.geturl()
    filename = rsp.geturl().split('/')[-1]
    br.retrieve(pdf, filename)


def cell(url):
    br.open(url)
    rsp = br.follow_link(text_regex=r'Switch to Standard View')
    br.open(rsp.geturl())
    rsp = br.follow_link(text_regex=r'.*PDF.*')
    pdf = rsp.geturl() + '?intermediate=true'
    filename = rsp.geturl().split('/')[-1]
    br.retrieve(pdf, filename)

def pubmed(PMID='', url=''):
    if PMID:
        br.open('http://www.ncbi.nlm.nih.gov/pubmed?term='+str(PMID))
        for lk in br.links():
            print(lk)



#science('http://www.sciencemag.org/content/337/6100/1333')
#nature('http://www.nature.com/nrg/journal/v13/n4/full/nrg3199.html')
#nature('http://www.nature.com/nature/journal/v400/n6745/full/400687a0.html')
#cell('http://www.cell.com/abstract/S0092-8674(12)00889-6')
pubmed(19275120)

