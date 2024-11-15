---
stoplight-id: 6ea9fcd9e478c
---

# Appstore Data Resources

App visualizations are powered by datasets that reside in Domo. The architecture of app DataSets is a critical part of building a great app and warrants careful consideration.  For example, creating DataSets that can be easily reproduced by Domo's customers will simplify app installation and result in a much better experience for customers.  This page is intended to introduce you to some data resources and information that will help you create apps with optimal data architectures.

## Sample Data Engine

If you don’t have credentials to all the connectors available on Domo (don’t worry, we don’t expect you to), then you’ll want to utilize our Sample Data Engine to power your budding app.

The Sample Data Engine is a powerful tool to give you the data you need from the most widely used connectors so you can focus on building your app rather than producing compatible, fictitious data.

Modocorp, the fictitious company on which the Sample Data Engine reports are based, is a large, technical company with an affinity to using as many applications as possible and, lucky for us, maintaining relationships between applications as much as possible. For example, you’ll see the same employees in their HR system as well as their recruiting and hiring systems. Likewise, you’ll see the same customer base in their PM systems that already flowed through their CRM systems.

Though fictitious, the datasets you’ll find in the Sample Data Engine maintain compatibility with the real connectors, so your customers will see the same thing you submit to the Domo Appstore when initially installed and their data connection experience is simplified because there is no guesswork on where the data can potentially come from. Summarized – there are no surprises between you and your customers when you use the Sample Data Engine to power your visualizations.

Overall benefits to powering your development with Sample Data Engine reports:
<ol>
 	<li>Compatible with the most widely used connectors</li>
 	<li>Provides real-to-life fictitious data</li>
 	<li>Complies with sensitive data requirements</li>
 	<li>Bridges the gap between the one-source requirement and your multiple connector apps</li>
</ol>


## Data Architecture

<p class="doc-row-title">Data is the lifeblood of your app. It shapes your design, powers your visualizations, and provides the valuable insights your customers are seeking in Domo. As a publisher, you will have access to powerful tools you can use to manipulate your data to provide even richer insights to your customers. The way you choose to architect your data has a significant impact on the usability and value proposition of your app.</p>

<div class="small-pad-bottom">

One of the most important architectural considerations you will need to make as a publisher is which data sources your app will support. The more data sources you support, the more potential customers you will have. The Domo sample data engine provides data from all the most popular systems in use today, but it is up to you to decide which of them you want to support. To support more than one data source (or combination of data sources), you will need to choose from one of two high level architectures, each with its own pros and cons. In this section, we will review each architecture and its corresponding powerup experience from both the publisher and customer perspective.

</div>
<h3>Architecture 1 - System-specific Data</h3>
The first architectural model for supporting multiple data sources involves building and publishing a separate version of your app for each system (or combination of systems) you want to support. The benefit of this model is that your customer's data is much more likely to match the sample data grids powering your app, thus making powerup a snap. However, it requires that you the publisher build and maintain multiple versions of your app.
<h3>Publisher Experience</h3>
<div class="small-pad-bottom">

<img class="alignnone size-full wp-image-339" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-01.jpg" alt="dev_how_to copy-01" width="1100" height="" />

<img class="alignnone size-full wp-image-340" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-02.jpg" alt="dev_how_to copy-02" width="1100" height="" />

<img class="alignnone size-full wp-image-341" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-03.jpg" alt="dev_how_to copy-03" width="1100" height="" /><img class="alignnone size-full wp-image-342" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-04.jpg" alt="dev_how_to copy-04" width="1100" height="" />

</div>
<img class="alignnone size-full wp-image-410" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience15.png" alt="PublisherExperience1[5]" width="1100" height="" />
<div class="small-pad-bottom">
<h3>Customer Experience</h3>
<img class="alignnone size-full wp-image-345" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-07.jpg" alt="dev_how_to copy-07" width="1100" height="" /><img class="alignnone size-full wp-image-346" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-08.jpg" alt="dev_how_to copy-08" width="1100" height="" />
<h3>Architecture 2 - System-agnostic Data</h3>
The second architectural model for supporting multiple data sources involves authoring generic sample data grids for your customers to map to from the system of their choice. The benefits of this model are that you only need to maintain a single listing for your app. However, your customers must do a little more technical lifting on their side to power it up.
<h3>Publisher Experience</h3>
<img class="alignnone size-full wp-image-411" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience20.jpeg" alt="PublisherExperience2[0]" width="1100" height="" /> <img class="alignnone size-full wp-image-412" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience21.jpeg" alt="PublisherExperience2[1]" width="1100" height="" /> <img class="alignnone size-full wp-image-413" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience22.jpeg" alt="PublisherExperience2[2]" width="1100" height="" /> <img class="alignnone size-full wp-image-414" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience23.jpeg" alt="PublisherExperience2[3]" width="1100" height="" /> <img class="alignnone size-full wp-image-415" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience24.jpeg" alt="PublisherExperience2[4]" width="1100" height="" /> <img class="alignnone size-full wp-image-416" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/08173205/PublisherExperience25.jpeg" alt="PublisherExperience2[5]" width="1100" height="" />
<h3>Customer Experience</h3>
<img class="alignnone size-full wp-image-353" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-15.jpg" alt="dev_how_to copy-15" width="1100" height="" />

<img class="alignnone size-full wp-image-354" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-16.jpg" alt="dev_how_to copy-16" width="1100" height="" />

<img class="alignnone size-full wp-image-355" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/02/17003807/dev_how_to-copy-17.jpg" alt="dev_how_to copy-17" width="1100" height="" />

</div>


## Other Resources

Information about other data topics like the Data Center, data transforms, and connectors is available by following the links below:

- [No Code Story Apps](https://domo-support.domo.com/s/article/360043428433?language=en_US)
- [App Developer Framework Getting Data Guide](../../Apps/App-Framework/Guides/getting-data.md)

