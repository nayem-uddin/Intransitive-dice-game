import secrets,hashlib,hmac


class keygen:
  @classmethod
  def otk(self):
    return secrets.token_bytes(32)
  
  @classmethod
  def digest(self,key:bytes):
    return hashlib.sha3_256(key).hexdigest()

  @classmethod
  def keyDigest(self,key:bytes):
    return hashlib.sha3_256(key).hexdigest()

class HMAC:
  @classmethod
  def getMAC(self,key:bytes,value:int):
    return hmac.new(key,str(value).encode(),"sha3_256").hexdigest()