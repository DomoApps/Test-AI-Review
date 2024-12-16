# Troubleshooting

Domo is committed to answering all of your App development questions, even when you’re burning the midnight oil. Feel free to check out our <a href="https://dojo.domo.com/t5/Domo-Developer/bd-p/DeveloperForum">Community Forum</a> for frequently asked questions. 


Try us: Our technical support consultants are there 24/7 to provide world-class service and help you make the most of your Domo experience. Please email <a href="http://support.domo.com/">support.domo.com</a>

#### My Collection is not Syncing to my Dataset
There are a few other things to check if your collection isn't syncing correctly to your Dataset:
<ol>
 	<li>Check that collection sync is enabled</li>
 	<li>Check that the owner of the dataset and the collection are the same person</li>
 	<li>Check if there are documents that need syncing (syncRequired: true)</li>
 	<li>Check documents in your collection to make sure they have the right types for exported fields - often, the issue is that at least one document in the collection has a property that isn't being cast correctly.</li>
</ol>

Sometimes developers confuse Typescript types (like "Number") with the column types that are supported for Domo datasets. Instead, use “DOUBLE”, “LONG”, or “DECIMAL” types. Please refer to the [AppDB API](../../../Domo-App-APIs/AppDB-API.md#defining-collections-in-the-manifest) documentation for the list of supported column types.
<h3>My App Won't Load a File</h3>
If this is a relative asset (it lives inside of your design) then use a forward slash `/` and make sure you don't have a typo in the path.

If it's an external resource (hosted outside of Domo) then you must load it with the `https://` protocol since Domo runs in that mode.
#### Errors When Installing on Windows

- Option 1: Install <a href="http://go.microsoft.com/fwlink/?LinkId=691126">Visual C++ Build Tools</a> using the <strong>Default Install</strong> option.
- Option 2: Install <a href="https://www.visualstudio.com/products/visual-studio-community-vs">Visual Studio 2015</a> (or modify an existing installation) and select <em>Common Tools for Visual C++</em> during setup. This also works with the free Community and Express for Desktop editions.
- Install <a href="https://www.python.org/downloads/">Python 2.7</a> (`v3.x.x`) is not supported), and run `npm config set python python2.7` (or see below for further instructions on specifying the proper Python version and path.)
- Launch cmd, `npm config set msvs_version 2015`


#### How to Submit a Bug
If you come across a bug while building your app, please follow these steps to make it easier for us to help you:
<ol>
 	<li>Create a separate app that demonstrates the bug in isolation.</li>
 	<li>Make sure the code is as small as possible and only related to the bug.</li>
 	<li>If the bug is data related, wire the app to a very simple webform dataset. Export the webform dataset as CSV and put it in your app directory.</li>
 	<li>Zip up the app directory and email it to Domo support.</li>
</ol>

Important: Please include the version of the CLI you are using in your email to support. You can get the version with the `domo --version command`

This will allow us to more quickly find and fix the bug you're reporting.

If you are reporting multiple issues, please send one separate app per issue.
