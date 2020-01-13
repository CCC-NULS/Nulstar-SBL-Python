#!/usr/bin/python3.7

""",

by Nancy Schorr for Nuls-io
January 2020
""",
# "method name constants representing possible api calls to Nulstar.",

# These don't need to change often if ever
# only used twice - once in client, once in nulsws_call_db


class NulsWsApiLabel(object):
    ApiLabelDict = {
        'AC_ADD_ADDRESS_PREFIX': "ac_addAddressPrefix",
        'AC_CREATE_ACCOUNT': "ac_createAccount",
        'AC_CREATE_CONTRACT_ACCOUNT': "ac_createContractAccount",
        'AC_CREATE_MULTI_SIGN_ACCOUNT': "ac_createMultiSignAccount",
        'AC_CREATE_MULTI_SIGN_TRANSFER': "ac_createMultiSignTransfer",
        'AC_CREATE_OFFLINE_ACCOUNT': "ac_createOfflineAccount",
        'AC_EXPORT_ACCOUNT_KEYSTORE': "ac_exportAccountKeyStore",
        'AC_EXPORT_KEYSTORE_JSON': "ac_exportKeyStoreJson",
        'AC_GET_ACCOUNT_LIST': "ac_getAccountList",
        'AC_GET_ACCOUNT_BYADDRESS': "ac_getAccountByAddress",
        'AC_GET_ADDRESS_LIST': "ac_getAddressList",
        'AC_GET_ADDRESS_PREFIX_BY_CHAINID': "ac_getAddressPrefixByChainId",
        'AC_GET_ALIASBY_ADDRESS': "ac_getAliasByAddress",
        'AC_GET_ALL_ADDRESS_PREFIX': "ac_getAllAddressPrefix",
        'AC_GET_ALL_PRIKEY': "ac_getAllPriKey",
        'AC_GET_ENCRYPTED_ADDRESS_LIST': "ac_getEncryptedAddressList",
        'AC_GET_MULTI_SIGN_ACCOUNT': "ac_getMultiSignAccount",
        'AC_GET_PRIKEY': "ac_getPriKeyByAddress",
        'AC_GET_PUBKEY': "ac_getPubKey",
        'AC_IMPORT_ACCOUNT_BY_PRIKEY': "ac_importAccountByPriKey",
        'AC_IMPORT_ACCOUNT_BY_KEYSTORE': "ac_importAccountByKeystore",
        'AC_IS_ALIAS_USABLE': "ac_isAliasUsable",
        'AC_IS_MULTISIGN_ACCOUNT_BUILDER': "ac_isMultiSignAccountBuilder",
        'AC_REMOVE_ACCOUNT': "ac_removeAccount",
        'AC_REMOVE_MULTISIGN_ACCOUNT': "ac_removeMultiSignAccount",
        'AC_SET_ALIAS': "ac_setAlias",
        'AC_SET_MULTISIGN_ALIAS': "ac_setMultiSignAlias",
        'AC_SET_REMARK': "ac_setRemark",
        'AC_SIGN_BLOCKDIGEST': "ac_signBlockDigest",
        'AC_SIGN_DIGEST': "ac_signDigest",
        'AC_SIGN_MULTISIGN_TRANSACTION': "ac_signMultiSignTransaction",
        'AC_TRANSFER': "ac_transfer",
        'AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD': "ac_updateOfflineAccountPassword",
        'AC_UPDATE_PASSWORD': "ac_updatePassword",
        'AC_VALIDATION_PASSWORD': "ac_validationPassword",
        'AC_VERIFY_SIGN_DATA': "ac_verifySignData",
        'SC_CCOUNT_CONTRACTS': "sc_account_contracts",
        'BATCH_VALIDATE_BEGIN': "batchValidateBegin",
        'BLOCK_VALIDATE': "blockValidate",
        'CANCEL_CROSSCHAIN': "cancelCrossChain",
        'CHECK_BLOCK_VERSION': "checkBlockVersion",
        'CHECK_UPDATES': "checkupdates",
        'CLEAR_UNCONFIRMED_TX': "clearUnconfirmTxs",
        'CM_ASSET_CIRCULATE_COMMIT': "cm_assetCirculateCommit",
        'CM_ASSET_CIRCULATE_ROLLBACK': "cm_assetCirculateRollBack",
        'CM_ASSET_CIRCULATE_VALIDATOR': "cm_assetCirculateValidator",
        'CM_ASSET': 'cm_asset',
        'CM_ASSET_DISABLE': 'cm_assetDisable',
        'CM_ASSET_REG': 'cm_assetReg',
        'CM_CHAIN_ACTIVE': 'cm_chainActive',
        'CM_CHAIN': 'cm_chain',
        'CM_CHAIN_REG': 'cm_chainReg',
        'CM_GET_CHAIN_ASSET': 'cm_getChainAsset',
        'CM_GET_CIRCULATE_CHAIN_ASSET': 'cm_getCirculateChainAsset',
        'CM_GET_CROSSCHAIN_SIMPLE_INFOS': 'cm_getChainsSimpleInfo',
        'COMMIT_BATCH_UNCONFIRMED_TXS': 'commitBatchUnconfirmedTxs',
        'COMMIT_BLOCKTXS': 'commitBlockTxs',
        'COMMIT_UNCONFIRMEDTX': 'commitUnconfirmedTx',
        'CONNECT_READY': 'connectReady',
        'CREATE_AGENT_VALID': 'createAgentValid',
        'CREATE_CROSSTX': 'createCrossTx',
        'CROSSCHAIN_REGISTER_CHANGE': 'crossChainRegisterChange',
        'CS_ADD_BLOCK': 'cs_addBlock',
        'CS_ADD_EVIDENCE_RECORD': 'cs_addEvidenceRecord',
        'CS_CHAIN_ROLLBACK': 'cs_chainRollBack',
        'CS_CONTRACT_DEPOSIT': 'cs_contractDeposit',
        'CS_CONTRACT_WITHDRAW': 'cs_contractWithdraw',
        'CS_CREATE_AGENT': 'cs_createAgent',
        'CS_CREATE_CONTRACT_AGENT': 'cs_createContractAgent',
        'CS_CREATE_MULTI_AGENT': 'cs_createMultiAgent',
        'CS_DEPOSIT_TOAGENT': 'cs_depositToAgent',
        'CS_DOUBLE_SPEND_RECORD': 'cs_doubleSpendRecord',
        'CS_GET_AGENT_ADDRESS_LIST': 'cs_get_AgentAddressList',
        'CS_GET_AGENT_CHANGE_INFO': 'cs_getAgentChangeInfo',
        'CS_GET_AGENT_INFO': 'cs_getAgentInfo',
        'CS_GET_AGENT_LIST': 'cs_getAgentList',
        'CS_GET_AGENT_STATUS': 'cs_getAgentStatus',
        'CS_GET_CONSENSUS_CONFIG': 'cs_getConsensusConfig',
        'CS_GET_CONTRACT_AGENT_INFO': 'cs_getContractAgentInfo',
        'CS_GET_CONTRACT_DEPOSIT_INFO': 'cs_getContractDepositInfo',
        'CS_GET_DEPOSIT_LIST': 'cs_getDepositList',
        'CS_GET_INFO': 'cs_getInfo',
        'CS_GET_NODE_PACKING_ADDR': 'cs_getNodePackingAddress',
        'CS_GET_PACKER_INFO': 'cs_getPackerInfo',
        'CS_GET_PUBLISH_LIST': 'cs_getPublishList',
        'CS_GET_ROUND_INFO': 'cs_getRoundInfo',
        'CS_GET_ROUND_MEMBER_LIST': 'cs_getRoundMemberList',
        'CS_GET_SEED_NODE_INFO': 'cs_getSeedNodeInfo',
        'CS_GET_WHOLEINFO': 'cs_getwholeinfo',
        'CS_MULTI_DEPOSIT': 'cs_multiDeposit',
        'CS_MULTI_WITHDRAW': 'cs_multiWithdraw',
        'CS_RANDOM_RAW_SEEDS_COUNT': 'cs_random_raw_seeds_count',
        'CS_RANDOM_RAW_SEEDS_HEIGHT': 'cs_random_raw_seeds_height',
        'CS_RANDOM_SEED_COUNT': 'cs_random_seed_count',
        'CS_RANDOM_SEED_HEIGHT': 'cs_random_seed_height',
        'CS_RECEIVE_HEADERLIST': 'cs_receiveHeaderList',
        'CS_RUN_CHAIN': 'cs_runChain',
        'CS_RUN_MAINCHAIN': 'cs_runMainChain',
        'CS_STOP_AGENT': 'cs_stopagent',
        'CS_STOPAGENT': 'cs_stopAgent',
        'CS_STOP_CHAIN': 'cs_stopchain',
        'CS_STOPCHAIN': 'cs_stopChain',
        'CS_STOP_CONTRACT_AGENT': 'cs_stopContractAgent',
        'CS_STOP_MULTI_AGENT': 'cs_stopMultiAgent',
        'CS_TRIGGER_COINBASE_CONTRACT': 'cs_triggerCoinBaseContract',
        'CS_UPDATE_AGENT_CONSENSUS_STATUS': 'cs_updateAgentConsensusStatus',
        'CS_UPDATE_AGENT_STATUS': 'cs_updateAgentStatus',
        'CS_VALIDBLOCK': 'cs_validBlock',
        'CS_WITHDRAW': 'cs_withdraw',
        'DEPOSIT_VALID': 'depositValid',
        'FORWARD_MESSAGE': 'ForwardMessage',
        'GET_BALANCE': 'getBalance',
        'GET_BALANCE_NONCE': 'getBalanceNonce',
        'GET_BLOCK_BY_HASH': 'getBlockByHash',
        'GET_BLOCK_BY_HEIGHT': 'getBlockByHeight',
        'GET_BLOCKHEADER_BY_HASH': 'getBlockHeaderByHash',
        'GET_BLOCKHEADER_BY_HEIGHT': 'getBlockHeaderByHeight',
        'GET_BLOCKHEADER_PO_BY_HASH': 'getBlockHeaderPoByHash',
        'GET_BLOCKHEADER_POBY_HEIGHT': 'getBlockHeaderPoByHeight',
        'GET_BLOCKHEADERS_BY_HEIGHT_RANGE': 'getBlockHeadersByHeightRange',
        'GET_BLOCKHEADERS_FOR_PROTOCOL': 'getBlockHeadersForProtocol',
        'GET_BYZANTINE_COUNT': 'getByzantineCount',
        'GET_CIRCULAT': 'getCirculat',
        'GET_CONSOLIDATEDAPI': 'GetConsolidatedAPI',
        'GET_CROSSCHAIN_INFOS': 'getCrossChainInfos',
        'GET_CROSSTX_STATE': 'getCrossTxState',
        'GET_CTX': 'getCtx',
        'GET_CTX_STATE': 'getCtxState',
        'GET_FREEZEGET_FREEZELIST_LIST': 'getFreezeList',
        'GET_FRIEND_CHAIN_CIRCULATE': 'getFriendChainCirculate',
        'GET_LATEST_BLOCKHEADERS': 'getLatestBlockHeaders',
        'GET_LATEST_ROUND_BLOCKHEADERS': 'getLatestRoundBlockHeaders',
        'GET_NETWORK_GROUP': 'getGroupByChainId',
        'GET_NONCE': 'getNonce',
        'GET_OTHERCTX': 'getOtherCtx',
        'GET_REGISTERED_CHAIN_INFO_LIST': 'getRegisteredChainInfoList',
        'GET_REGISTERED_CHAIN_MESSAGE': 'getChains',
        'GET_ROUND_BLOCKHEADERS': 'getRoundBlockHeaders',
        'GET_STATUS': 'getStatus',
        'GET_VERSION': 'getVersion',
        'INFO': 'info',
        'LATEST_BLOCKHEADER': 'latestBlockHeader',
        'LATEST_BLOCKHEADER_PO': 'latestBlockHeaderPo',
        'LATEST_BLOCK': 'latestBlock',
        'LATEST_HEIGHT': 'latestHeight',
        'GET_ASSETS_BY_ID': 'getAssetsById',
        'LISTENER_DEPENDENCIES_READY': 'listenerDependenciesReady',
        'MSG_PROCESS': 'msgProcess',
        'NEW_API_MOD_CROSS_TX': 'newApiModuleCrossTx',
        'NEW_BLOCK_HEIGHT': 'newBlockHeight',
        'NW_ACTIVE_CROSS': 'nw_activeCross',
        'NW_ADD_NODES': 'nw_addNodes',
        'NW_BROADCAST': 'nw_broadcast',
        'NW_CREATE_NODEGROUP': 'nw_createNodeGroup',
        'NW_CROSS_RANDOM_BROADCAST': 'nw_crossRandomBroadcast',
        'NW_CUR_TIME_MILLIS': 'nw_currentTimeMillis',
        'NW_DELETE_NODEGROUP': 'nw_delNodeGroup',
        'NW_DEL_NODES': 'nw_delNodes',
        'NW_GET_CHAIN_CONNECT_AMOUNT': 'nw_getChainConnectAmount',
        'NW_GET_GROUP_BY_CHAINID': 'nw_getGroupByChainId',
        'NW_GET_GROUPS': 'nw_getGroups',
        'NW_GET_MAIN_NET_MAGIC_NUMBER': 'nw_getMainMagicNumber',
        'NW_GET_NODES': 'nw_getNodes',
        'NW_GET_SEEDS': 'nw_getSeeds',
        'NW_INFO': 'nw_info',
        'NW_NODES': 'nw_nodes',
        'NW_PROTOCOL_REGISTER': 'nw_protocolRegister',
        'NW_RECONNECT': 'nw_reconnect',
        'NW_SEND_PEERS_MSG': 'nw_sendPeersMsg',
        'NW_UPDATE_NODE_INFO': 'nw_updateNodeInfo',
        'PARAM_TEST_CMD': 'paramTestCmd',
        'PROTOCOL_PRIORITY_REGISTER': 'protocolRegisterWithPriority',
        'PROTOCOL_VERSION_CHANGE': 'protocolVersionChange',
        'RECEIVE_PACKING_BLOCK': 'receivePackingBlock',
        'RECV_CIRCULAT': 'recvCirculat',
        'RECV_CTX_HASH': 'recvCtxHash',
        'RECV_CTX': 'recvCtx',
        'RECV_CTX_SIGN': 'recvCtxSign',
        'RECV_CTX_STATE': 'recvCtxState',
        'RECV_OTHER_CTX': 'recvOtherCtx',
        'RECV_REGCHAIN': 'recvRegChain',
        'REG_CROSS_ASSET': 'registerAsset',
        'REG_CROSSCHAIN': 'registerCrossChain',
        'REGISTER_API': 'RegisterAPI',
        'REGISTER_MODULE_DEPENDENCIES': 'registerModuleDependencies',
        'REGISTER_PROTOCOL': 'registerProtocol',
        'ROLLBACK_BLOCK': 'rollbackBlock',
        'ROLLBACK_BLOCK_TXS': 'rollBackBlockTxs',
        'ROLLBACK_TX_VALIDATE_STATUS': 'rollbackTxValidateStatus',
        'ROLLBACK_UNCONFIRM_TX': 'rollBackUnconfirmTx',
        'SAVE_BLOCK': 'saveBlock',
        'SCAN_MANAGED_MODULES': 'scanmanagedmodules',
        'SC_BATCH_BEFORE_END': 'sc_batch_before_end',
        'SC_BATCH_BEGIN': 'sc_batch_begin',
        'SC_BATCH_END': 'sc_batch_end',
        'SC_CALL': 'sc_call',
        'SC_CALL_VALIDATOR': 'sc_call_validator',
        'SC_CONSTRUCTOR': 'sc_constructor',
        'SC_CONTRACT_INFO': 'sc_contract_info',
        'SC_CONTRACT_OFFLINE_TX_HASH_LIST': 'sc_contract_offline_tx_hash_list',
        'SC_CONTRACT_RESULT_LIST': 'sc_contract_result_list',
        'SC_CONTRACT_RESULT': 'sc_contract_result',
        'SC_CONTRACT_TX': 'sc_contract_tx',
        'SC_CREATE': 'sc_create',
        'SC_CREATE_VALIDATOR': 'sc_create_validator',
        'SC_DELETE': 'sc_delete',
        'SC_DELETE_VALIDATOR': 'sc_delete_validator',
        'SC_IMPUTED_CALL_GAS': 'sc_imputed_call_gas',
        'SC_IMPUTED_CREATE_GAS': 'sc_imputed_create_gas',
        'SC_INITIAL_ACCOUNT_TOKEN': 'sc_initial_account_token',
        'SC_INVOKE_CONTRACT': 'sc_invoke_contract',
        'SC_INVOKE_VIEW': 'sc_invoke_view',
        'SC_PACKAGE_BATCH_END': 'sc_package_batch_end',
        'SC_REGISTER_CM_FOR_CONTRACT': 'sc_register_cmd_for_contract',
        'SC_TOKEN_ASSETS_LIST': 'sc_token_assets_list',
        'SC_TOKEN_BALANCE': 'sc_token_balance',
        'SC_TOKEN_TRANSFER_LIST': 'sc_token_transfer_list',
        'SC_TOKEN_TRANSFER': 'sc_token_transfer',
        'SC_TRANSFER_FEE': 'sc_transfer_fee',
        'SC_TRANSFER': 'sc_transfer',
        'SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT': 'sc_trigger_payable_for_consensus_contract',
        'SC_UPLOAD': 'sc_upload',
        'SC_VALIDATE_CALL': 'sc_validate_call',
        'SC_VALIDATE_CREATE': 'sc_validate_create',
        'SC_VALIDATE_DELETE': 'sc_validate_delete',
        'SHUTDOWN_SYSTEM': 'shutdownsystem',
        'STOP_AGENTVALID': 'stopAgentValid',
        'STOP_ALL_MODULES': 'stopallmodules',
        'TX_BACK_PACKABLE_TXS': 'tx_backPackableTxs',
        'TX_BASE_VALIDATE': 'tx_baseValidateTx',
        'TX_BATCH_VERIFY': 'tx_batchVerify',
        'TX_BLOCK_HEIGHT': 'tx_blockHeight',
        'TX_BL_STATE': 'tx_bl_state',
        'TX_CLEAN_THREAD': 'cleanTxThread',
        'TX_COMMIT': 'txCommit',
        'TX_COUNT': 'txCount',
        'TX_CS_STATE': 'tx_cs_state',
        'TX_GENESIS_SAVE': 'tx_gengsisSave',
        'TX_GET_BLOCKTXS_EXTEND': 'tx_getBlockTxsExtend',
        'TX_GET_BLOCKTXS': 'tx_getBlockTxs',
        'TX_GET_CONFIRMED_TX_CLIENT': 'tx_getConfirmedTxClient',
        'TX_GET_CONFIRMED_TX': 'tx_getConfirmedTx',
        'TX_GET_NONEXISTENT_UNCONFIRMED_HASHS': 'tx_getNonexistentUnconfirmedHashs',
        'TX_GET_SYSTEMTYPES': 'tx_getSystemTypes',
        'TX_GET_TX_CLIENT': 'tx_getTxClient',
        'TX_GET_TX': 'tx_getTx',
        'TX_HASH_LIST': 'txHashList',
        'TX_HASH': 'txHash',
        'TX_LIST': 'txList',
        'TX_NEWTX': 'tx_newTx',
        'TX_PACKABLE_TXS': 'tx_packableTxs',
        'TX_REGISTER': 'tx_register',
        'TX_ROLLBACK': 'tx_rollback',
        'TX_SAVE': 'tx_save',
        'NEW_NET_TX_THREAD': 'newNetTxThread',
        'TX_VALIDATOR': 'txValidator',
        'TX_VERIFY_TX': 'tx_verifyTx',
        'UPDATE_CHAIN_ASSET': 'updateChainAsset',
        'VERIFY_COINDATA_BATCH_PACKAGED': 'verifyCoinDataBatchPackaged',
        'VERIFY_COINDATA': 'verifyCoinData',
        'WITHDRAW_VALID': 'withdrawValid'}
    
    
    
