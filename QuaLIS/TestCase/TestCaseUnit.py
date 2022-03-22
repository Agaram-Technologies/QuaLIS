from TestCoverage import TestCoverageUnit, TestCoverageAudittrail
from Utility import BrowserOperation, BasicOperation

name="murali"

description="murali"


driver=BrowserOperation.launchLIMS()

TestCoverageUnit.auditTrailUnitAdd(driver,name,description)

TestCoverageUnit.unitDelete(driver,name)



