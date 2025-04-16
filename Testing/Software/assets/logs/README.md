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
| UTHP-R1-0060 | PASS | hardware,core,plc,remote,can0-2 | SCB | all tests passed! (no safe-shutdown)|
