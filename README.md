LT-notification
===============

LT Hub system for notification handling to avoid polluting everyone mails

Goals
------
The whole project revolves around the idea that not everyone wants to receive notifications of services (like jenkins, teamcity, jir or travis) by e-mail and do the filtering by themselves.
To tackle this issue, this tool is designed as a central HUB for notification handling and routing, its goals are to :

 * Provide API access points to broadcast notifications;
 * Provide API access points to handle subscriptions by users and medium;
 * Define and handle several medias to propagate notifications (Email, SMS, Jabber, HipChat ...);
 * Allow anyone to change its subscription using a simple UI and OpenID connection;

Bootstrap
---------

