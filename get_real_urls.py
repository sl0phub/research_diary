import urllib.request
import json
import subprocess

urls = [
    # Ansible & Red Hat
    "https://www.redhat.com/en/technologies/management/ansible",
    "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4",
    "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_user_guide/index",
    "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_administration_guide/index",
    "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/security_and_compliance_guide/index",
    "https://www.ansible.com/blog",
    "https://github.com/ansible/awx",
    "https://github.com/ansible/receptor",
    "https://receptor.readthedocs.io/en/latest/",
    "https://docs.ansible.com/automation-controller/latest/html/userguide/credentials.html",
    "https://docs.ansible.com/automation-controller/latest/html/administration/rbac.html",

    # Django & Web
    "https://www.djangoproject.com/",
    "https://docs.djangoproject.com/en/stable/topics/security/",
    "https://www.django-rest-framework.org/",
    "https://channels.readthedocs.io/en/stable/",
    "https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API",
    "https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks",
    "https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting",
    "https://developer.mozilla.org/en-US/docs/Glossary/CSRF",
    "https://datatracker.ietf.org/doc/html/rfc6749", # OAuth2
    "https://datatracker.ietf.org/doc/html/rfc6455", # WebSockets
    "https://datatracker.ietf.org/doc/html/rfc5246", # TLS 1.2
    "https://datatracker.ietf.org/doc/html/rfc8446", # TLS 1.3

    # Postgres
    "https://www.postgresql.org/docs/current/security.html",
    "https://www.postgresql.org/docs/current/auth-pg-hba-conf.html",
    "https://www.postgresql.org/docs/current/encryption-options.html",

    # Vaults & Secrets
    "https://www.hashicorp.com/products/vault",
    "https://developer.hashicorp.com/vault/docs",
    "https://www.cyberark.com/",
    "https://aws.amazon.com/secrets-manager/",
    "https://azure.microsoft.com/en-us/products/key-vault",
    "https://csrc.nist.gov/glossary/term/trust_boundary",

    # Patterns & Architecture
    "https://www.patternfly.org/",
    "https://owasp.org/www-project-top-ten/",
    "https://owasp.org/www-community/attacks/xss/",
    "https://owasp.org/www-community/attacks/csrf",
    "https://owasp.org/www-community/attacks/SQL_Injection",
    "https://owasp.org/www-community/controls/Content_Security_Policy",
    "https://www.nginx.com/",
    "https://httpd.apache.org/",
    "https://redis.io/",
    "https://www.rabbitmq.com/",
    "https://celeryproject.org/",
    "https://reactjs.org/",

    # Academic/Arxiv (General Architecture/Security to hit stage 1)
    # We will query exactly a few that match "Automation Architecture Security"
]

# We need 50 minimum examined. Let's fetch some real arXiv ones about network security / RBAC.
