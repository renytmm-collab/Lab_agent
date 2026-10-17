import bcrypt

def hash_password(password: str) -> str:
    """生成密码的哈希值"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """验证密码是否匹配"""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except ValueError:
        # 库里的值不是合法的 bcrypt 哈希（历史明文 / 手工插入的脏数据）
        # 直接返回 False，避免整个接口 500
        return False