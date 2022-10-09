#!/bin/bash
touch oldFiles.txt
grep -r jane_ /home/student-00-cdae4528af94/data|cut -d ' ' -f 3 > oldFiles.txt