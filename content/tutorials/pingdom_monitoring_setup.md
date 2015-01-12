Title: How to configure monitoring using Pingdom and AdNabu
Date: 2015-01-05 20:00
Category: tutorials
Tags: pingdom, tutorial, monitoring, 
Author: Suvodhoy Sinha
Summary: This tutorial shows how to setup monitoring using Pingdom

The following is a step by step procedure on how to setup a [monitoring check](http://www.adnabu.com/products/monitor) in Pingdom and configuring an alerting webhook.

Register in AdNabu
------------------

![Adnabu Main Site]({filename}/images/tutorial/pingdom/main_site.png)

[Register](https://www.adnabu.com/accounts/register/ "AdNabu signup link") 

![Adnabu Registration Box]({filename}/images/tutorial/pingdom/registration_form.png)

or [Login](http://www.adnabu.com/accounts/login/ "AdNabu login link") if you already have an account.

![Adnabu Login Box]({filename}/images/tutorial/pingdom/login_form.png)

Link your Google Oauth
----------------------

Click on the **Google Oauth** tab in the navigation bar or go to the following [link](http://www..adnabu.com/googleoauth/). Link your **Google Oauth** after reading the instructions carefully. 
Please note this is an important step in getting your secret key generated for your AdWords account/accounts.

Enable Campaign Monitoring
--------------------------

If you have successfully linked your **Google Oauth** account, you will be able to go to the [monitoring dashboard](http://www.adnabu.com/monitor/). 
The dashboard will contain your adwords account details or in case of an MCC account all your accounts details.
You can select which accounts you want to enable for monitoring. Once enabled you will be able to see the generated url along with the secret key which will serve as your alerting endpoint.

Signup in Pingdom
-----------------

[Signup](https://www.pingdom.com/signup/ "Pingdom signup link") in Pingdom or [login](https://my.pingdom.com/ "Pingdom login link") if you previously have a pingdom account. 
In case you want to try out, you can [signup free](https://www.pingdom.com/free "Pingdom free signup")

![Pingdom Free Signup]({filename}/images/tutorial/pingdom/free_signup.png)

Once logged in you will be prompted to fill in some basic details.

![Pingdom Personal Details]({filename}/images/tutorial/pingdom/basic_details.png)
![Pingdom Timezone Details]({filename}/images/tutorial/pingdom/timezone_details.png)

Create an Alerting Webhook
--------------------------

On the left sidebar you will see a tab called **Alerting**. Click on it and then click **Alerting Endpoints**. You will be have the following view on your screen. 
You can directly navigate to this [link](https://my.pingdom.com/newims/externalendpoints "Pingdom Alerting Endpoints") to access this page.

![Alerting Endpoints]({filename}/images/tutorial/pingdom/alerting_endpoint_page.png)

On the right hand top corner you will see a button to **Add New** endpoint. Click on it.

![New Alerting Endpoint]({filename}/images/tutorial/pingdom/new_endpoint.png)

Give a name to it and click on **Add Contact Method**.

![Contact Method]({filename}/images/tutorial/pingdom/contact_method.png)

Select the contact method as **URL/WEBHOOK** and paste the url as provided by the AdNabu details page. Please note the url is encoded and has to pasted as it is.

![Final Contact Method View]({filename}/images/tutorial/pingdom/final_contact_box.png)

Click on **Save Settings**.

![Final Endpoint View]({filename}/images/tutorial/pingdom/final_endpoint_view.png)

Creating a Check
----------------

Go to the left sidebar and click on [Dashboard](https://my.pingdom.com/dashboard/checks). On the top right hand corner you will find an option to **Add New**.

Give a name to your check and your site url.

![Adding New Check]({filename}/images/tutorial/pingdom/new_check.png)

Scroll down to choose an alert policy. Select **Extremely Critical**. Currently the alert will be assigned to the user who created the check. Hover over the policy to find the **Edit** button on the right.

![Choose Alert Policy]({filename}/images/tutorial/pingdom/choose_alert_policy.png)

On the edit page click on the small arrow and click edit.

![Edit Alert Policy]({filename}/images/tutorial/pingdom/edit_policy.png)

Under **Assign to** remove the user and add the alerting endpoint.

![Assign Webhook]({filename}/images/tutorial/pingdom/assign_webhook.png)

Click on save and your settings are complete. You can open the check and confirm if your settings are all in place.

![Final Settings View]({filename}/images/tutorial/pingdom/final_check_view.png)