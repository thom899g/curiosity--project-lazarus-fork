"""
Configuration and environment management for Project Lazarus Fork.
Centralized configuration prevents hardcoded values and ensures type safety.
"""
import os
from dataclasses import dataclass
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class BlockchainConfig:
    """Configuration for blockchain RPC connectivity"""
    ETH_RPC_URL: str = os.getenv("ETH_RPC_URL", "https://mainnet.infura.io/v3/your-project-id")
    POLYGON_RPC_URL: str = os.getenv("POLYGON_RPC_URL", "https://polygon-mainnet.infura.io/v3/your-project-id")
    ARBITRUM_RPC_URL: str = os.getenv("ARBITRUM_RPC_URL", "https://arbitrum-mainnet.infura.io/v3/your-project-id")
    WALLET_PRIVATE_KEY: str = os.getenv("WALLET_PRIVATE_KEY", "")
    MAX_GAS_PRICE_GWEI: int = int(os.getenv("MAX_GAS_PRICE_GWEI", "150"))
    CONFIRMATION_BLOCKS: int = int(os.getenv("CONFIRMATION_BLOCKS", "3"))

@dataclass
class FirebaseConfig:
    """Configuration for Firebase public ledger"""
    CREDENTIALS_PATH: str = os.getenv("FIREBASE_CREDENTIALS_PATH", "./firebase-credentials.json")
    DATABASE_URL: str = os.getenv("FIREBASE_DATABASE_URL", "https://project-lazarus.firebaseio.com")
    COLLECTION_NAME: str = os.getenv("FIREBASE_COLLECTION", "swap_logs")

@dataclass
class TradingConfig:
    """Configuration for A/B testing framework"""
    MIN_PROFIT_THRESHOLD_WEI: int = int(os.getenv("MIN_PROFIT_THRESHOLD_WEI", "10000000000000"))  # 0.00001 ETH
    MAX_SLIPPAGE_BPS: int = int(os.getenv("MAX_SLIPPAGE_BPS", "50"))  # 0.5%
    TEST_DURATION_SECONDS: int = int(os.getenv("TEST_DURATION_SECONDS", "300"))
    SAMPLE_SIZE_PER_TEST: int = int(os.getenv("SAMPLE_SIZE_PER_TEST", "10"))

@dataclass
class SystemConfig:
    """System-level configuration"""
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    HEARTBEAT_INTERVAL_SECONDS: int = int(os.getenv("HEARTBEAT_INTERVAL_SECONDS", "30"))
    RAM_REQUEST_THRESHOLD_WEI: int = int(os.getenv("RAM_REQUEST_THRESHOLD_WEI", "100000000000000000"))  # 0.1 ETH
    TERMINATION_THRESHOLD_CYCLES: int = int(os.getenv("TERMINATION_THRESHOLD_CYCLES", "10"))

# Global configuration instances
blockchain_config = BlockchainConfig()
firebase_config = FirebaseConfig()
trading_config = TradingConfig()
system_config = SystemConfig()