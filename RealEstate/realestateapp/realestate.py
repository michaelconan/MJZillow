import zillow
import numpy as np

key = 'X1-ZWz1bb4e622vbf_7rj5m'
api = zillow.ValuationApi()

def get_zestimate(address, postal_code):
    
    # Zillow library search results (/deep)
    deep_results = api.GetDeepSearchResults(key, address, postal_code)

    return deep_results.zestimate.amount, deep_results.zpid

def get_comps(zpid):
    comp_data = api.GetDeepComps(key, zpid, 25)
    zest = np.mean([c.zestimate.amount for c in comp_data['comps'] if c.zestimate.amount])
    beds = np.mean([c.extended_data.bedrooms for c in comp_data['comps'] if c.extended_data.bedrooms])
    return zest, beds