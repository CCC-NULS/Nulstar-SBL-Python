#!usr/bin/python3.7


'''
author:  Nancy M Schorr, for Nuls
December 2, 2019

NEGOTIATE CONNECTION

The first message that should be sent. If this message receives a response of '1', then
service may proceed to further requests.

With a failure, a NegotiateConnectionResponse object will be received with
Status of '0' (Failure) and this service should disconnect immediately.

Messages have a common structure composed of six fields:

•  ProtocolVersion: version the service to understand,2 numbers, major/minor
•  MessageID: identifies a request.
•  Timestamp:  Number  of  seconds  since  epoch January 1,1970
•  TimeZone: The time zone where the request was originated
•  MessageType: The message type, these are specified on section 3
•  MessageData: A Json object with the message payload

Example Negotiate Connection message - order of items doesn't matter when at the same level
{ "MessageID":"1569897424187-1",
  "MessageType":"NegotiateConnection",
  "TimeZone":"-4",
  "Timestamp":"1569897424187",
  "MessageData":{
    "CompressionAlgorithm":"zlib",
    "CompressionRate":"0",
    "ProtocolVersion":"0.1"
  },
}

Compression Rate can be values 0 through 9.
Compression Algorithm is normally "zlib"

 -- Enter your custom settings data via the library file 'nulsws_msgtype1.py'.

Note: Don't use typing.Dict - it can cause json problems when converted.

This file right now provides support for the the client only.

'''

import json
from time import time, timezone
from nulsws_msgtype1 import proto_ver, compress_type1, comp_rate1
from nulsws_staticvals import m_dict, bigtest

from nulsws_staticvals import compress_type_label, compress_rate_label, msg_data_label, \
    msg_id_label, msg_type_label, negotiate_conn_label, negotiate_stat_label, \
    negotiate_conn_resp_label, proto_label, tmstmp_label, tmzone_label, request_label, \
    request_internalid_label, request_date_label, request_time_label, json_seps

json_d = None

def do_math(msg_index=1):
    t_stamp = int(time() * 1000)      # change float to int
    tzone = int(timezone / 3600)  # change float to int to str
    m_id = str(t_stamp) + "-" + str(msg_index)
    return t_stamp, tzone, m_id

def prep_header_section(msg_type: int):         # this section builds 4 items:
    #1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4",   #3 "Timestamp": "1569897424187"
                                            # #4 "MessageType": "NegotiateConnection",
    msg_type_name = m_dict.__getitem__(msg_type)
    t_stamp, tzone, m_id= do_math()
    top_part = {
                proto_label: proto_ver,
                msg_id_label: m_id,
                tmstmp_label : t_stamp,
                tmzone_label: tzone,
                msg_type_label: msg_type_name }
    return top_part

#-----------prep_data_type1--------------------------------------#
def prep_data_type1():
        # this section has any number of items depending on the msg type
    top_sect = prep_header_section(1)
    data_part = {msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type1,
                  compress_rate_label: comp_rate1}}
    top_sect.update(data_part)
    json_str = json.dumps(top_sect, separators=json_seps)
    return json_str

#-----------prep_data_type3--------------------------------------#

def prep_data_type3_old():
    # this section has any number of items depending on the msg type
    top_sect = prep_header_section(3)

    # values from user defined library/config file
    from nulsws_msgtype3 import sub_event_ct, sub_period_int, sub_range, res_max_size, \
        address_val, msg_type3

    # labels:
    from nulsws_staticvals import request_t_label, sub_rg_label, subscrip_evnt_ct_label, \
        subscrip_period_label, req_method_label, get_bal_label, response_max_size_label, \
        address_label, get_height_label

    data_getbalance = {get_bal_label: { address_label: address_val  }}

    # data_height = {get_height_label: {}}
    #rquest_list = [data_getbalance, {get_height_label: {}}]
    rquest_list = [data_getbalance]
    req_methods_sec = {req_method_label: rquest_list }

    data_part = {request_t_label: str(msg_type3),
                 subscrip_evnt_ct_label: str(sub_event_ct),
                 subscrip_period_label: str(sub_period_int),
                 sub_rg_label: str(sub_range),
                 response_max_size_label: str(res_max_size)
                }

    data_part.update(req_methods_sec)

    msg_data_sect = {msg_data_label: data_part}
    top_sect.update(msg_data_sect)
    jds_indented = json.dumps(top_sect, indent=4)

    json_str = json.dumps(top_sect)
    #jds = json.dumps(bigtest, indent=4)
    #print(json_str)
    #json_str = json.dumps(bigtest)
    print(jds_indented)

    return json_str




