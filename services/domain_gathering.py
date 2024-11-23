from dns import resolver as dns_resolver
import whois

class DomainGathering:

    def __init__(self):
        self.records_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        self.resolver = dns_resolver.Resolver()

    def get_details(self, domain):
        """Get IP geolocation."""
        return {
            "dns_info": self.get_dns_info(domain),
            "whois_info": self.map_whois_info(whois.whois(domain))
        }

    def get_dns_info(self, domain):
        """Get DNS information."""
        dns_info = {}
        for record_type in self.records_types:
            try:
                result = self.resolver.resolve(domain, record_type)
                for record in result:
                    dns_info[record_type] = record.to_text()
            except dns_resolver.NoAnswer:
                continue
        return dns_info

    def map_whois_info(self, whois_info):
        """Map Whois information."""
        if not whois_info:
            return {}
        return {
            "Domain Name": whois_info['domain_name'],
            "Register": whois_info['registrar'],
            "Whois Server": whois_info['whois_server'],
            "Creation Date": whois_info['creation_date'],
            "Expiration Date": whois_info['expiration_date'],
            "Updated Date": ", ".join(date.strftime("%d/%m/%Y %H:%M") for date in whois_info['updated_date']),
            "Nameservers": ", ".join(whois_info['name_servers']),
            "Emails": ", ".join(whois_info['emails']) if type(whois_info['emails']) == list else whois_info['emails'],
        }
