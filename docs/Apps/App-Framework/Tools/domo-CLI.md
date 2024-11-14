---
stoplight-id: rmfbkwje8kmqj
---

# Domo Apps CLI

The Domo Apps Command Line Interface (CLI) will be your main tool to 

- create
- publish
- edit

custom app designs to your Domo instance. 

Here's how to [install it](/docs/Apps/App-Framework/Quickstart/Setup-and-Installation.md). 

The following is an enhanced **reference** for the more **common** CLI commands. 

For a **complete** list of commands available, ask your version of the CLI with `domo --help` (refer to the Help section below).

### Help
---
If at any point you need a reminder on the available commands for the CLI you can run

```
$ domo -h
```

Additionally, you can get available options for a specific command

```
$ domo [command] -h
```

**OPTIONS**
* `-v, --version`: output the version number
* `-s, --ssl`: disable SSL
* `-m, --manifest <filename>`: specify a manifest file. Defaults to `manifest.json` in the current working directory.
* `-h, --help`: output usage information


### Common Commands
---
### dev

Spins up a local development server with the following features:

  * **Live Reload**: reloads when changes to code are detected
  * **App Sizing**: renders the app in a frame that honors the sizing and fullpage settings from the app manifest
  * **Data Proxy**: proxies basic XHR requests for data to the appropriate Domo instance, enabling local development with live data.

```
$ domo dev [options]
```

**OPTIONS**
* `-u, --userId`: Use a specific user. Helpful for testing app states where user Id is important
* `-e, --external`: exposes the dev server on a public IP address

#### Advanced Data Proxy
In order to enable proxying for advanced requests (like AppDB or the Files API), you must provide the Id of an app in your instance that the CLI can proxy to. You can add this app Id to your manifest under the property `proxyId` and, assuming that the Id is valid, proxying advanced requests with `domo dev` will automatically start working.

The app Id can be found as part of the URL for the iframe in which your app is displayed. It will be of the form XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX. To find the ID:

* Make sure the app has been published at least once with `domo publish`
* Publish a new card based on your app design, or navigate to an existing card made from your app design
* Right-click anywhere in the card and choose "Inspect element"
* Find the `<iframe>` that contains your app's code. The URL should be of the form `//{ID}.domoapps.prodX.domo.com?userId=...`
* Copy the ID found between `//` and `.domoapps`. That is your app's id.

App ids tie apps to cards. If you delete the card from which you retrieved the id, you will have to get a new one from another card created from your app design.

### init

Asks you some questions to initialize a new Custom App design template. Once complete be sure to follow the "Next Steps" provided.

<!-- theme: info -->
> #### No `mkdir` necessary
>
> `domo init` will create the folder for you

**PROMPTS**
* design name
* select a starter: see "STARTER PROMPTS"
* would you like to connect to any datasets? (Y/n): see "DATASET MAPPING PROMPTS"

**STARTERS**
* hello world: creates a basic project in a new directory with the following content

```
design-name
  - app.css
  - app.js
  - domo.js
  - index.html
  - manifest.json
```

* manifest only: adds a single `manifest.json` file to the current working directory

**DATASET MAPPING PROMPTS**
* dataset id: can be found in the URL of the dataset detail page in the Domo instance. `https://[customer].domo.com/datasources/[dataset id]/details/overview`
* dataset alias: the alias your app will use when requesting data from Domo

**Note**: Be sure to complete the field mapping portion in the `manifest.json`. Refer to the [manifest](../Guides/manifest.md#mapping) reference docs for more details on data mapping.

### login [options]

Authenticate to your Domo instance from the CLI. This is a requirement before doing other commands like `publish`, and for fetching data during `domo dev`. If no options are provided then you'll be prompted to choose from a list of previous instances or a "new instance", at which point you'll be prompted for instance name, username, and password.

```
$ domo login [options]
```

**OPTIONS**
* `i, --instance`: Domo instance (e.g. customer.domo.com)
* `u, --user-email`: user email
* `--no-upgrade-check`: prevent the CLI from checking for new versions and prompting for user input to upgrade or not

### owner <add|rm|ls>

Manage the owners of the Custom App design. Only owners of a design are able to manage that design from the CLI or the Asset Library within the Domo instance. Additionally, only owners of a design are authorized to deploy new apps based on said design.

```
$ domo owner [options] [add|rm|ls] joe.bob@mycompany.com
```

**OPTIONS**
* `-i, --design_id`: specify a design Id or defaults to the Id from the manifest file in the current working directory

### publish 

Uploads all the assets of your current working directory as a Custom App design. You can choose to ignore certain files, meaning domo publish will not upload those files. Any node_modules directories are ignored by default. Refer to the [manifest](../Guides/manifest.md#ignore) reference docs for more details on ignoring files.

If an existing ID is not found in the manifest then a new design will be created and the manifest file will be updated with the newly created design Id. Existing designs will be updated.

```
$ domo publish [options]
```

**OPTIONS**
* `-g, --go`: open the design in the Asset Library after publishing

### release

Locks a design version for submitting to the Domo Appstore. Once a version is released you can't make further changes to it. You can, however, work on a new version by bumping the version in the manifest file. 

```
$ domo release
```