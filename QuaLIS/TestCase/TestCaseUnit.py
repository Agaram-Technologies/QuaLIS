from TestCoverage import TestCoverageUnit, TestCoverageAudittrail
from Utility import BrowserOperation, BasicOperation

name="cm4"

description="cm1"


driver=BrowserOperation.launchLIMS()



TestCoverageUnit.auditTrailUnitAdd(driver,name,description)

#TestCoverageUnit.unitDelete(driver,name)



