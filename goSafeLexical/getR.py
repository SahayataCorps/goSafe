import dns.resolver

answers = dns.resolver.query('pornhub.net', 'NS')
for rdata in answers:
    print(rdata)
"""
for rdata in answers:
    print ('Host', rdata.exchange, 'has preference', rdata.preference)"""