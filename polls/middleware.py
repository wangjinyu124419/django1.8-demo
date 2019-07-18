# -*- coding: utf-8 -*-
import time

import  logging

class LoggingMiddleware(object):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        execute_time = time.time() - request.start_time
        # path = request.get_full_path()
        # log=logging.getLogger(__name__)
        # logging.INFO('wang')
        # print 'execute_time:%f'%execute_time
        logger = logging.getLogger(__name__)

        logger.error('execute_time:%f'%execute_time)
        # logging.INFO('request: %s --execute_time: %f' % (path, execute_time))
        return response