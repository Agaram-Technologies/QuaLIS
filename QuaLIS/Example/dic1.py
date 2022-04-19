from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation

oldName="cm"

oldDescription="Centi meter"

driver=BrowserOperation.launchLIMS()

TestCoverageUnit.auditTrailUnitAdd(driver,oldName,oldDescription,"No")