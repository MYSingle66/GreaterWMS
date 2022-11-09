import os
import pytest
from common.handle_path import temps_path,report_path

if __name__ == '__main__':
    logpath=os.path.join(temps_path)
    repath=os.path.join(report_path)
    pytest.main(['-vs', '--alluredir', '{}'.format(logpath), '--clean-alluredir'])
    os.system('allure generate {} -o {} --clean'.format(logpath,repath))

    # pytest.main()