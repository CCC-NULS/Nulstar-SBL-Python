# "method name constants representing possible api calls to Nulstar.",
# "Nancy Schorr, December, 2019

AC_ADDRESS_PREFIX = "ac_addAddressPrefix"
AC_CREATE_ACCOUNT = "ac_createAccount"
AC_CREATE_CONTRACT_ACCOUNT = "ac_createContractAccount"
AC_CREATE_MULTI_SIGN_ACCOUNT = "ac_createMultiSignAccount"
AC_CREATE_MULTI_SIGN_TRANSFER = "ac_createMultiSignTransfer"
AC_CREATE_OFFLINE_ACCOUNT = "ac_createOfflineAccount"
AC_EXPORT_ACCOUNT_KEYSTORE = "ac_exportAccountKeyStore"
AC_EXPORT_KEYSTORE_JSON = "ac_exportKeyStoreJson"
AC_GET_ACCOUNT_LIST = "ac_getAccountList"
AC_GET_ACCOUNT_BYADDRESS = "ac_getAccountByAddress"
AC_GET_ADDRESS_LIST = "ac_getAddressList"
AC_GET_ADDRESS_PREFIX_BY_CHAINID = "ac_getAddressPrefixByChainId"
AC_GET_ALIASBY_ADDRESS = "ac_getAliasByAddress"
AC_GET_ALL_ADDRESS_PREFIX = "ac_getAllAddressPrefix"
AC_GET_ALL_PRIKEY = "ac_getAllPriKey"
AC_GET_ENCRYPTED_ADDRESS_LIST = "ac_getEncryptedAddressList"
AC_GET_MULTI_SIGN_ACCOUNT = "ac_getMultiSignAccount"
AC_GET_PRIKEY = "ac_getPriKeyByAddress"
AC_GET_PUBKEY = "ac_getPubKey"
AC_IMPORT_ACCOUNT_BY_PRIKEY = "ac_importAccountByPriKey"
AC_IMPORT_ACCOUNT_BY_KEYSTORE = "ac_importAccountByKeystore"
AC_IS_ALIAS_USABLE = "ac_isAliasUsable"
AC_IS_MULTISIGN_ACCOUNT_BUILDER = "ac_isMultiSignAccountBuilder"
AC_REMOVE_ACCOUNT = "ac_removeAccount"
AC_REMOVE_MULTISIGN_ACCOUNT = "ac_removeMultiSignAccount"
AC_SET_ALIAS = "ac_setAlias"
AC_SET_MULTISIGN_ALIAS = "ac_setMultiSignAlias"
AC_SET_REMARK = "ac_setRemark"
AC_SIGN_BLOCKDIGEST = "ac_signBlockDigest"
AC_SIGN_DIGEST = "ac_signDigest"
AC_SIGN_MULTISIGN_TRANSACTION = "ac_signMultiSignTransaction"
AC_TRANSFER = "ac_transfer"
AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD = "ac_updateOfflineAccountPassword"
AC_UPDATE_PASSWORD = "ac_updatePassword"
AC_VALIDATION_PASSWORD = "ac_validationPassword"
AC_VERIFY_SIGN_DATA = "ac_verifySignData"
SC_CCOUNT_CONTRACTS = "sc_account_contracts"
BATCH_VALIDATE_BEGIN = "batchValidateBegin"
BLOCK_VALIDATE = "blockValidate"
CANCEL_CROSSCHAIN = "cancelCrossChain"
CHECK_BLOCK_VERSION = "checkBlockVersion"
CHECK_UPDATES = "checkupdates"
CLEAR_UNCONFIRMED_TX = "clearUnconfirmTxs"
CM_ASSET_CIRCULATE_COMMIT = "cm_assetCirculateCommit"
CM_ASSET_CIRCULATE_ROLLBACK = "cm_assetCirculateRollBack"
CM_ASSET_CIRCULATE_VALIDATOR = "cm_assetCirculateValidator"
CM_ASSET = "cm_asset"
CM_ASSET_DISABLE = "cm_assetDisable"
CM_ASSET_REG = "cm_assetReg"
CM_CHAIN_ACTIVE = "cm_chainActive"
CM_CHAIN = "cm_chain"
CM_CHAIN_REG = "cm_chainReg"
CM_GET_CHAIN_ASSET = "cm_getChainAsset"
CM_GET_CIRCULATE_CHAIN_ASSET = "cm_getCirculateChainAsset"
CM_GET_CROSSCHAIN_SIMPLE_INFOS = "cm_getChainsSimpleInfo"
COMMIT_BATCH_UNCONFIRMED_TXS = "commitBatchUnconfirmedTxs"
COMMIT_BLOCKTXS = "commitBlockTxs"
COMMIT_UNCONFIRMEDTX = "commitUnconfirmedTx"
CONNECT_READY = "connectReady"
CREATE_AGENT_VALID = "createAgentValid"
CREATE_CROSSTX = "createCrossTx"
CROSSCHAIN_REGISTER_CHANGE = "crossChainRegisterChange"
CS_ADD_BLOCK = "cs_addBlock"
CS_ADD_EVIDENCE_RECORD = "cs_addEvidenceRecord"
CS_CHAIN_ROLLBACK = "cs_chainRollBack"
CS_CONTRACT_DEPOSIT = "cs_contractDeposit"
CS_CONTRACT_WITHDRAW = "cs_contractWithdraw"
CS_CREATE_AGENT = "cs_createAgent"
CS_CREATE_CONTRACT_AGENT = "cs_createContractAgent"
CS_CREATE_MULTI_AGENT = "cs_createMultiAgent"
CS_DEPOSIT_TOAGENT = "cs_depositToAgent"
CS_DOUBLE_SPEND_RECORD = "cs_doubleSpendRecord"
CS_GET_AGENT_ADDRESS_LIST = "cs_get_AgentAddressList"
CS_GET_AGENT_CHANGE_INFO = "cs_getAgentChangeInfo"
CS_GET_AGENT_INFO = "cs_getAgentInfo"
CS_GET_AGENT_LIST = "cs_getAgentList"
CS_GET_AGENT_STATUS = "cs_getAgentStatus"
CS_GET_CONSENSUS_CONFIG = "cs_getConsensusConfig"
CS_GET_CONTRACT_AGENT_INFO = "cs_getContractAgentInfo"
CS_GET_CONTRACT_DEPOSIT_INFO = "cs_getContractDepositInfo"
CS_GET_DEPOSIT_LIST = "cs_getDepositList"
CS_GET_INFO = "cs_getInfo"
CS_GET_NODE_PACKING_ADDR = "cs_getNodePackingAddress"
CS_GET_PACKER_INFO = "cs_getPackerInfo"
CS_GET_PUBLISH_LIST = "cs_getPublishList"
CS_GET_ROUND_INFO = "cs_getRoundInfo"
CS_GET_ROUND_MEMBER_LIST = "cs_getRoundMemberList"
CS_GET_SEED_NODE_INFO = "cs_getSeedNodeInfo"
CS_GET_WHOLEINFO = "cs_getwholeinfo"
CS_MULTI_DEPOSIT = "cs_multiDeposit"
CS_MULTI_WITHDRAW = "cs_multiWithdraw"
CS_RANDOM_RAW_SEEDS_COUNT = "cs_random_raw_seeds_count"
CS_RANDOM_RAW_SEEDS_HEIGHT = "cs_random_raw_seeds_height"
CS_RANDOM_SEED_COUNT = "cs_random_seed_count"
CS_RANDOM_SEED_HEIGHT = "cs_random_seed_height"
CS_RECEIVE_HEADERLIST = "cs_receiveHeaderList"
CS_RUN_CHAIN = "cs_runChain"
CS_RUN_MAINCHAIN = "cs_runMainChain"
CS_STOP_AGENT = "cs_stopagent"
CS_STOPAGENT = "cs_stopAgent"
CS_STOP_CHAIN = "cs_stopchain"
CS_STOPCHAIN = "cs_stopChain"
CS_STOP_CONTRACT_AGENT = "cs_stopContractAgent"
CS_STOP_MULTI_AGENT = "cs_stopMultiAgent"
CS_TRIGGER_COINBASE_CONTRACT = "cs_triggerCoinBaseContract"
CS_UPDATE_AGENT_CONSENSUS_STATUS = "cs_updateAgentConsensusStatus"
CS_UPDATE_AGENT_STATUS = "cs_updateAgentStatus"
CS_VALIDBLOCK = "cs_validBlock"
CS_WITHDRAW = "cs_withdraw"
DEPOSIT_VALID = "depositValid"
FORWARD_MESSAGE = "ForwardMessage"
GET_BALANCE = "getBalance"
GET_BALANCE_NONCE = "getBalanceNonce"
GET_BLOCK_BY_HASH = "getBlockByHash"
GET_BLOCK_BY_HEIGHT = "getBlockByHeight"
GET_BLOCKHEADER_BY_HASH = "getBlockHeaderByHash"
GET_BLOCKHEADER_BY_HEIGHT = "getBlockHeaderByHeight"
GET_BLOCKHEADER_PO_BY_HASH = "getBlockHeaderPoByHash"
GET_BLOCKHEADER_POBY_HEIGHT = "getBlockHeaderPoByHeight"
GET_BLOCKHEADERS_BY_HEIGHT_RANGE = "getBlockHeadersByHeightRange"
GET_BLOCKHEADERS_FOR_PROTOCOL = "getBlockHeadersForProtocol"
GET_BYZANTINE_COUNT = "getByzantineCount"
GET_CIRCULAT = "getCirculat"
GET_CONSOLIDATEDAPI = "GetConsolidatedAPI"
GET_CROSSCHAIN_INFOS = "getCrossChainInfos"
GET_CROSSTX_STATE = "getCrossTxState"
GET_CTX = "getCtx"
GET_CTX_STATE = "getCtxState"
GET_FREEZEGET_FREEZELIST_LIST = "getFreezeList"
GET_FRIEND_CHAIN_CIRCULATE = "getFriendChainCirculate"
GET_LATEST_BLOCKHEADERS = "getLatestBlockHeaders"
GET_LATEST__ROUND_BLOCKHEADERS = "getLatestRoundBlockHeaders"
GET_NETWORK_GROUP = "getGroupByChainId"
GET_NONCE = "getNonce"
GET_OTHERCTX = "getOtherCtx"
GET_REGISTERED_CHAIN_INFO_LIST = "getRegisteredChainInfoList"
GET_REGISTERED_CHAIN_MESSAGE = "getChains"
GET_ROUND_BLOCKHEADERS = "getRoundBlockHeaders"
GET_STATUS = "getStatus"
GET_VERSION = "getVersion"
INFO = "info"
LATEST_BLOCKHEADER = "latestBlockHeader"
LATEST_BLOCKHEADER_PO = "latestBlockHeaderPo"
LATEST_BLOCK = "latestBlock"
LATEST__HEIGHT = "latestHeight"
GET_ASSETS_BY_ID = "getAssetsById"
LISTENER_DEPENDENCIES_READY = "listenerDependenciesReady"
MSG_PROCESS = "msgProcess"
NEW_API_MOD_CROSS_TX = "newApiModuleCrossTx"
NEW_BLOCK_HEIGHT = "newBlockHeight"
NW_ACTIVE_CROSS = "nw_activeCross"
NW_ADD_NODES = "nw_addNodes"
NW_BROADCAST = "nw_broadcast"
NW_CREATE_NODEGROUP = "nw_createNodeGroup"
NW_CROSS_RANDOM_BROADCAST = "nw_crossRandomBroadcast"
NW_CUR_TIME_MILLIS = "nw_currentTimeMillis"
NW_DELETE_NODEGROUP = "nw_delNodeGroup"
NW_DEL_NODES = "nw_delNodes"
NW_GET_CHAIN_CONNECT_AMOUNT = "nw_getChainConnectAmount"
NW_GET_GROUP_BY_CHAINID = "nw_getGroupByChainId"
NW_GET_GROUPS = "nw_getGroups"
NW_GET_MAIN_NET_MAGIC_NUMBER = "nw_getMainMagicNumber"
NW_GET_NODES = "nw_getNodes"
NW_GET_SEEDS = "nw_getSeeds"
NW_INFO = "nw_info"
NW_NODES = "nw_nodes"
NW_PROTOCOL_REGISTER = "nw_protocolRegister"
NW_RECONNECT = "nw_reconnect"
NW_SEND_PEERS_MSG = "nw_sendPeersMsg"
NW_UPDATE_NODE_INFO = "nw_updateNodeInfo"
PARAM_TEST_CMD = "paramTestCmd"
PROTOCOL_PRIORITY_REGISTER = "protocolRegisterWithPriority"
PROTOCOL_VERSION_CHANGE = "protocolVersionChange"
RECEIVE_PACKING_BLOCK = "receivePackingBlock"
RECV_CIRCULAT = "recvCirculat"
RECV_CTX_HASH = "recvCtxHash"
RECV_CTX = "recvCtx"
RECV_CTX_SIGN = "recvCtxSign"
RECV_CTX_STATE = "recvCtxState"
RECV_OTHER_CTX = "recvOtherCtx"
RECV_REGCHAIN = "recvRegChain"
REG_CROSS_ASSET = "registerAsset"
REG_CROSSCHAIN = "registerCrossChain"
REGISTER_API = "RegisterAPI"
REGISTER_MODULE_DEPENDENCIES = "registerModuleDependencies"
REGISTER_PROTOCOL = "registerProtocol"
ROLLBACK_BLOCK = "rollbackBlock"
ROLLBACK_BLOCK_TXS = "rollBackBlockTxs"
ROLLBACK_TX_VALIDATE_STATUS = "rollbackTxValidateStatus"
ROLLBACK_UNCONFIRM_TX = "rollBackUnconfirmTx"
SAVE_BLOCK = "saveBlock"
SCAN_MANAGED_MODULES = "scanmanagedmodules"
SC_BATCH_BEFORE_END = "sc_batch_before_end"
SC_BATCH_BEGIN = "sc_batch_begin"
SC_BATCH_END = "sc_batch_end"
SC_CALL = "sc_call"
SC_CALL_VALIDATOR = "sc_call_validator"
SC_CONSTRUCTOR = "sc_constructor"
SC_CONTRACT_INFO = "sc_contract_info"
SC_CONTRACT_OFFLINE_TX_HASH_LIST = "sc_contract_offline_tx_hash_list"
SC_CONTRACT_RESULT_LIST = "sc_contract_result_list"
SC_CONTRACT_RESULT = "sc_contract_result"
SC_CONTRACT_TX = "sc_contract_tx"
SC_CREATE = "sc_create"
SC_CREATE_VALIDATOR = "sc_create_validator"
SC_DELETE = "sc_delete"
SC_DELETE_VALIDATOR = "sc_delete_validator"
SC_IMPUTED_CALL_GAS = "sc_imputed_call_gas"
SC_IMPUTED_CREATE_GAS = "sc_imputed_create_gas"
SC_INITIAL_ACCOUNT_TOKEN = "sc_initial_account_token"
SC_INVOKE_CONTRACT = "sc_invoke_contract"
SC_INVOKE_VIEW = "sc_invoke_view"
SC_PACKAGE_BATCH_END = "sc_package_batch_end"
SC_REGISTER_CM_FOR_CONTRACT = "sc_register_cmd_for_contract"
SC_TOKEN_ASSETS_LIST = "sc_token_assets_list"
SC_TOKEN_BALANCE = "sc_token_balance"
SC_TOKEN_TRANSFER_LIST = "sc_token_transfer_list"
SC_TOKEN_TRANSFER = "sc_token_transfer"
SC_TRANSFER_FEE = "sc_transfer_fee"
SC_TRANSFER = "sc_transfer"
SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT = "sc_trigger_payable_for_consensus_contract"
SC_UPLOAD = "sc_upload"
SC_VALIDATE_CALL = "sc_validate_call"
SC_VALIDATE_CREATE = "sc_validate_create"
SC_VALIDATE_DELETE = "sc_validate_delete"
SHUTDOWN_SYSTEM = "shutdownsystem"
STOP_AGENTVALID = "stopAgentValid"
STOP_ALL_MODULES = "stopallmodules"
TX_BACK_PACKABLE_TXS = "tx_backPackableTxs"
TX_BASE_VALIDATE = "tx_baseValidateTx"
TX_BATCH_VERIFY = "tx_batchVerify"
TX_BLOCK_HEIGHT = "tx_blockHeight"
TX_BL_STATE = "tx_bl_state"
TX_CLEAN_THREAD = "cleanTxThread"
TX_COMMIT = "txCommit"
TX_COUNT = "txCount"
TX_CS_STATE = "tx_cs_state"
TX_GENESIS_SAVE = "tx_gengsisSave"
TX_GET_BLOCKTXS_EXTEND = "tx_getBlockTxsExtend"
TX_GET_BLOCKTXS = "tx_getBlockTxs"
TX_GET_CONFIRMED_TX_CLIENT = "tx_getConfirmedTxClient"
TX_GET_CONFIRMED_TX = "tx_getConfirmedTx"
TX_GET_NONEXISTENT_UNCONFIRMED_HASHS = "tx_getNonexistentUnconfirmedHashs"
TX_GET_SYSTEMTYPES = "tx_getSystemTypes"
TX_GET_TX_CLIENT = "tx_getTxClient"
TX_GET_TX = "tx_getTx"
TX_HASH_LIST = "txHashList"
TX_HASH = "txHash"
TX_LIST = "txList"
TX_NEWTX = "tx_newTx"
TX_PACKABLE_TXS = "tx_packableTxs"
TX_REGISTER = "tx_register"
TX_ROLLBACK = "tx_rollback"
TX_SAVE = "tx_save"
NEW_NET_TX_THREAD = "newNetTxThread"
TX_VALIDATOR = "txValidator"
TX_VERIFY_TX = "tx_verifyTx"
UPDATE_CHAIN_ASSET = "updateChainAsset"
VERIFY_COINDATA_BATCH_PACKAGED = "verifyCoinDataBatchPackaged"
VERIFY_COINDATA = "verifyCoinData"
WITHDRAW_VALID = "withdrawValid"

