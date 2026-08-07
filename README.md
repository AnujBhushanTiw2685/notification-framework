# Component Shared Workflow


* This repo is the part of CICD project where it is used to trigger email when release run failure occurs due to some specified reasons or for providing run status for nightly trigger of all components along with the reason of failure
* The email is triggered to the executor and the recipient(s) providing specific description for failure reasons (when manually triggered) or providing the release run status for all the components during nightly run along with description of failure (if there exists any).