# Quality Assurance Logs

This directory contains logs of the quality assurance process for the UTHP software. The logs are organized by date and time, and contain information about the [testing process](https://github.com/SystemsCyber/meta-uthp/tree/scarthgap/recipes-devtools/uthp-tests/files/uthp-tests), including the test cases, test results, and unique identifiers for the test runs.

> To add a new log file, create a new directory with the name of the UTHP ([UTHP-R1-XXXX](./UTHP-R1-XXXX/)) and copy the contents of the log results to that directory:

```
git clone https://github.com/SystemsCyber/UTHP
cd UTHP/Testing/Software/assets/logs
mkdir UTHP-R1-XXXX
cp /path/to/logfile.txt UTHP-R1-XXXX/
```

Create your own branch to track your log files with git:

```
git checkout -b logs-<your-name>
git add .
git commit -m "Add logs for UTHP-R1-XXXX"
git push origin logs-<your-name>
```

Then create a pull request to merge your branch into the main repository. If you are unable to push to the repository, you can email the maintainers of the repository with your issue or request.

After submitting your logs, sign off with your initials to indicate that the logs have been reviewed and approved as passing the quality assurance process. If your test failed, please put the reason for the failure in a README.md file in the directory of the UTHP serial number, similar to the [example](./UTHP-R1-XXXX).

## QA entry format:

> Note: Test Cases column should be comma separated.

| UTHP Serial Number | Test Results | Test Cases | Signed off by |
|--------------------|--------------|------------|---------------|
| UTHP-R1-XXXX       | PASS/FAIL    | core,hardware       | SB            |
| UTHP-R1-XXXX       | PASS/FAIL    | core,plc   | SB            |
| UTHP-R1-XXXX       | PASS/FAIL    | core,plc,remote | SB        |
| UTHP-R1-XXXX       | PASS/FAIL    | core,plc,remote | SB        |
| UTHP-R1-XXXX       | PASS/FAIL    | core,plc,remote,can0-2 | SB        |

## Test Results:

| UTHP Serial Number | Test Results | Test Cases | Signed off by | Notes |
|--------------------|--------------|------------|---------------|---------------|
|      UTHP-R1-0018  |   PASS       | hardware,core,plc,remote,can0-2     |  SCB     | all tests passed! |
|     UTHP-R1-0032   |       PASS  |  hardware,core,plc,remote,can0-2     |  CTG  | all tests passed! |
| UTHP-R1-0089 |   PASS  | hardware,core,plc,remote,can0-2 | SCB | all tests passed! |
| UTHP-R1-0083 | PASS | hardware,core,plc,remote,can0-2 | SCB | all tests passed! |
| UTHP-R1-0011 | PASS | hardware,core,plc,remote,can0-2 | SS  | all tests passed! (no safe-shutdown)|
| UTHP-R1-0060 | PASS | hardware,core,plc,remote,can0-2 | SCB | all tests passed! (no safe-shutdown)|
| UTHP-R1-0021 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0038 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0066 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0092 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0019 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0001 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0068 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0073 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0004 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0029 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0081 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0036 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0013 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0026 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0047 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0088 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0093 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0043 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0012 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0002 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0006 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0050 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0031 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0076 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0063 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0057 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0080 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0084 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0023 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0003 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0056 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0094 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0027 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0010 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0008 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0086 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0100 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0064 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0078 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0062 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0085 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0054 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0005 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0030 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0037 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0040 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0070 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0059 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0033 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0028 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0020 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0017 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0045 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0007 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0051 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0039 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0015 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0074 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0075 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0098 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0046 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0082 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0095 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0069 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0049 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0055 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0022 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0034 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0090 | PASS | hardware,core,plc,remote,can0-2 | SB | all tests passed! (no safe-shutdown)|
| UTHP-R1-0016 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0091 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0099 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0071 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0024 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0077 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0052 | PASS | hardware,core,plc,remote,can0-2 | CG | all tests passed! (no safe-shutdown)|
| UTHP-R1-0048 | PASS | hardware,core,plc,remote,can0-2 | CG | all tests passed! (no safe-shutdown)|
| UTHP-R1-0035 | PASS | hardware,core,plc,remote,can0-2 | SB | all tests passed! (no safe-shutdown)|
| UTHP-R1-0079 | PASS | hardware,core,plc,remote,can0-2 | CG | all tests passed! (no safe-shutdown)|
| UTHP-R1-0058 | PASS | hardware,core,plc,remote,can0-2 | CG | all tests passed! (no safe-shutdown)|
| UTHP-R1-0061 | PASS | hardware,core,plc,remote,can0-2 | CG | all tests passed! (no safe-shutdown)|
| UTHP-R1-0044 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0025 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0087 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0096 | PASS | hardware,core,plc,remote,can0-2 | SB | all tests passed! (no safe-shutdown)|
| UTHP-R1-0072 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! (no safe-shutdown)|
| UTHP-R1-0041 | PASS | hardware,core,plc,remote,can0-2 | SB | all tests passed! (no safe-shutdown)|
| UTHP-R1-0067 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0053 | PASS | hardware,core,plc,remote,can0-2 | SS | all tests passed! |
| UTHP-R1-0014 | PASS | hardware,core,plc,remote,can0-2 | SB | all tests passed! |
| UTHP-R1-0097 | PASS | hardware,core,plc,remote,can0-2 | CG | all tests passed! |