# to generate _ALL_ list:     dir(nulsws_CONSTANTS_API_names)
__ALL__ = ['AC_ADDRESS_PREFIX', 'AC_CREATE_ACCOUNT', 'AC_CREATE_CONTRACT_ACCOUNT',
           'AC_CREATE_MULTI_SIGN_ACCOUNT', 'AC_CREATE_MULTI_SIGN_TRANSFER', 'AC_CREATE_OFFLINE_ACCOUNT',
           'AC_EXPORT_ACCOUNT_KEYSTORE', 'AC_EXPORT_KEYSTORE_JSON', 'AC_GET_ACCOUNT_BYADDRESS',
           'AC_GET_ACCOUNT_LIST', 'AC_GET_ADDRESS_LIST', 'AC_GET_ADDRESS_PREFIX_BY_CHAINID',
           'AC_GET_ALIASBY_ADDRESS', 'AC_GET_ALL_ADDRESS_PREFIX', 'AC_GET_ALL_PRIKEY',
           'AC_GET_ENCRYPTED_ADDRESS_LIST', 'AC_GET_MULTI_SIGN_ACCOUNT', 'AC_GET_PRIKEY', 'AC_GET_PUBKEY',
           'AC_IMPORT_ACCOUNT_BY_KEYSTORE', 'AC_IMPORT_ACCOUNT_BY_PRIKEY', 'AC_IS_ALIAS_USABLE',
           'AC_IS_MULTISIGN_ACCOUNT_BUILDER', 'AC_REMOVE_ACCOUNT', 'AC_REMOVE_MULTISIGN_ACCOUNT',
           'AC_SET_ALIAS', 'AC_SET_MULTISIGN_ALIAS', 'AC_SET_REMARK', 'AC_SIGN_BLOCKDIGEST', 'AC_SIGN_DIGEST',
           'AC_SIGN_MULTISIGN_TRANSACTION', 'AC_TRANSFER', 'AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD',
           'AC_UPDATE_PASSWORD', 'AC_VALIDATION_PASSWORD', 'AC_VERIFY_SIGN_DATA', 'BATCH_VALIDATE_BEGIN',
           'BLOCK_VALIDATE', 'CANCEL_CROSSCHAIN', 'CHECK_BLOCK_VERSION', 'CHECK_UPDATES',
           'CLEAR_UNCONFIRMED_TX', 'CM_ASSET', 'CM_ASSET_CIRCULATE_COMMIT', 'CM_ASSET_CIRCULATE_ROLLBACK',
           'CM_ASSET_CIRCULATE_VALIDATOR', 'CM_ASSET_DISABLE', 'CM_ASSET_REG', 'CM_CHAIN', 'CM_CHAIN_ACTIVE',
           'CM_CHAIN_REG', 'CM_GET_CHAIN_ASSET', 'CM_GET_CIRCULATE_CHAIN_ASSET',
           'CM_GET_CROSSCHAIN_SIMPLE_INFOS', 'COMMIT_BATCH_UNCONFIRMED_TXS', 'COMMIT_BLOCKTXS',
           'COMMIT_UNCONFIRMEDTX', 'CONNECT_READY', 'CREATE_AGENT_VALID', 'CREATE_CROSSTX',
           'CROSSCHAIN_REGISTER_CHANGE', 'CS_ADD_BLOCK', 'CS_ADD_EVIDENCE_RECORD', 'CS_CHAIN_ROLLBACK',
           'CS_CONTRACT_DEPOSIT', 'CS_CONTRACT_WITHDRAW', 'CS_CREATE_AGENT', 'CS_CREATE_CONTRACT_AGENT',
           'CS_CREATE_MULTI_AGENT', 'CS_DEPOSIT_TOAGENT', 'CS_DOUBLE_SPEND_RECORD',
           'CS_GET_AGENT_ADDRESS_LIST', 'CS_GET_AGENT_CHANGE_INFO', 'CS_GET_AGENT_INFO', 'CS_GET_AGENT_LIST',
           'CS_GET_AGENT_STATUS', 'CS_GET_CONSENSUS_CONFIG', 'CS_GET_CONTRACT_AGENT_INFO',
           'CS_GET_CONTRACT_DEPOSIT_INFO', 'CS_GET_DEPOSIT_LIST', 'CS_GET_INFO', 'CS_GET_NODE_PACKING_ADDR',
           'CS_GET_PACKER_INFO', 'CS_GET_PUBLISH_LIST', 'CS_GET_ROUND_INFO', 'CS_GET_ROUND_MEMBER_LIST',
           'CS_GET_SEED_NODE_INFO', 'CS_GET_WHOLEINFO', 'CS_MULTI_DEPOSIT', 'CS_MULTI_WITHDRAW',
           'CS_RANDOM_RAW_SEEDS_COUNT', 'CS_RANDOM_RAW_SEEDS_HEIGHT', 'CS_RANDOM_SEED_COUNT',
           'CS_RANDOM_SEED_HEIGHT', 'CS_RECEIVE_HEADERLIST', 'CS_RUN_CHAIN', 'CS_RUN_MAINCHAIN',
           'CS_STOPAGENT', 'CS_STOPCHAIN', 'CS_STOP_AGENT', 'CS_STOP_CHAIN', 'CS_STOP_CONTRACT_AGENT',
           'CS_STOP_MULTI_AGENT', 'CS_TRIGGER_COINBASE_CONTRACT', 'CS_UPDATE_AGENT_CONSENSUS_STATUS',
           'CS_UPDATE_AGENT_STATUS', 'CS_VALIDBLOCK', 'CS_WITHDRAW', 'DEPOSIT_VALID', 'FORWARD_MESSAGE',
           'GET_ASSETS_BY_ID', 'GET_BALANCE', 'GET_BALANCE_NONCE', 'GET_BLOCKHEADERS_BY_HEIGHT_RANGE',
           'GET_BLOCKHEADERS_FOR_PROTOCOL', 'GET_BLOCKHEADER_BY_HASH', 'GET_BLOCKHEADER_BY_HEIGHT',
           'GET_BLOCKHEADER_POBY_HEIGHT', 'GET_BLOCKHEADER_PO_BY_HASH', 'GET_BLOCK_BY_HASH',
           'GET_BLOCK_BY_HEIGHT', 'GET_BYZANTINE_COUNT', 'GET_CIRCULAT', 'GET_CONSOLIDATEDAPI',
           'GET_CROSSCHAIN_INFOS', 'GET_CROSSTX_STATE', 'GET_CTX', 'GET_CTX_STATE',
           'GET_FREEZEGET_FREEZELIST_LIST', 'GET_FRIEND_CHAIN_CIRCULATE', 'GET_LATEST_BLOCKHEADERS',
           'GET_LATEST__ROUND_BLOCKHEADERS', 'GET_NETWORK_GROUP', 'GET_NONCE', 'GET_OTHERCTX',
           'GET_REGISTERED_CHAIN_INFO_LIST', 'GET_REGISTERED_CHAIN_MESSAGE', 'GET_ROUND_BLOCKHEADERS',
           'GET_STATUS', 'GET_VERSION', 'INFO', 'LATEST_BLOCK', 'LATEST_BLOCKHEADER', 'LATEST_BLOCKHEADER_PO',
           'LATEST__HEIGHT', 'LISTENER_DEPENDENCIES_READY', 'MSG_PROCESS', 'NEW_API_MOD_CROSS_TX',
           'NEW_BLOCK_HEIGHT', 'NEW_NET_TX_THREAD', 'NW_ACTIVE_CROSS', 'NW_ADD_NODES', 'NW_BROADCAST',
           'NW_CREATE_NODEGROUP', 'NW_CROSS_RANDOM_BROADCAST', 'NW_CUR_TIME_MILLIS', 'NW_DELETE_NODEGROUP',
           'NW_DEL_NODES', 'NW_GET_CHAIN_CONNECT_AMOUNT', 'NW_GET_GROUPS', 'NW_GET_GROUP_BY_CHAINID',
           'NW_GET_MAIN_NET_MAGIC_NUMBER', 'NW_GET_NODES', 'NW_GET_SEEDS', 'NW_INFO', 'NW_NODES',
           'NW_PROTOCOL_REGISTER', 'NW_RECONNECT', 'NW_SEND_PEERS_MSG', 'NW_UPDATE_NODE_INFO',
           'PARAM_TEST_CMD', 'PROTOCOL_PRIORITY_REGISTER', 'PROTOCOL_VERSION_CHANGE', 'RECEIVE_PACKING_BLOCK',
           'RECV_CIRCULAT', 'RECV_CTX', 'RECV_CTX_HASH', 'RECV_CTX_SIGN', 'RECV_CTX_STATE', 'RECV_OTHER_CTX',
           'RECV_REGCHAIN', 'REGISTER_API', 'REGISTER_MODULE_DEPENDENCIES', 'REGISTER_PROTOCOL',
           'REG_CROSSCHAIN', 'REG_CROSS_ASSET', 'ROLLBACK_BLOCK', 'ROLLBACK_BLOCK_TXS',
           'ROLLBACK_TX_VALIDATE_STATUS', 'ROLLBACK_UNCONFIRM_TX', 'SAVE_BLOCK', 'SCAN_MANAGED_MODULES',
           'SC_BATCH_BEFORE_END', 'SC_BATCH_BEGIN', 'SC_BATCH_END', 'SC_CALL', 'SC_CALL_VALIDATOR',
           'SC_CCOUNT_CONTRACTS', 'SC_CONSTRUCTOR', 'SC_CONTRACT_INFO', 'SC_CONTRACT_OFFLINE_TX_HASH_LIST',
           'SC_CONTRACT_RESULT', 'SC_CONTRACT_RESULT_LIST', 'SC_CONTRACT_TX', 'SC_CREATE',
           'SC_CREATE_VALIDATOR', 'SC_DELETE', 'SC_DELETE_VALIDATOR', 'SC_IMPUTED_CALL_GAS',
           'SC_IMPUTED_CREATE_GAS', 'SC_INITIAL_ACCOUNT_TOKEN', 'SC_INVOKE_CONTRACT', 'SC_INVOKE_VIEW',
           'SC_PACKAGE_BATCH_END', 'SC_REGISTER_CM_FOR_CONTRACT', 'SC_TOKEN_ASSETS_LIST', 'SC_TOKEN_BALANCE',
           'SC_TOKEN_TRANSFER', 'SC_TOKEN_TRANSFER_LIST', 'SC_TRANSFER', 'SC_TRANSFER_FEE',
           'SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT', 'SC_UPLOAD', 'SC_VALIDATE_CALL', 'SC_VALIDATE_CREATE',
           'SC_VALIDATE_DELETE', 'SHUTDOWN_SYSTEM', 'STOP_AGENTVALID', 'STOP_ALL_MODULE_S',
           'TX_BACK_PACKABLE_TXS', 'TX_BASE_VALIDATE', 'TX_BATCH_VERIFY', 'TX_BLOCK_HEIGHT', 'TX_BL_STATE',
           'TX_CHAIN_ID', 'TX_CLEAN_THREAD', 'TX_COMMIT', 'TX_COUNT', 'TX_CS_STATE', 'TX_GENESIS_SAVE',
           'TX_GET_BLOCKTXS', 'TX_GET_BLOCKTXS_EXTEND', 'TX_GET_CONFIRMED_TX', 'TX_GET_CONFIRMED_TX_CLIENT',
           'TX_GET_NONEXISTENT_UNCONFIRMED_HASHS', 'TX_GET_SYSTEMTYPES', 'TX_GET_TX', 'TX_GET_TX_CLIENT',
           'TX_HASH', 'TX_HASH_LIST', 'TX_LIST', 'TX_NEWTX', 'TX_PACKABLE_TXS', 'TX_REGISTER', 'TX_ROLLBACK',
           'TX_SAVE', 'TX_VALIDATOR', 'TX_VERIFY_TX', 'UPDATE_CHAIN_ASSET', 'VERIFY_COINDATA',
           'VERIFY_COINDATA_BATCH_PACKAGED', 'WITHDRAW_VALID']



# ---------------- Example -------------------------------------------------------------------

#
# Example of type 3 message:
# {
#     "ProtocolVersion": "0.1.0"
#     "MessageID": m_id,
#     "TimeZone": tzone,
#     "Timestamp": t_stamp
#     "MessageType": "Request",
#     "MessageData": {
#         "RequestType": "1",
#         "SubscriptionEventCounter": "0",
#         "SubscriptionPeriod": "1",
#         "SubscriptionRange": "[100]",
#         "ResponseMaxSize": "0",
#         "RequestMethods": [
#           {
#             "GetBalance": {
#               "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#             }
#           },
#           {
#             "GetHeight": {}
#           }
#         ]
#        }
#     }