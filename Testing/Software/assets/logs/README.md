# Quality Assurance Logs

This directory contains logs of the quality assurance process for the UTHP software. The logs are organized by date and time, and contain information about the [testing process](https://github.com/SystemsCyber/meta-uthp/tree/scarthgap/recipes-devtools/uthp-tests/files/uthp-tests), including the test cases, test results, and unique identifiers for the test runs.

> To add a new log file, create a new directory with the name of the UTHP ([UTHP-R1-XXXX](./UTHP-R1-XXXX/)) and copy the contents of the log results to that directory:

```
git clone https://github.com/SystemsCyber/UTHP
cd UTHP/Testing/Software/assets/logs
mkdir UTHP-R1-XXXX
cp /path/to/logfile.log UTHP-R1-XXXX/
```

## QA entry format:

| Date       | Time | UTHP Serial Number | Test Results | Test Cases | Test Run ID |
|------------|------|--------------------|--------------|------------|-------------|
| 2021-08-01 | 12:00| UTHP-R1-XXXX       | PASS/FAIL    | X          | core        |

## Test Results: