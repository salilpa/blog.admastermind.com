Title: How to send automated adwords reports as email periodically
Date: 2015-08-20 17:00
Category: adwords
Tags: google adwords reporting tool, adwords scripts, automated email
Author: Salil Panikkaveettil
Summary: Various ways to schedule adwords reports and their respective advantages and disadvantages.

Every marketer wants to be on top of their data as frequently as it is possible. In an extremely dynamic environment like 
AdWords, Its important to be up to date with your campaigns almost daily. Let us look at the most common reports that AdWords 
experts track and steps to automate them.

AdWords Report Types
--------------------
Here are the top reports in no particular order

- Account Performance Report
- Campaign Performance Report
- Ad Group Performance Report
- Keyword Performance Report
- Search Term Performance Report

Out of these reports, the one report i track daily is the campaign performance report. This report gives a bird's eye view of all
the campaigns running in your account and gives an early indication of things going wrong. 

AdWords Scheduled Emails
------------------------

AdWords lets you [schedule reports](https://support.google.com/adwords/answer/2404176?hl=en "Official AdWords help") periodically. 
Although helpful, there are some serious limitations.

- All emails have a link to download the report from and not the report itself. To download the report, one needs to log in to adwords account.
This becomes a huge hassle if you are accessing reports from different devices.
- Emails cannot be sent to people without the account access. Although a good security feature, There will be times the reports need to be sent to 
senior management who necessarily need not have AdWords account access.
- Reports cannot be attached to the emails sent.
- HTML emails are not supported.


AdWords Scripts
---------------

AdWords Scripts solve the serious limitations by providing a programmatic way to retrieve and email data. Main advantages of 
AdWords Scripts are as follows

- Can send email reports to people who may not have adwords account access.
- Emails can be formatted as simple text or html
- Reports can be attached as pdf, csv reports in the email.

There are some limitations of AdWords Scripts also

 - Need to have programming expertise to create reports
 - Using the same reports is a tedious task
 - Customizing reports is not easy & takes time and change in the script itself
 - A small change in the script has to be replicated across multiple accounts by copy pasting the same code
 
 Here is a free script for sending last 30 days campaign performance report. [github](https://github.com/AdNabu/AdWords-Reports-Sample-Script)
 
```javascript
function main() {
  var date = getCurrentDate();
  var titles = ["Campaign", "Clicks", "Impressions", "Conversions", "Cost","Cost/conversion"];
  var last_30_days = runReport("LAST_30_DAYS","CAMPAIGN_PERFORMANCE_REPORT");
  var last_30_days_total = runReport("LAST_30_DAYS","ACCOUNT_PERFORMANCE_REPORT");
  last_30_days_total[0][0] = 'Total';
  last_30_days.push(last_30_days_total[0]);
  var last_30_days_html = arrayToTable(last_30_days, titles, "Campaign Stats for Last 30 Days");
  var content = last_30_days_html;
  
  mail("marketing@adnabu.com", "AdWords Campaign Stats as on " + date, content);
}

function getCurrentDate(){
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth()+1; //January is 0!
  var yyyy = today.getFullYear();

  if(dd<10) {
    dd='0'+dd
  } 

  if(mm<10) {
    mm='0'+mm
  } 

  today = dd+'/'+mm+'/'+yyyy;
  
  return today;
}

function runReport(time_range,report_type) {
  if(report_type == "CAMPAIGN_PERFORMANCE_REPORT"){
    var select_name = "CampaignName"
    var report = AdWordsApp.report(
      'SELECT CampaignName, Clicks, Impressions, ConvertedClicks, Cost, CostPerConvertedClick ' +
      'FROM ' + report_type + 
      ' WHERE  Impressions > 0 AND Clicks > 0 AND CampaignStatus = ENABLED '+
      'DURING ' + time_range + ' '
    );
  }
  if(report_type == "ACCOUNT_PERFORMANCE_REPORT") {
    var select_name = "AccountDescriptiveName"
    var report = AdWordsApp.report(
      'SELECT AccountDescriptiveName, Clicks, Impressions, ConvertedClicks, Cost, CostPerConvertedClick ' +
      'FROM ' + report_type + 
      ' WHERE  Impressions > 0 AND Clicks > 0 '+
      'DURING ' + time_range + ' '
    );
  }

  var rows = report.rows();
  var report = []
  while (rows.hasNext()) {
    var row = rows.next();
    var campaignName = row[select_name];
    var clicks = row['Clicks'];
    var impressions = row['Impressions'];
    var cost = row['Cost'];
    var conversions = row['ConvertedClicks'];
    var costperConversion = row['CostPerConvertedClick'];
    report.push([campaignName, clicks, impressions, conversions, cost, costperConversion]);
  }
  Logger.log(report);
  return report;
}

function mail(to, subject, content){
  MailApp.sendEmail({
    to: to,
    subject: subject,
    htmlBody: content,
  });
}

function arrayToTable(report_array, titles, heading){
  var html_table = "<h2>" + heading + "</h2>";
  
  html_table += "<table border='1'><tr>";
  
  for (var i=0; i<titles.length; i++){
    html_table += "<th>" + titles[i] + "</th>";
  }
  
  html_table += "</tr>";
  
  for (var j=0; j<report_array.length; j++){
    html_table += "<tr>";
    
    for (var k=0; k<report_array[j].length; k++){
      html_table += "<td>" + report_array[j][k] + "</td>";
    }
    
    html_table += "</tr>";
  }
  
  html_table += "</table>";
  Logger.log(html_table);
  return html_table;
}

function sum_array(report_array){
  
  var result = ["Total"];
  
  for (var k=1; k<report_array[0].length; k++){
    result[k] = 0.0;
  }
  
  for (var j=0; j<report_array.length; j++){
    for (var k=1; k<report_array[j].length; k++){
      result[k] += (+(report_array[j][k]).replace(',', ''));
    }
  }
  for (var k=1; k<report_array[0].length; k++){
    result[k] = Math.round(result[k]);
  }
  
  Logger.log(result);
  return result;
  
}
```
 
Other Sample AdWords Scripts for reporting.

- [Search Query Report](https://developers.google.com/adwords/scripts/docs/solutions/search-query)
- [Keyword Performance Report](https://developers.google.com/adwords/scripts/docs/solutions/keyword-performance)
- [Ad Performance Report](https://developers.google.com/adwords/scripts/docs/solutions/ad-performance)
- [Account Summary Report](https://developers.google.com/adwords/scripts/docs/solutions/account-summary)


AdNabu Reporting for AdWords
----------------------------

AdNabu simplifies the entire process of reporting. Within a few clicks, One can create a scheduled report which can run 
at any time of day/week/month. These reports are mobile optimized and highly customizable as per need. Biggest advantages of
AdNabu platform are

- Ability to schedule reports any time
- HTML formatted emails
- Ability to send to multiple email addresses
- Includes graphical overview of campaigns which can be segmented on day/week/month
- Highly customizable reports with all main variables available

Below is a sample report sent through AdNabu's [AdWords Report Creation Tool](https://www.adnabu.com/products/report/creation "AdWords Reporting Tool")

![Sample AdNabu AdWords Campaign Performance Report]({filename}/images/reports/sample_report.png)

Start your [free trial for AdWords Reporting Tool](https://www.adnabu.com/plans/pricing/ "AdWords Reporting Tool") today.