#
#
#
#     AC_ADD_ADDRESS_PREFIX = "ac_addAddressPrefix",
# AC_CREATE_ACCOUNT = "ac_createAccount",
# AC_CREATE_CONTRACT_ACCOUNT = "ac_createContractAccount",
# AC_CREATE_MULTI_SIGN_ACCOUNT = "ac_createMultiSignAccount",
# AC_CREATE_MULTI_SIGN_TRANSFER = "ac_createMultiSignTransfer",
# AC_CREATE_OFFLINE_ACCOUNT = "ac_createOfflineAccount",
# AC_EXPORT_ACCOUNT_KEYSTORE = "ac_exportAccountKeyStore",
# AC_EXPORT_KEYSTORE_JSON = "ac_exportKeyStoreJson",
# AC_GET_ACCOUNT_LIST = "ac_getAccountList",
# AC_GET_ACCOUNT_BYADDRESS = "ac_getAccountByAddress",
# AC_GET_ADDRESS_LIST = "ac_getAddressList",
# AC_GET_ADDRESS_PREFIX_BY_CHAINID = "ac_getAddressPrefixByChainId",
# AC_GET_ALIASBY_ADDRESS = "ac_getAliasByAddress",
# AC_GET_ALL_ADDRESS_PREFIX = "ac_getAllAddressPrefix",
# AC_GET_ALL_PRIKEY = "ac_getAllPriKey",
# AC_GET_ENCRYPTED_ADDRESS_LIST = "ac_getEncryptedAddressList",
# AC_GET_MULTI_SIGN_ACCOUNT = "ac_getMultiSignAccount",
# AC_GET_PRIKEY = "ac_getPriKeyByAddress",
# AC_GET_PUBKEY = "ac_getPubKey",
# AC_IMPORT_ACCOUNT_BY_PRIKEY = "ac_importAccountByPriKey",
# AC_IMPORT_ACCOUNT_BY_KEYSTORE = "ac_importAccountByKeystore",
# AC_IS_ALIAS_USABLE = "ac_isAliasUsable",
# AC_IS_MULTISIGN_ACCOUNT_BUILDER = "ac_isMultiSignAccountBuilder",
# AC_REMOVE_ACCOUNT = "ac_removeAccount",
# AC_REMOVE_MULTISIGN_ACCOUNT = "ac_removeMultiSignAccount",
# AC_SET_ALIAS = "ac_setAlias",
# AC_SET_MULTISIGN_ALIAS = "ac_setMultiSignAlias",
# AC_SET_REMARK = "ac_setRemark",
# AC_SIGN_BLOCKDIGEST = "ac_signBlockDigest",
# AC_SIGN_DIGEST = "ac_signDigest",
# AC_SIGN_MULTISIGN_TRANSACTION = "ac_signMultiSignTransaction",
# AC_TRANSFER = "ac_transfer",
# AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD = "ac_updateOfflineAccountPassword",
# AC_UPDATE_PASSWORD = "ac_updatePassword",
# AC_VALIDATION_PASSWORD = "ac_validationPassword",
# AC_VERIFY_SIGN_DATA = "ac_verifySignData",
# SC_CCOUNT_CONTRACTS = "sc_account_contracts",
# BATCH_VALIDATE_BEGIN = "batchValidateBegin",
# BLOCK_VALIDATE = "blockValidate",
# CANCEL_CROSSCHAIN = "cancelCrossChain",
# CHECK_BLOCK_VERSION = "checkBlockVersion",
# CHECK_UPDATES = "checkupdates",
# CLEAR_UNCONFIRMED_TX = "clearUnconfirmTxs",
# CM_ASSET_CIRCULATE_COMMIT = "cm_assetCirculateCommit",
# CM_ASSET_CIRCULATE_ROLLBACK = "cm_assetCirculateRollBack",
# CM_ASSET_CIRCULATE_VALIDATOR = "cm_assetCirculateValidator",
# CM_ASSET = "cm_asset",
# CM_ASSET_DISABLE = "cm_assetDisable",
# CM_ASSET_REG = "cm_assetReg",
# CM_CHAIN_ACTIVE = "cm_chainActive",
# CM_CHAIN = "cm_chain",
# CM_CHAIN_REG = "cm_chainReg",
# CM_GET_CHAIN_ASSET = "cm_getChainAsset",
# CM_GET_CIRCULATE_CHAIN_ASSET = "cm_getCirculateChainAsset",
# CM_GET_CROSSCHAIN_SIMPLE_INFOS = "cm_getChainsSimpleInfo",
# COMMIT_BATCH_UNCONFIRMED_TXS = "commitBatchUnconfirmedTxs",
# COMMIT_BLOCKTXS = "commitBlockTxs",
# COMMIT_UNCONFIRMEDTX = "commitUnconfirmedTx",
# CONNECT_READY = "connectReady",
# CREATE_AGENT_VALID = "createAgentValid",
# CREATE_CROSSTX = "createCrossTx",
# CROSSCHAIN_REGISTER_CHANGE = "crossChainRegisterChange",
# CS_ADD_BLOCK = "cs_addBlock",
# CS_ADD_EVIDENCE_RECORD = "cs_addEvidenceRecord",
# CS_CHAIN_ROLLBACK = "cs_chainRollBack",
# CS_CONTRACT_DEPOSIT = "cs_contractDeposit",
# CS_CONTRACT_WITHDRAW = "cs_contractWithdraw",
# CS_CREATE_AGENT = "cs_createAgent",
# CS_CREATE_CONTRACT_AGENT = "cs_createContractAgent",
# CS_CREATE_MULTI_AGENT = "cs_createMultiAgent",
# CS_DEPOSIT_TOAGENT = "cs_depositToAgent",
# CS_DOUBLE_SPEND_RECORD = "cs_doubleSpendRecord",
# CS_GET_AGENT_ADDRESS_LIST = "cs_get_AgentAddressList",
# CS_GET_AGENT_CHANGE_INFO = "cs_getAgentChangeInfo",
# CS_GET_AGENT_INFO = "cs_getAgentInfo",
# CS_GET_AGENT_LIST = "cs_getAgentList",
# CS_GET_AGENT_STATUS = "cs_getAgentStatus",
# CS_GET_CONSENSUS_CONFIG = "cs_getConsensusConfig",
# CS_GET_CONTRACT_AGENT_INFO = "cs_getContractAgentInfo",
# CS_GET_CONTRACT_DEPOSIT_INFO = "cs_getContractDepositInfo",
# CS_GET_DEPOSIT_LIST = "cs_getDepositList",
# CS_GET_INFO = "cs_getInfo",
# CS_GET_NODE_PACKING_ADDR = "cs_getNodePackingAddress",
# CS_GET_PACKER_INFO = "cs_getPackerInfo",
# CS_GET_PUBLISH_LIST = "cs_getPublishList",
# CS_GET_ROUND_INFO = "cs_getRoundInfo",
# CS_GET_ROUND_MEMBER_LIST = "cs_getRoundMemberList",
# CS_GET_SEED_NODE_INFO = "cs_getSeedNodeInfo",
# CS_GET_WHOLEINFO = "cs_getwholeinfo",
# CS_MULTI_DEPOSIT = "cs_multiDeposit",
# CS_MULTI_WITHDRAW = "cs_multiWithdraw",
# CS_RANDOM_RAW_SEEDS_COUNT = "cs_random_raw_seeds_count",
# CS_RANDOM_RAW_SEEDS_HEIGHT = "cs_random_raw_seeds_height",
# CS_RANDOM_SEED_COUNT = "cs_random_seed_count",
# CS_RANDOM_SEED_HEIGHT = "cs_random_seed_height",
# CS_RECEIVE_HEADERLIST = "cs_receiveHeaderList",
# CS_RUN_CHAIN = "cs_runChain",
# CS_RUN_MAINCHAIN = "cs_runMainChain",
# CS_STOP_AGENT = "cs_stopagent",
# CS_STOPAGENT = "cs_stopAgent",
# CS_STOP_CHAIN = "cs_stopchain",
# CS_STOPCHAIN = "cs_stopChain",
# CS_STOP_CONTRACT_AGENT = "cs_stopContractAgent",
# CS_STOP_MULTI_AGENT = "cs_stopMultiAgent",
# CS_TRIGGER_COINBASE_CONTRACT = "cs_triggerCoinBaseContract",
# CS_UPDATE_AGENT_CONSENSUS_STATUS = "cs_updateAgentConsensusStatus",
# CS_UPDATE_AGENT_STATUS = "cs_updateAgentStatus",
# CS_VALIDBLOCK = "cs_validBlock",
# CS_WITHDRAW = "cs_withdraw",
# DEPOSIT_VALID = "depositValid",
# FORWARD_MESSAGE = "ForwardMessage",
# GET_BALANCE = "getBalance",
# GET_BALANCE_NONCE = "getBalanceNonce",
# GET_BLOCK_BY_HASH = "getBlockByHash",
# GET_BLOCK_BY_HEIGHT = "getBlockByHeight",
# GET_BLOCKHEADER_BY_HASH = "getBlockHeaderByHash",
# GET_BLOCKHEADER_BY_HEIGHT = "getBlockHeaderByHeight",
# GET_BLOCKHEADER_PO_BY_HASH = "getBlockHeaderPoByHash",
# GET_BLOCKHEADER_POBY_HEIGHT = "getBlockHeaderPoByHeight",
# GET_BLOCKHEADERS_BY_HEIGHT_RANGE = "getBlockHeadersByHeightRange",
# GET_BLOCKHEADERS_FOR_PROTOCOL = "getBlockHeadersForProtocol",
# GET_BYZANTINE_COUNT = "getByzantineCount",
# GET_CIRCULAT = "getCirculat",
# GET_CONSOLIDATEDAPI = "GetConsolidatedAPI",
# GET_CROSSCHAIN_INFOS = "getCrossChainInfos",
# GET_CROSSTX_STATE = "getCrossTxState",
# GET_CTX = "getCtx",
# GET_CTX_STATE = "getCtxState",
# GET_FREEZEGET_FREEZELIST_LIST = "getFreezeList",
# GET_FRIEND_CHAIN_CIRCULATE = "getFriendChainCirculate",
# GET_LATEST_BLOCKHEADERS = "getLatestBlockHeaders",
# GET_LATEST_ROUND_BLOCKHEADERS = "getLatestRoundBlockHeaders",
# GET_NETWORK_GROUP = "getGroupByChainId",
# GET_NONCE = "getNonce",
# GET_OTHERCTX = "getOtherCtx",
# GET_REGISTERED_CHAIN_INFO_LIST = "getRegisteredChainInfoList",
# GET_REGISTERED_CHAIN_MESSAGE = "getChains",
# GET_ROUND_BLOCKHEADERS = "getRoundBlockHeaders",
# GET_STATUS = "getStatus",
# GET_VERSION = "getVersion",
# INFO = "info",
# LATEST_BLOCKHEADER = "latestBlockHeader",
# LATEST_BLOCKHEADER_PO = "latestBlockHeaderPo",
# LATEST_BLOCK = "latestBlock",
# LATEST_HEIGHT = "latestHeight",
# GET_ASSETS_BY_ID = "getAssetsById",
# LISTENER_DEPENDENCIES_READY = "listenerDependenciesReady",
# MSG_PROCESS = "msgProcess",
# NEW_API_MOD_CROSS_TX = "newApiModuleCrossTx",
# NEW_BLOCK_HEIGHT = "newBlockHeight",
# NW_ACTIVE_CROSS = "nw_activeCross",
# NW_ADD_NODES = "nw_addNodes",
# NW_BROADCAST = "nw_broadcast",
# NW_CREATE_NODEGROUP = "nw_createNodeGroup",
# NW_CROSS_RANDOM_BROADCAST = "nw_crossRandomBroadcast",
# NW_CUR_TIME_MILLIS = "nw_currentTimeMillis",
# NW_DELETE_NODEGROUP = "nw_delNodeGroup",
# NW_DEL_NODES = "nw_delNodes",
# NW_GET_CHAIN_CONNECT_AMOUNT = "nw_getChainConnectAmount",
# NW_GET_GROUP_BY_CHAINID = "nw_getGroupByChainId",
# NW_GET_GROUPS = "nw_getGroups",
# NW_GET_MAIN_NET_MAGIC_NUMBER = "nw_getMainMagicNumber",
# NW_GET_NODES = "nw_getNodes",
# NW_GET_SEEDS = "nw_getSeeds",
# NW_INFO = "nw_info",
# NW_NODES = "nw_nodes",
# NW_PROTOCOL_REGISTER = "nw_protocolRegister",
# NW_RECONNECT = "nw_reconnect",
# NW_SEND_PEERS_MSG = "nw_sendPeersMsg",
# NW_UPDATE_NODE_INFO = "nw_updateNodeInfo",
# PARAM_TEST_CMD = "paramTestCmd",
# PROTOCOL_PRIORITY_REGISTER = "protocolRegisterWithPriority",
# PROTOCOL_VERSION_CHANGE = "protocolVersionChange",
# RECEIVE_PACKING_BLOCK = "receivePackingBlock",
# RECV_CIRCULAT = "recvCirculat",
# RECV_CTX_HASH = "recvCtxHash",
# RECV_CTX = "recvCtx",
# RECV_CTX_SIGN = "recvCtxSign",
# RECV_CTX_STATE = "recvCtxState",
# RECV_OTHER_CTX = "recvOtherCtx",
# RECV_REGCHAIN = "recvRegChain",
# REG_CROSS_ASSET = "registerAsset",
# REG_CROSSCHAIN = "registerCrossChain",
# REGISTER_API = "RegisterAPI",
# REGISTER_MODULE_DEPENDENCIES = "registerModuleDependencies",
# REGISTER_PROTOCOL = "registerProtocol",
# ROLLBACK_BLOCK = "rollbackBlock",
# ROLLBACK_BLOCK_TXS = "rollBackBlockTxs",
# ROLLBACK_TX_VALIDATE_STATUS = "rollbackTxValidateStatus",
# ROLLBACK_UNCONFIRM_TX = "rollBackUnconfirmTx",
# SAVE_BLOCK = "saveBlock",
# SCAN_MANAGED_MODULES = "scanmanagedmodules",
# SC_BATCH_BEFORE_END = "sc_batch_before_end",
# SC_BATCH_BEGIN = "sc_batch_begin",
# SC_BATCH_END = "sc_batch_end",
# SC_CALL = "sc_call",
# SC_CALL_VALIDATOR = "sc_call_validator",
# SC_CONSTRUCTOR = "sc_constructor",
# SC_CONTRACT_INFO = "sc_contract_info",
# SC_CONTRACT_OFFLINE_TX_HASH_LIST = "sc_contract_offline_tx_hash_list",
# SC_CONTRACT_RESULT_LIST = "sc_contract_result_list",
# SC_CONTRACT_RESULT = "sc_contract_result",
# SC_CONTRACT_TX = "sc_contract_tx",
# SC_CREATE = "sc_create",
# SC_CREATE_VALIDATOR = "sc_create_validator",
# SC_DELETE = "sc_delete",
# SC_DELETE_VALIDATOR = "sc_delete_validator",
# SC_IMPUTED_CALL_GAS = "sc_imputed_call_gas",
# SC_IMPUTED_CREATE_GAS = "sc_imputed_create_gas",
# SC_INITIAL_ACCOUNT_TOKEN = "sc_initial_account_token",
# SC_INVOKE_CONTRACT = "sc_invoke_contract",
# SC_INVOKE_VIEW = "sc_invoke_view",
# SC_PACKAGE_BATCH_END = "sc_package_batch_end",
# SC_REGISTER_CM_FOR_CONTRACT = "sc_register_cmd_for_contract",
# SC_TOKEN_ASSETS_LIST = "sc_token_assets_list",
# SC_TOKEN_BALANCE = "sc_token_balance",
# SC_TOKEN_TRANSFER_LIST = "sc_token_transfer_list",
# SC_TOKEN_TRANSFER = "sc_token_transfer",
# SC_TRANSFER_FEE = "sc_transfer_fee",
# SC_TRANSFER = "sc_transfer",
# SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT = "sc_trigger_payable_for_consensus_contract",
# SC_UPLOAD = "sc_upload",
# SC_VALIDATE_CALL = "sc_validate_call",
# SC_VALIDATE_CREATE = "sc_validate_create",
# SC_VALIDATE_DELETE = "sc_validate_delete",
# SHUTDOWN_SYSTEM = "shutdownsystem",
# STOP_AGENTVALID = "stopAgentValid",
# STOP_ALL_MODULES = "stopallmodules",
# TX_BACK_PACKABLE_TXS = "tx_backPackableTxs",
# TX_BASE_VALIDATE = "tx_baseValidateTx",
# TX_BATCH_VERIFY = "tx_batchVerify",
# TX_BLOCK_HEIGHT = "tx_blockHeight",
# TX_BL_STATE = "tx_bl_state",
# TX_CLEAN_THREAD = "cleanTxThread",
# TX_COMMIT = "txCommit",
# TX_COUNT = "txCount",
# TX_CS_STATE = "tx_cs_state",
# TX_GENESIS_SAVE = "tx_gengsisSave",
# TX_GET_BLOCKTXS_EXTEND = "tx_getBlockTxsExtend",
# TX_GET_BLOCKTXS = "tx_getBlockTxs",
# TX_GET_CONFIRMED_TX_CLIENT = "tx_getConfirmedTxClient",
# TX_GET_CONFIRMED_TX = "tx_getConfirmedTx",
# TX_GET_NONEXISTENT_UNCONFIRMED_HASHS = "tx_getNonexistentUnconfirmedHashs",
# TX_GET_SYSTEMTYPES = "tx_getSystemTypes",
# TX_GET_TX_CLIENT = "tx_getTxClient",
# TX_GET_TX = "tx_getTx",
# TX_HASH_LIST = "txHashList",
# TX_HASH = "txHash",
# TX_LIST = "txList",
# TX_NEWTX = "tx_newTx",
# TX_PACKABLE_TXS = "tx_packableTxs",
# TX_REGISTER = "tx_register",
# TX_ROLLBACK = "tx_rollback",
# TX_SAVE = "tx_save",
# NEW_NET_TX_THREAD = "newNetTxThread",
# TX_VALIDATOR = "txValidator",
# TX_VERIFY_TX = "tx_verifyTx",
# UPDATE_CHAIN_ASSET = "updateChainAsset",
# VERIFY_COINDATA_BATCH_PACKAGED = "verifyCoinDataBatchPackaged",
# VERIFY_COINDATA = "verifyCoinData",
# WITHDRAW_VALID = "withdrawValid",
