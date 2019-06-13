# -*- coding: utf-8 -*-
import logging


LUGGAGE = {
    'polls'       : 'default',
    'polls_2'       : 'demo2',
    'news_in'       : 'push_in',
    'news_ru'       : 'push_ru',
    'news_us'       : 'push_us',
    'appboy'        : 'push_zz',
    'old_push'      : 'old_push',
    'opera_news'    : 'opera_news',
    'news_wangjinyu':'demo2'
}
class Router(object):
    def db_for_read(self, model, **hints):
        logging.error('read---------------%r'%model._meta.app_label)
        # return model._meta.app_label
        return LUGGAGE.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        logging.error('writer---------------%r'%model._meta.app_label)

        # return model._meta.app_label
        return LUGGAGE.get(model._meta.app_label, 'default')

    def allow_relation(self, obj1, obj2, **hints):
        return True


    def allow_migrate(self, db, model):
        logging.error('%r%r'%(db,model._meta.app_label))
        """
        Make sure the app02 app only appears in the hvdb database.
        """


        # 两个数据库写入对应应用，默认demo中缺少必要的数据库
        # return LUGGAGE.get(model._meta.app_label)==db
        # return True
        # logging.error('migrate---------------%r*%r'%(db,model._meta.app_label_))
        # pass
        if db == 'demo2':
            return model._meta.app_label == 'polls_2'
        elif model._meta.app_label == 'polls_2':
            return False

