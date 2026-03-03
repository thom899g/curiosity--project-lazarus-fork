"""
Robust blockchain RPC connectivity manager with fallback mechanisms and health checks.
Handles multiple chains and ensures reliable connectivity for swap operations.
"""
import logging
from typing import Dict, Optional, Tuple
from web3 import Web3
from web3.providers import HTTPProvider
from web3.exceptions import TransactionNotFound, TimeExhausted
from eth_account import Account
from ..config import blockchain_config

logger = logging.getLogger(__name__)

class RPCManager:
    """Manages blockchain RPC connections with health monitoring and failover"""
    
    def __init__(self):
        self.connections: Dict[str, Web3] = {}
        self.health_status: Dict[str, bool] = {}
        self.account: Optional[Account] = None
        self._initialize_connections()
        self._initialize_wallet()
    
    def _initialize_connections(self) -> None:
        """Initialize RPC connections for all configured chains"""
        chains = {
            'ethereum': blockchain_config.ETH_RPC_URL,
            'polygon': blockchain_config.POL