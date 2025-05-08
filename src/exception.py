
# Loads the sys module so you can access system-level info — especially for getting detailed error tracebacks.
import sys
import logging

# Defines a function that accepts:
# error: the actual error object (like ZeroDivisionError)
#error_detail: the sys module, to extract traceback info
def error_message_details(error, error_detail:sys):
 
#It’s a function from the sys module that returns detailed info about the last exception that occurred.
#It gives a tuple with 3 items:
#(exc_type, exc_value, exc_traceback)
#Value	        Meaning
#exc_type	    What type of error it was (like ZeroDivisionError)
#exc_value	    The actual error message (division by zero)
#exc_traceback	A special object that knows where the error happened (file, line number)
    _,_,exc_tb = error_detail.exc_info()

#from exc_tb, you can extract: file name, line number, code context
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))
    return error_message
    


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message       


