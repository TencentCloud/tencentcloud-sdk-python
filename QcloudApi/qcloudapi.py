#! /usr/bin/env python
# -*- coding: utf-8 -*-

from QcloudApi.modules import base


class QcloudApi(object):
    def __init__(self, module, config):
        self.module = module
        self.config = config

    def _factory(self, module, config):
        if (module == 'cdb'):
            from .modules.cdb import Cdb
            service = Cdb(config)
        elif (module == 'account'):
            from .modules.account import Account
            service = Account(config)
        elif (module == 'cvm'):
            from .modules.cvm import Cvm
            service = Cvm(config)
        elif (module == 'image'):
            from .modules.image import Image
            service = Image(config)
        elif (module == 'lb'):
            from .modules.lb import Lb
            service = Lb(config)
        elif (module == 'sec'):
            from .modules.sec import Sec
            service = Sec(config)
        elif (module == 'trade'):
            from .modules.trade import Trade
            service = Trade(config)
        elif (module == 'bill'):
            from .modules.bill import Bill
            service = Bill(config)
        elif (module == 'monitor'):
            from .modules.monitor import Monitor
            service = Monitor(config)
        elif (module == 'cdn'):
            from .modules.cdn import Cdn
            service = Cdn(config)
        elif (module == 'vpc'):
            from .modules.vpc import Vpc
            service = Vpc(config)
        elif (module == 'vod'):
            from .modules.vod import Vod
            service = Vod(config)
        elif (module == 'yunsou'):
            from .modules.yunsou import Yunsou
            service = Yunsou(config)
        elif (module == 'wenzhi'):
            from .modules.wenzhi import Wenzhi
            service = Wenzhi(config)
        elif (module == 'market'):
            from .modules.market import Market
            service = Market(config)
        elif (module == 'live'):
            from .modules.live import Live
            service = Live(config)
        elif (module == 'eip'):
            from .modules.eip import Eip
            service = Eip(config)
        elif (module == 'cbs'):
            from .modules.cbs import Cbs
            service = Cbs(config)
        elif (module == 'snapshot'):
            from .modules.snapshot import Snapshot
            service = Snapshot(config)
        elif (module == 'scaling'):
            from .modules.scaling import Scaling
            service = Scaling(config)
        elif (module == 'cmem'):
            from .modules.cmem import Cmem
            service = Cmem(config)
        elif (module == 'tdsql'):
            from .modules.tdsql import Tdsql
            service = Tdsql(config)
        elif (module == 'bm'):
            from .modules.bm import Bm
            service = Bm(config)
        elif (module == 'bmlb'):
            from .modules.bmlb import Bmlb
            service = Bmlb(config)
        elif (module == 'redis'):
            from .modules.redis import Redis
            service = Redis(config)
        elif (module == 'dfw'):
            from .modules.dfw import Dfw
            service = Dfw(config)
        elif (module == 'ccs'):
            from .modules.ccs import Ccs
            service = Ccs(config)
        elif (module == 'feecenter'):
            from .modules.feecenter import Feecenter
            service = Feecenter(config)
        elif (module == 'cns'):
            from .modules.cns import Cns
            service = Cns(config)
        elif (module == 'bmeip'):
            from .modules.bmeip import Bmeip
            service = Bmeip(config)
        elif (module == 'bmvpc'):
            from .modules.bmvpc import Bmvpc
            service = Bmvpc(config)
        elif module == 'bgpip':
            from .modules.bgpip import Bgpip
            service = Bgpip(config)
        elif module == 'scf':
            from .modules.scf import Scf
            service = Scf(config)
        elif module == 'apigateway':
            from .modules.apigateway import APIGateway
            service = APIGateway(config)
        elif module == 'batch':
            from .modules.batch import Batch
            service = Batch(config)
        elif module == 'cloudaudit':
            from .modules.cloudaudit import CloudAudit
            service = CloudAudit(config)
        elif module == 'tmt':
            from .modules.tmt import Tmt
            service = Tmt(config)
        elif module == 'partners':
            from .modules.partners import Partners
            service = Partners(config)
        elif module == 'tbaas':
            from .modules.tbaas import Tbaas
            service = Tbaas(config)
        elif module == 'athena':
            from .modules.athena import Athena
            service = Athena(config)
        elif module == 'emr':
            from .modules.emr import Emr
            service = Emr(config)
        elif module == 'sts':
            from .modules.sts import Sts
            service = Sts(config)
        elif module == 'ccr':
            from .modules.ccr import Ccr
            service = Ccr(config)
        elif module == 'dc':
            from .modules.dc import Dc
            service = Dc(config)
        else:
            config.setdefault("endpoint", module + '.api.qcloud.com')
            service = base.Base(config)

        return service

    def setSecretId(self, secretId):
        self.config['secretId'] = secretId

    def setSecretKey(self, secretKey):
        self.config['secretKey'] = secretKey

    def setRequestMethod(self, method):
        self.config['method'] = method

    def setRegion(self, region):
        self.config['Region'] = region

    def setSignatureMethod(self, SignatureMethod):
        self.config['SignatureMethod'] = SignatureMethod

    def generateUrl(self, action, params):
        service = self._factory(self.module, self.config)
        return service.generateUrl(action, params)

    def call(self, action, params, req_timeout=None, debug=False):
        """
        @type action: string
        @param action: action interface

        @type params: dict
        @param params: interface parameters

        @type req_timeout: int
        @param req_timeout: request timeout(seconds)

        @type debug: bool
        @param debug: debug switch
        """
        service = self._factory(self.module, self.config)
        if req_timeout is not None:
            service.set_req_timeout(req_timeout)
        if debug:
            service.open_debug()

        methods = dir(service)
        for method in methods:
            if (method == action):
                func = getattr(service, action)
                return func(params)

        return service.call(action, params)
