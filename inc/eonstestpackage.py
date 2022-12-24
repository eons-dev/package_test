import logging
import eons

class eonstestpackage(eons.Functor):
    def __init__(this, name="Test Package"):
        super().__init__(name)
    
    def Function(this):
        logging.info("Test functor successfully executed")
        this.functionSucceeded = True
