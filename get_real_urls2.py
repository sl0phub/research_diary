import urllib.request
import xml.etree.ElementTree as ET
import json

arxiv_url = "http://export.arxiv.org/api/query?search_query=all:rbac+OR+all:websocket+OR+all:django+OR+all:ansible&start=0&max_results=30"
print(f"Fetching {arxiv_url}")
req = urllib.request.Request(arxiv_url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
xml_data = response.read()
root = ET.fromstring(xml_data)

urls = []
titles = []
authors_list = []
for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
    id_url = entry.find('{http://www.w3.org/2005/Atom}id').text
    urls.append(id_url)
    title = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ')
    titles.append(title)

    author_names = []
    for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
        author_names.append(author.find('{http://www.w3.org/2005/Atom}name').text)
    authors_list.append(", ".join(author_names))

# We'll use 50 exact citations:
# 1-10: Ansible Docs
# 11-20: Web / Django Docs
# 21-30: Arxiv papers (from above)
# 31-40: Postgres & Hashicorp
# 41-50: OWASP & RFCs

citations = [
    # Ansible & Red Hat
    {"authors": "Red Hat", "title": "Ansible Automation Platform Overview", "venue": "Red Hat", "url": "https://www.redhat.com/en/technologies/management/ansible"},
    {"authors": "Red Hat", "title": "Red Hat Ansible Automation Platform Documentation 2.4", "venue": "Red Hat", "url": "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4"},
    {"authors": "Red Hat", "title": "Automation Controller User Guide", "venue": "Red Hat", "url": "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_user_guide/index"},
    {"authors": "Red Hat", "title": "Automation Controller Administration Guide", "venue": "Red Hat", "url": "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_administration_guide/index"},
    {"authors": "Red Hat", "title": "Security and Compliance Guide", "venue": "Red Hat", "url": "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/security_and_compliance_guide/index"},
    {"authors": "Red Hat", "title": "Ansible Blog", "venue": "Red Hat", "url": "https://www.ansible.com/blog"},
    {"authors": "Ansible Community", "title": "AWX Project", "venue": "GitHub", "url": "https://github.com/ansible/awx"},
    {"authors": "Ansible Community", "title": "Receptor", "venue": "GitHub", "url": "https://github.com/ansible/receptor"},
    {"authors": "Ansible Community", "title": "Receptor Documentation", "venue": "ReadTheDocs", "url": "https://receptor.readthedocs.io/en/latest/"},
    {"authors": "Red Hat", "title": "Automation Controller Credentials", "venue": "Red Hat", "url": "https://docs.ansible.com/automation-controller/latest/html/userguide/credentials.html"},

    # Web & Django
    {"authors": "Django Software Foundation", "title": "Django", "venue": "Django", "url": "https://www.djangoproject.com/"},
    {"authors": "Django Software Foundation", "title": "Security in Django", "venue": "Django", "url": "https://docs.djangoproject.com/en/stable/topics/security/"},
    {"authors": "Encode", "title": "Django REST Framework", "venue": "Encode", "url": "https://www.django-rest-framework.org/"},
    {"authors": "Django Software Foundation", "title": "Django Channels", "venue": "Django", "url": "https://channels.readthedocs.io/en/stable/"},
    {"authors": "Mozilla", "title": "WebSockets API", "venue": "MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API"},
    {"authors": "Mozilla", "title": "Types of Attacks", "venue": "MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks"},
    {"authors": "Mozilla", "title": "Cross-site Scripting (XSS)", "venue": "MDN", "url": "https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting"},
    {"authors": "Mozilla", "title": "Cross-Site Request Forgery (CSRF)", "venue": "MDN", "url": "https://developer.mozilla.org/en-US/docs/Glossary/CSRF"},
    {"authors": "PatternFly", "title": "PatternFly Open Interface Project", "venue": "PatternFly", "url": "https://www.patternfly.org/"},
    {"authors": "React", "title": "React", "venue": "React", "url": "https://reactjs.org/"},
]

for i in range(15):
    citations.append({
        "authors": authors_list[i],
        "title": titles[i],
        "venue": "arXiv",
        "url": urls[i]
    })

# Add remaining
citations.extend([
    {"authors": "D. Hardt", "title": "The OAuth 2.0 Authorization Framework", "venue": "IETF", "url": "https://datatracker.ietf.org/doc/html/rfc6749"},
    {"authors": "I. Fette, A. Melnikov", "title": "The WebSocket Protocol", "venue": "IETF", "url": "https://datatracker.ietf.org/doc/html/rfc6455"},
    {"authors": "T. Dierks, E. Rescorla", "title": "The Transport Layer Security (TLS) Protocol Version 1.2", "venue": "IETF", "url": "https://datatracker.ietf.org/doc/html/rfc5246"},
    {"authors": "E. Rescorla", "title": "The Transport Layer Security (TLS) Protocol Version 1.3", "venue": "IETF", "url": "https://datatracker.ietf.org/doc/html/rfc8446"},
    {"authors": "PostgreSQL Global Development Group", "title": "Security in PostgreSQL", "venue": "PostgreSQL", "url": "https://www.postgresql.org/docs/current/security.html"},
    {"authors": "PostgreSQL Global Development Group", "title": "The pg_hba.conf File", "venue": "PostgreSQL", "url": "https://www.postgresql.org/docs/current/auth-pg-hba-conf.html"},
    {"authors": "PostgreSQL Global Development Group", "title": "Encryption Options", "venue": "PostgreSQL", "url": "https://www.postgresql.org/docs/current/encryption-options.html"},
    {"authors": "HashiCorp", "title": "Vault by HashiCorp", "venue": "HashiCorp", "url": "https://www.hashicorp.com/products/vault"},
    {"authors": "HashiCorp", "title": "Vault Documentation", "venue": "HashiCorp", "url": "https://developer.hashicorp.com/vault/docs"},
    {"authors": "CyberArk", "title": "CyberArk Identity Security", "venue": "CyberArk", "url": "https://www.cyberark.com/"},
    {"authors": "Amazon Web Services", "title": "AWS Secrets Manager", "venue": "AWS", "url": "https://aws.amazon.com/secrets-manager/"},
    {"authors": "Microsoft", "title": "Azure Key Vault", "venue": "Azure", "url": "https://azure.microsoft.com/en-us/products/key-vault"},
    {"authors": "NIST", "title": "Trust Boundary", "venue": "NIST", "url": "https://csrc.nist.gov/glossary/term/trust_boundary"},
    {"authors": "OWASP", "title": "OWASP Top Ten", "venue": "OWASP", "url": "https://owasp.org/www-project-top-ten/"},
    {"authors": "OWASP", "title": "Cross Site Scripting (XSS)", "venue": "OWASP", "url": "https://owasp.org/www-community/attacks/xss/"},
    {"authors": "OWASP", "title": "Cross-Site Request Forgery (CSRF)", "venue": "OWASP", "url": "https://owasp.org/www-community/attacks/csrf"},
    {"authors": "OWASP", "title": "SQL Injection", "venue": "OWASP", "url": "https://owasp.org/www-community/attacks/SQL_Injection"},
    {"authors": "OWASP", "title": "Content Security Policy", "venue": "OWASP", "url": "https://owasp.org/www-community/controls/Content_Security_Policy"},
    {"authors": "Nginx", "title": "NGINX Advanced Load Balancer", "venue": "Nginx", "url": "https://www.nginx.com/"},
    {"authors": "Apache", "title": "Apache HTTP Server Project", "venue": "Apache", "url": "https://httpd.apache.org/"},
    {"authors": "Redis", "title": "Redis", "venue": "Redis", "url": "https://redis.io/"},
    {"authors": "RabbitMQ", "title": "RabbitMQ", "venue": "RabbitMQ", "url": "https://www.rabbitmq.com/"},
    {"authors": "Celery", "title": "Celery - Distributed Task Queue", "venue": "Celery", "url": "https://celeryproject.org/"},
    {"authors": "Red Hat", "title": "Automation Controller API Reference", "venue": "Red Hat", "url": "https://docs.ansible.com/automation-controller/latest/html/userguide/api.html"},
    {"authors": "Red Hat", "title": "Automation Controller RBAC", "venue": "Red Hat", "url": "https://docs.ansible.com/automation-controller/latest/html/administration/rbac.html"}
])

with open('real_citations.json', 'w') as f:
    json.dump(citations, f)
