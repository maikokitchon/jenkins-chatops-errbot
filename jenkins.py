from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests

class Jenkins(BotPlugin):
    """
    jenkins
    """
    _services = {
        'web': {
            'url': 'http://admin:1168c4dd9ddf99fc9de9eead120a675711@172.17.0.4:8080',
            'token': '8rEqg7vCBGvuFvgHQc7FjLfaaCa9CuuPMHzYCP',
            'job_url': 'http://127.0.0.1:8080/job/My%20Sample%20Project/'
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
        resp += f"| Jenkins Job Url | {Jenkins._services['web']['job_url']}\n"

        response = requests.post(f"{Jenkins._services['web']['url']}/job/My%20Sample%20Project/build?token={Jenkins._services['web']['token']}&cause=This+was+started+by+{frm.person}")
        
        return resp

    @botcmd
    def jenkins_show_logs(self, message, service=None):
        """This is just a sample plugin"""

        response = requests.get(f"{Jenkins._services['web']['url']}/job/My%20Sample%20Project/lastBuild/consoleText")
        
        return "```"+response.text