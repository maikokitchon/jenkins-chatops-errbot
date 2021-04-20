from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests

class Jenkins(BotPlugin):
    """
    jenkins
    """
    _services = {
        'web': {'image': 'nginx:latest',
            'ports': {'80/tcp': '8090'},
            'info': 'Web created at http://localhost:8090'
        },
        'jenkins': {'image': 'jenkins:latest',
            'ports': {'8080/tcp': '8080', '5000/tcp': '5000'},
            'info': 'Jenkins created at http://localhost:8080'
        },
    }

    def activate(self):
        """
        Triggers on plugin activation
        """
        super(Jenkins, self).activate()
        self['services'] = []

    @botcmd
    def sampleonly(self, message, service=None):
        """This is just a sample plugin"""

        # container_id = self.get_container_id(service)
        # if container_id:
        #     return f'Service {service} already running'
        # container = client.containers.run(Jenkins._services[service]['image'],
        #                                   detach=True,
        #                                   remove=True,
        #                                   ports=Jenkins._services[service]['ports'])
        # services = list(self['services'])
        # services.append({'id': container.id, 'name': service})
        # self['services'] = services
        # return Jenkins._services[service]['info']
        return "This is just a sample function"
    
    @botcmd
    def jenkins_build(self, message, service=None):
        """This is just a sample plugin"""

        frm = message.frm
        
        resp = "| key      | value\n"
        resp += "| -------- | --------\n"
        resp += f"| Triggered By | `{frm.person}`\n"
        resp += f"| Triggered Jenkins Job Name | My Sample Project\n"
        resp += f"| Jenkins Job Url | http://127.0.0.1:8080/job/My%20Sample%20Project/\n"

        response = requests.post(f"http://admin:1168c4dd9ddf99fc9de9eead120a675711@172.17.0.3:8080/job/My%20Sample%20Project/build?token=8rEqg7vCBGvuFvgHQc7FjLfaaCa9CuuPMHzYCP&cause=This+was+started+by+{frm.person}")
        
        return resp

    @botcmd
    def jenkins_show_logs(self, message, service=None):
        """This is just a sample plugin"""

        response = requests.get(f"http://admin:1168c4dd9ddf99fc9de9eead120a675711@172.17.0.3:8080/job/My%20Sample%20Project/lastBuild/consoleText")
        
        return response.text