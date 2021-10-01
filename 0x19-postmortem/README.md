## Postmortem

# Apache2 (incident #1)
## Date:
2021-09-29

## Authors:
Charles Osoti

## Status:
Complete, solved successfully

## Issue Summary
On 2021-09-29 at 10:30pm EAT, users started experiencing a response with status code 500 which meant that the web server hosing our website was unable to serve the requested content. The entire website service was down for about 20 minutes. The root cause appears to be associated with the settings files on the Apache 2 web server application pointing to a nonexisting symlink. There was a typographical error in this settings file in which a .php file was typed as a .phpp file.

## Timeline
* 10:30 pm - After deployingan update to the Wordpress, I noticed that there was internal server errors in the HTTP response of code 500
* 10:35 pm - HTTP Testing was initiated and it was realized that the Apache2 webserver was unable to serve content
* 10:36 pm - Running processes were checked using the command **ps auxf**. The web server Apache2 and database MySQL were running without errors. This narrowed down the error to the PHP/Wordpress. 
* 10:37 pm - When debugging a Wordpress CMS, the first thing to do is change the debug mode to enabled by editing the configuration file **`/var/www/html/wp-config.php`**
* 10:38 pm - Using **`curl`**, the website returned a fatal error(status code 500) and further information by debug mode indicated that a file, **`/var/www/html/wp-includes/class-wp-locale.phpp`**, was missing but is required in the **`/var/www/html/wp-settings.php`**. But the extension **`.phpp`** does not exist thus, a typographical error. 
* 10:39 pm - To further confirm this error, I listed the files within the **`/var/www/html/wp-includes/`** and discovered the existence of the file, **`/var/www/html/wp-includes/class-wp-locale.php`** indicating a typographical error.
* 10.41 pm - the errror was fixed by using the command **`sed -i 's/phpp/php/' /var/www/html/wp-settings.php`**
* 10:42 pm - After successfully running the command, the web server worked perfectly as expected.
* 10.45 pm - To scale this fix to other web servers serving the web service, a puppet manifest was developed to solved this proplem at one go.
* 10:50 pm - the developed manifest was deployed on the remaining servers and the website service was brought back to 100% functional.

## Root Cause
The issue was caused by a typo in the settings file for Apache2 where the symbolic link filename did not exist. The **`wp-settings.php`** was pointing to **`locale-wp.phpp`** when the file that actually existed in the folder **`/var/www/html/locale/`** was called **`locale-wp.php`**. The issue was fixed by going into the **`wp-settings.php`** file and correcting the typo from **`.phpp`** to **`.php`** on the file called **`locale-wp.php`**. Since this code was deployed on all servers, this error caused a 100% outage. A puppet manifest to fix the typographical error was developed and deployed on all servers, reinstating service within 20 minutes of the outage.

## Preventative Measures
Effort should be made to test all code code before shipping especially when the deployment is wide scale.

#### Things to consider:
* establish code testing protocal before deployment
* note down every changes made to the configuration files at every minor and major updated to the web servers
