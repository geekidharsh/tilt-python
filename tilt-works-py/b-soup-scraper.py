from bs4 import BeautifulSoup as bsoup
from urllib2 import urlopen
import requests as rq
import re

urls = ["http://www.merckmillipore.com/INTL/en/product/HBSS-with-Phenol-Red,EMD_BIO-L"]
# "http://www.emdmillipore.com/US/en/product/Alcian-Blue%2CEMD_CHEM-109",
# "http://www.emdmillipore.com/US/en/product/Aniline-Blue-W.S.%2CEMD_CHEM-128",
# "http://www.emdmillipore.com/US/en/product/Biebrich-Scarlette%2CEMD_CHEM-148",
# "http://www.emdmillipore.com/US/en/product/Brilliant-Green%2CEMD_CHEM-162",
# "http://www.emdmillipore.com/US/en/product/Cresyl-Blue-Brilliant%2CEMD_CHEM-163",
# "http://www.emdmillipore.com/US/en/product/Carmine-Aluminum-Lake%2CEMD_CHEM-168",
# "http://www.emdmillipore.com/US/en/product/Congo-Red%2CEMD_CHEM-186",
# "http://www.emdmillipore.com/US/en/product/Cresyl-Violet%2CEMD_CHEM-190",
# "http://www.emdmillipore.com/US/en/product/Crystal-Violet%2CEMD_CHEM-192",
# "http://www.emdmillipore.com/US/en/product/Eosin-Y-Powder%2CEMD_CHEM-200",
# "http://www.emdmillipore.com/US/en/product/Fast-Green%2CEMD_CHEM-210",
# "http://www.emdmillipore.com/US/en/product/Fuchsin-Acid%2CEMD_CHEM-218",
# "http://www.emdmillipore.com/US/en/product/Fuchsin-Basic%2CEMD_CHEM-220"]
for page in urls:
    sauce = urlopen(page).read()
    soup = bsoup(sauce, 'lxml')
    print soup

