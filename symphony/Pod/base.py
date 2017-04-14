'''
    Purpose:
        pod endpoint basic methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


def sessioninfo(self):
    ''' list apps '''
    req_hook = 'pod/v1/sessioninfo'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return status_code, response
