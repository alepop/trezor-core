from trezor.utils import unimport


MAX_CHAIN_ID = 2147483630


def ethereum_signing_check(msg):
    if msg.gas_price is None or msg.gas_limit is None:
        return False
    if msg.to is None:
        if msg.data_length == 0:
            return False
    else:
        if len(msg.to) != 20:
            return False
    if len(msg.gas_price) + len(msg.gas_limit) > 30:
        return False


@unimport
async def ethereum_sign_tx(ctx, msg):
    from trezor.messages.EthereumTxAck import EthereumTxAck

    if msg.value is None:
        msg.value = b''
    if msg.data_initial_chunk is None:
        msg.data_initial_chunk = b''
    if msg.data_length is None:
        msg.data_length = 0
    if msg.to is None:
        msg.to = b''
    if msg.nonce is None:
        msg.nonce = b''

    if msg.chain_id is None:
        msg.chain_id = 0
    else:
        if msg.chain_id < 1 or msg.chain_id > MAX_CHAIN_ID:
            raise ValueError(FailureType.DataError, 'Chain Id out of bounds')

    if msg.data_length > 0:
        if not msg.data_initial_chunk:
            raise ValueError(Failure.DataError, 'Data length provided, but no initial chunk')
        if msg.data_length > 16000000:
            raise ValueError(Failure.DataError, 'Data length exceeds limit')
        if len(msg.data_initial_chunk) > msg.data_length:
            raise ValueError(Failure.DataError, 'Invalid size of initial chunk')


    if not ethereum_signing_check(msg):
        raise ValueError(Failure.DataError, 'Safety check failed')

    # TODO: tokens

    print('XXX', ctx, msg)
    return EthereumTxAck()
