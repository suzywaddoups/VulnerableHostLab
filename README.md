# Cyber Tower Defense: Vulnerable Linux Host Lab
The purpose of this Linux Host Lab is to help you gain experience hardening an Ubuntu Linux VM so that it adheres to several security policies set in the scenario and the CIS Benchmark.  The python grading script should be used to check that the host was appropriately fixed.


This repository should be used to quickly switch a VM’s state from either secure or insecure.  We have created bash scripts that will automatically change the host’s settings.  The "vuln_state_settings.sh" script should be run to change the VM state to insecure before practicing securing the host.

 
To help instruct on what must do to secure the vulnerable Linux host, we have created a lab scenario document, as well as four lab walkthroughs for the following labs: 
      1. Insecure Service Clients 
      2. User & Password Management 
      3. SSH Server Configuration 
      4. SMB Secure Configuration 

The vulnerable Linux host setup, scenario, and lab walkthrough documents can be downloaded using the following link: 
https://byu.box.com/s/gnuimbmhlxipa7tlfm4x4sssmnew66fx  


The lab scenario document contains a background story and lists what Linux host settings must be hardened.  The document also contains instructions for how to run the grading script which will check if the system has been appropriately hardened.  The Linux host lab’s grading script is written in Python and will check to see if the Linux system was appropriately hardened.  In the repository's "grading_scritps" folder is a python grading script called "auto_grader.py". After editing the source code to fix the two vulnerabilities, the python grading script should be used to check that the web app vulnerabilities were appropriately fixed.


We have also created a vulnerable VM that already has the preconfigured system vulnerabilities and insecure settings that do not adhere to the Center for Internet Security’s (CIS) Benchmark for Ubuntu Linux set up. The packaged vulnerable web application VM can be downloaded using the following link: 
https://byu.box.com/s/gbqv2ddhdy7v1pjc5wcy7sstunuwmvbc
