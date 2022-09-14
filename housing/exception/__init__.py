import os
import sys


class housingExeption(Exception):
    def __init__(self,errorMessage:Exception,errorDetails:sys):
        super().__init__(errorMessage)
        
        self.errorMessage = housingExeption.getDetailedErrorMessage(errorMessage=errorMessage,errorDetails=errorDetails)

    @staticmethod
    def getDetailedErrorMessage(errorMessage:Exception,errorDetails:sys):
        _,_,exec_tb = errorDetails.exc_info()
        lineNum = exec_tb.tb_frame.f_lineno
        fileName = exec_tb.tb_frame.f_code.co_filename
        errorMessage = f"Error occur in scrip :{fileName} at line number : {lineNum} and error message is {errorMessage}"
        return errorMessage

    def __str__(self) -> str:
        return self.errorMessage

    def __repr__(self) -> str:
        return housingExeption.__name__.str()