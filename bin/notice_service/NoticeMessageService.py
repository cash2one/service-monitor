#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def sendSMS(self, msg, phones):
    """
    Parameters:
     - msg
     - phones
    """
    pass

  def SendMail(self, msg, mails):
    """
    Parameters:
     - msg
     - mails
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def sendSMS(self, msg, phones):
    """
    Parameters:
     - msg
     - phones
    """
    self.send_sendSMS(msg, phones)
    self.recv_sendSMS()

  def send_sendSMS(self, msg, phones):
    self._oprot.writeMessageBegin('sendSMS', TMessageType.CALL, self._seqid)
    args = sendSMS_args()
    args.msg = msg
    args.phones = phones
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_sendSMS(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = sendSMS_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.rpcException is not None:
      raise result.rpcException
    return

  def SendMail(self, msg, mails):
    """
    Parameters:
     - msg
     - mails
    """
    self.send_SendMail(msg, mails)
    self.recv_SendMail()

  def send_SendMail(self, msg, mails):
    self._oprot.writeMessageBegin('SendMail', TMessageType.CALL, self._seqid)
    args = SendMail_args()
    args.msg = msg
    args.mails = mails
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_SendMail(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = SendMail_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.rpcException is not None:
      raise result.rpcException
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["sendSMS"] = Processor.process_sendSMS
    self._processMap["SendMail"] = Processor.process_SendMail

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_sendSMS(self, seqid, iprot, oprot):
    args = sendSMS_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = sendSMS_result()
    try:
      self._handler.sendSMS(args.msg, args.phones)
    except NoticeRPCException, rpcException:
      result.rpcException = rpcException
    oprot.writeMessageBegin("sendSMS", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_SendMail(self, seqid, iprot, oprot):
    args = SendMail_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = SendMail_result()
    try:
      self._handler.SendMail(args.msg, args.mails)
    except NoticeRPCException, rpcException:
      result.rpcException = rpcException
    oprot.writeMessageBegin("SendMail", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class sendSMS_args:
  """
  Attributes:
   - msg
   - phones
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'msg', (NoticeSMSMessage, NoticeSMSMessage.thrift_spec), None, ), # 1
    (2, TType.SET, 'phones', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, msg=None, phones=None,):
    self.msg = msg
    self.phones = phones

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.msg = NoticeSMSMessage()
          self.msg.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.SET:
          self.phones = set()
          (_etype3, _size0) = iprot.readSetBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.phones.add(_elem5)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSMS_args')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRUCT, 1)
      self.msg.write(oprot)
      oprot.writeFieldEnd()
    if self.phones is not None:
      oprot.writeFieldBegin('phones', TType.SET, 2)
      oprot.writeSetBegin(TType.STRING, len(self.phones))
      for iter6 in self.phones:
        oprot.writeString(iter6)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendSMS_result:
  """
  Attributes:
   - rpcException
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'rpcException', (NoticeRPCException, NoticeRPCException.thrift_spec), None, ), # 1
  )

  def __init__(self, rpcException=None,):
    self.rpcException = rpcException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.rpcException = NoticeRPCException()
          self.rpcException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendSMS_result')
    if self.rpcException is not None:
      oprot.writeFieldBegin('rpcException', TType.STRUCT, 1)
      self.rpcException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SendMail_args:
  """
  Attributes:
   - msg
   - mails
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'msg', (NoticeEmailMessage, NoticeEmailMessage.thrift_spec), None, ), # 1
    (2, TType.SET, 'mails', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, msg=None, mails=None,):
    self.msg = msg
    self.mails = mails

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.msg = NoticeEmailMessage()
          self.msg.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.SET:
          self.mails = set()
          (_etype10, _size7) = iprot.readSetBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString();
            self.mails.add(_elem12)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SendMail_args')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRUCT, 1)
      self.msg.write(oprot)
      oprot.writeFieldEnd()
    if self.mails is not None:
      oprot.writeFieldBegin('mails', TType.SET, 2)
      oprot.writeSetBegin(TType.STRING, len(self.mails))
      for iter13 in self.mails:
        oprot.writeString(iter13)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SendMail_result:
  """
  Attributes:
   - rpcException
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'rpcException', (NoticeRPCException, NoticeRPCException.thrift_spec), None, ), # 1
  )

  def __init__(self, rpcException=None,):
    self.rpcException = rpcException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.rpcException = NoticeRPCException()
          self.rpcException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SendMail_result')
    if self.rpcException is not None:
      oprot.writeFieldBegin('rpcException', TType.STRUCT, 1)
      self.rpcException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)