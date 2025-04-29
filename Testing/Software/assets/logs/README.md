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
