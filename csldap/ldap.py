import ldap
import datetime as dt
from typing import Tuple
# Get below values for this from .env
username = "SELabManService"
password = "SomeServicePassword1!"

base = "OU=CS Users,DC=csd,DC=mtsu,DC=edu"

def isGroupMember(group_name,ldap_groups) -> bool:
  bgname = str.encode(group_name)
  for group in ldap_groups:
    if bgname in group:
      return True
  return False

# Provide the pipeline id and the actual system group name and receive
# a dictionary with {'isExpired':bool,'isMember':bool} for result.
def isAlreadyStillMember(pipeline_id,group_name) -> dict[str, bool]:
  criteria = "(&(objectCategory=person)(objectClass=user)(cn=%s))" % pipeline_id
  attributes = [
    'memberOf',
    'accountExpires'
  ]
  conn = ldap.initialize("ldap://csd.mtsu.edu")
  conn.set_option(ldap.OPT_REFERRALS,0)
  conn.set_option(ldap.OPT_SIZELIMIT,0)

  conn.simple_bind_s("{}@csd.mtsu.edu".format(username),password)

  result = conn.search_s(base,ldap.SCOPE_SUBTREE,criteria,attributes)
  if result == []:
    return {'isExpired':False,
            'isMember':False,
            'isValid':False}
            
  expires = int(result[0][1]['accountExpires'][0])/10000000
  expires = dt.datetime(1601,1,1) + dt.timedelta(seconds=expires)
  isExpired = dt.datetime.now() >= expires

  isMember = isGroupMember(group_name, result[0][1]['memberOf'])
      
  
  return {'isExpired':isExpired,
          'isMember':isMember,
          'isValid':True}