def check_json_answer(answer) -> bool:
    jload = json.loads(answer)
    jds = json.dumps(jload, separators=(':', ','), indent=4)
    print("check answer jds value= ", jds)
    msg_d_answer = jload.get(msg_data_label)
    mt = jload.get(msg_type_label)
    if mt == negotiate_conn_resp_label:
        final_int = msg_d_answer.get(negotiate_stat_label)
        if final_int == '1':
            print("Negotiate Status was 1. All is good")
            return True
        else:
            return False

def myprint(x, y=None, debug=True):
    if debug:
        if y:
            print(x, end=' ')
            print(y)
        else:
            print(x)

def prep_data_type3():   #requesttype 2 - return ack and response
    t_stamp, zn, m_id = do_math()
    stat_msg = {
        "ProtocolVersion": "0.1.0",
        "MessageID": m_id,
        "TimeZone": zn,
        "Timestamp": t_stamp,
        "MessageType": "Request",
        "MessageData": {
            "RequestType": "2",
            "SubscriptionEventCounter": "0",
            "SubscriptionPeriod": "0",
            "SubscriptionRange": "0",
            "ResponseMaxSize": "0",
            "RequestMethods":
              {
                #"GetChainID": { }

              "developerNodeAddress": {}
              }
          }
        }
    print(json.dumps(stat_msg, indent=4))
    jd = json.dumps(stat_msg)
    return jd


#   -------------------------------
#   "MessageData": {
#     "RequestType": "1",
#     "SubscriptionEventCounter": "0",
#     "SubscriptionPeriod": "1",
#     "SubscriptionRange": "[100]",
#     "ResponseMaxSize": "0",
#     "RequestMethods": [
#       {
#         "GetBalance": {
#           "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#         }
#       },
#       {
#         "GetHeight": {}
#       }
#     ]
#   }
# }
# def prep_data_type3_almostworks():   #requesttype 2 - return ack and response
#     t_stamp, zn, m_id = do_math()
#     stat_msg = {
#         "MessageID": m_id,
#         "TimeZone": zn,
#         "Timestamp": t_stamp,
#         "MessageType": "Request",
#         "MessageData": {
#             "RequestType": "2",
#             "SubscriptionEventCounter": "0",
#             "SubscriptionPeriod": "0",
#             "SubscriptionRange": "0",
#             "ResponseMaxSize": "0",
#             "RequestMethods":
#               {
#                 "GetCPUInfo": {
#                   "lMaxCPUs": "1"
#                 }
#               }
#           }
#         }



def prep_data_type3_OLD():
    t_stamp, zn, m_id = do_math()

    stat_msg = {
        "MessageID": m_id,
        "TimeZone": zn,
        "Timestamp": t_stamp,
        "MessageType": "Request",
        "MessageData": {
            "ResponseMaxSize": 0,
            "SubscriptionEventCounter": 0,
            "SubscriptionPeriod": 0,
            "SubscriptionRange": 0,
            "Abbeviation": "NSTM",
            "Methods":[
                {
                "MethodDescription":"Query information about CPU",
                "MethodMinEvent":"0",
                "MethodMinPeriod":"0",
                "MethodName":"GetCPUInfo",
                "MethodScope":"admin",
                "Parameters": [  {
                      "ParameterName": "lMaxCPUs",
                      "ParameterType": "int"
                        } ]
                }]
            } }

    print(json.dumps(stat_msg, indent=4))
    json_str = json.dumps(stat_msg)
    return json_str
