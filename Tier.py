def tier_online(url):
    tier1_domains = [
        "www.theage.com.au", "www.heraldsun.com.au", "www.smh.com.au",
        "www.afr.com", "www.canberratimes.com.au", "www.news.com.au",
        # ... you can add other Tier 1 domains here ...
    ]

    tier2_domains = [
        "www.manninghamleader.com.au", "www.sunshinecoastdaily.com.au",
        # ... you can add other Tier 2 domains here ...
    ]

    if any(domain in url for domain in tier1_domains):
        return "tier1"
    elif any(domain in url for domain in tier2_domains):
        return "tier2"
    else:
        return "Not tier1 or tier2"

#def tier_print(url):