
import CloudFlare
import dns.resolver

class SaasDomainManager:
  def __init__(self, zone_id, auth_token):
    self.cf = CloudFlare.CloudFlare(token=auth_token)
    self.zone_id = zone_id


  def create(self, hostname):
    payload = {
      "hostname": hostname,
      "ssl":{
        "type":"dv",
        "method": "http",
        "settings": {
            'min_tls_version': '1.3'
        },
        "wildcard": False,
      }
    }
    if not self.exists(hostname) and self.check_cname(hostname):
      self.cf.zones.custom_hostnames.post(self.zone_id, data=payload)

  def exists(self, hostname):
      hosts = self.cf.zones.custom_hostnames.get(self.zone_id, params={'hostname':hostname})
      return hosts
      
  def delete(self, hostname):
    host = self.exists(hostname)
    if host:
      self.cf.zones.custom_hostnames.delete(self.zone_id, host[0]['id'])

  def check_cname(self, hostname):
    try:
      resolver = dns.resolver.Resolver()
      answers = resolver.query(hostname, "CNAME")

      if len(list(answers)):
        print('check CNAME:', str(answers[0].target)[:-1])
        return  str(answers[0].target)[:-1]
    except:
      return ''