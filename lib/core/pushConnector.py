#!/usr/bin/env python
# encoding: utf-8

from lib.core.fileConnector import FileConnector

class PushConnector(FileConnector):
    """Push class extends from FileConnector"""

    # Constructor
    # param: url, password, server, fileList
    # return: none
    def __init__(self, url, password, server, fileList):
        FileConnector.__init__(self, url, password, server, fileList)
        self.localFilePath = self.fileList[0]
        self.remoteFilePath = self.fileList[1]

    # Upload file
    # param: none
    # return: bool
    def uploadFile(self):
        f = file(self.localFilePath, 'r')
        fileContent = f.read()
        f.close()
        payload = self.payloader.getUploadPayload(self.remoteFilePath, fileContent)
        status, result = self.postToServer(payload)
        if result != '[S]NOFILE[E]':
            print '+ Uploading Successful'
            print ''
        else:
            print '+ Uploading Failed'
            print ''

    # The callable method to launch the connector
    # param: none
    # return: none
    def launch(self):
        if FileConnector.launch(self) != 'fail':
            self.uploadFile()
