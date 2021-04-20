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
        # container = client.containers.run(Dos._services[service]['image'],
        #                                   detach=True,
        #                                   remove=True,
        #                                   ports=Dos._services[service]['ports'])
        # services = list(self['services'])
        # services.append({'id': container.id, 'name': service})
        # self['services'] = services
        # return Dos._services[service]['info']
        return "This is just a sample function"
    
    @botcmd
    def jenkins_build(self, message, service=None):
        """This is just a sample plugin"""

        response = requests.post('http://admin:1168c4dd9ddf99fc9de9eead120a675711@172.17.0.3:8080/job/My%20Sample%20Project/build?token=8rEqg7vCBGvuFvgHQc7FjLfaaCa9CuuPMHzYCP', headers=headers)
        print(response)
        return 'Triggered a job named My Sample Project with response '.response.text