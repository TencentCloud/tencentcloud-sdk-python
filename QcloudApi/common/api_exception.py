# -*- coding: utf-8 -*-


class ApiExceptionBase(Exception):
    """
    @type message: string
    @param message: error describe
    """
    def __init__(self, message):
        self.message = message

    def get_info(self):
        return 'Error Message: %s\n' % (self.message)

    def __str__(self):
        return "ApiExceptionBase  %s" % (self.get_info())


class ApiClientParamException(ApiExceptionBase):
    def __init__(self, message):
        ApiExceptionBase.__init__(self, message)

    def __str__(self):
        return "ApiClientException  %s" % (self.get_info())


class ApiClientNetworkException(ApiExceptionBase):
    """ @note: client network exception
    """
    def __init__(self, message):
        ApiExceptionBase.__init__(self, message)

    def __str__(self):
        return "ApiClientNetworkException  %s" % (self.get_info())


class ApiServerNetworkException(ApiExceptionBase):
    """ @note: api server exception
    """
    def __init__(self, status=200, header=None, data=""):
        if header is None:
            header = {}
        self.status = status
        self.header = header
        self.data = data

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("ApiServerNetworkException Status: %s\nHeader: %s\nData: %s\n"
                % (self.status, headers, self.data))
