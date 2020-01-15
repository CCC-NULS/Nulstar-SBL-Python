#!/usr/bin/python3.7

import json
from asyncio import sleep as a_sleep
import asyncio

from tornado.websocket import websocket_connect  # WebSocketClosedError
import nulsws_python.src.nulsws_python.nulsws_library as nulsws_library
from nulsws_python.src.nulsws_python.prep_request import PrepRequest
from nulsws_python.src.nulsws_python.make_top import MakeTop
from nulsws_python.src.nulsws_python.regular_request import RegularRequest


class RunQueries(object):

    async def run_queries(self, m_indx, run_list, conf_ini_d, mtpe=3):
        pause_time = .7
        nlib_obj = nulsws_library.NulsWsLib()
        prepr_obj = PrepRequest()
        prep_request = prepr_obj.prep_request

        connection = None
        conn_m = conf_ini_d.get("connect_method")
        host_r = conf_ini_d.get("host_req")
        port_r = conf_ini_d.get("port_req")
        websock_url = ''.join([conn_m, "://", host_r, ":", str(port_r)])
        debug = 1

        if not debug:
            mt_obj = MakeTop()
            top_plus_mid_dict = mt_obj.make_top(m_indx, conf_ini_d)  # must be done

            connection = await websocket_connect(websock_url)  # 1) CONNECT
            # await a_sleep(pause_time)
            while not connection:
                await a_sleep(pause_time)
            top_plus_mid_dict_json = json.dumps(top_plus_mid_dict)
            nlib_obj.json_prt(top_plus_mid_dict, "* * * First message going out- NEGOTIATE: \n")

            await connection.write_message(top_plus_mid_dict_json)  # 2) WRITE
            # await a_sleep(self.s_time)
            negotiate_result = await connection.read_message()  # 3 READ
            await a_sleep(pause_time)
            nlib_obj.json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        nlib_obj.myprint("------end Negotiate----------------------------------------")
        rr_obj = RegularRequest()

        for run_item in run_list:
            m_indx += 1

            if mtpe == 3:
                main_request = prep_request(m_indx, run_item, conf_ini_d)

                if debug:
                    json_reg = json.dumps(main_request)
                    nlib_obj.json_prt(json_reg, " ")

                else:
                    await rr_obj.regular_request(connection, main_request)
