### Tutorial: Building a Stacked Bar Chart with a Trended Line in Domo's Pro-Code Editor

In this tutorial, we will walk through the process of creating a stacked bar chart with a trended line using Domo's Pro-Code Editor and Chart.js. This guide assumes you are familiar with JavaScript, Chart.js, and Domo's data environment.

#### **Prerequisites**

*   Access to Domo's Pro-Code Editor.
*   Basic understanding of JavaScript and Chart.js.
*   A dataset uploaded to Domo.

* * *

### **Step 1: Set Up Your Pro-Code Environment**

1.  **Create a New Project in Pro-Code Editor**:
    *   Make sure your instance has Pro-Code Editor enabled.
    *   Navigate to your Asset Library.
    *   Click on the button top right of your screen called 'Pro-code Editor'. This will open a code editor in your browser.
    *   Now you can edit any of the files in your project.
2.  **File Structure**:
    
    *   In your project, these will be created automatically, all you have to do is edit them
        *   `index.html`
        *   `app.js`
        *   `app.css`
        *   `manifest.json`
    *   If you need, you can always change the way the `manifest.json` is shown. Just click on the button at the top right of the `manifest.json` file called 'Edit in JSON Editor'.

* * *

### **Step 2: Structure Your HTML (index.html)**

The `index.html` file will contain the structure of your app, including the canvas element where the chart will be rendered.

```html

<html>
<head>
    <link rel="stylesheet" href="app.css">
    <link href="//fonts.googleapis.com/css?family=Roboto+Mono:600,400,300" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="chartAreaWrapper">
        <canvas id="chart" height="400" width="1500">
</canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"> // Importing Chart.js
</script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels"> // Importing Datalabels
</script>
    <script src="https://unpkg.com/ryuu.js">
</script>
    <script src="app.js">
</script>
</body>
</html>
```
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"> // Importing Chart.js
</script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels"> // Importing Datalabels
</script>
```
Here we are importing Chart.js and Datalabels libraries to use on our Javascript.

### **Step 3: Define the Styling (app.css)**

The `app.css` file will control the appearance of your chart container, making it scrollable.

```css

body {
    width: 100vw;
}

.chartAreaWrapper {
    width: 3000px; /* Extend the width for scrolling */
    overflow-x: scroll;
}
```

### **Step 4: Write the JavaScript Logic (app.js)**

This is where the main bulk of the app logic will be. Although the snippets are separated, they are all in the same file. You can copy and paste them into your `app.js` file and it should display the chart, just remember to wire the dataset to the card.

#### Step 1: Fetch and Prepare Data

```javascript
// Fetch data using domo.get() method
const query = domo.get('/data/v1/dataset').then(res => createTheChart(res));

function createTheChart(data) {
    // Extract labels, stacks, and categories from the dataset
    var labels = [...new Set(data.map(item => item['Date']))];
    var stacks = [...new Set(data.map(item => item['Stacks']))];
    var categories = Object.keys(data[0]).filter(key => key.startsWith('Bar'));

````

*   `domo.get('/data/v1/dataset')` retrieves the dataset from Domo.
*   `createTheChart` function processes this data to create the chart.
*   Extract labels, stacks, and categories from the dataset using JavaScript's `map` and `Set` methods.

####Step 2: Define Colors and Create Datasets
-----------------------------------------

```javascript
    var colorPalette = [
        '#4e79a7',
        '#f28e2b',
        '#e15759',
        '#76b7b2',
        '#59a14f',
        '#edc949'
    ];

    var stackColors = {};
    stacks.forEach((stack, index) => {
        stackColors[stack] = colorPalette[index % colorPalette.length];
    });

    var datasets = categories.map(
category => {
        return stacks.map(
stack => {
            return {
                label: stack,
                data: labels.map(
label => {
                    var filteredData = data.filter(
item => item['Date'] === label && item[category] > 0 && item['Stacks'] === stack);
                    return filteredData.length > 0 ? filteredData.reduce((sum, item) => sum + item[category], 0) : 0;
                }),
                backgroundColor: stackColors[stack],
                stack: category,
                hidden: false,
            };
        });
    }).flat();
```

*   Define a color palette for different stacks.
*   Assign colors to each stack using `stackColors`.
*   Create datasets for each stack and category by mapping over labels and filtering data accordingly.

####Step 3: Calculate the Trended Line Data
---------------------------------------

```javascript
    // Calculate the billing percentage for the trended line
    var trendedPercentageData = labels.map(
label => {
        var billableHours = data.filter(
item => item['Date'] === label)
                                .reduce((sum, item) => sum + (item['Bar1'] || 0), 0);
        var scheduledHours = data.filter(
item => item['Date'] === label)
                                 .reduce((sum, item) => sum + item['Extra1'], 0);
        var outOfOfficeHours = data.filter(
item => item['Date'] === label)
                                   .reduce((sum, item) => sum + item['Extra2'], 0);
        return (scheduledHours - outOfOfficeHours) > 0 ? (billableHours / (scheduledHours - outOfOfficeHours)) * 100 : 0;
    });

    var lineData = {
        label: 'Billing %',
        data: trendedPercentageData,
        borderColor: 'rgba(255, 99, 132, 1)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        type: 'line',
        yAxisID: 'percentLine',
    };

    datasets.push(lineData);
```

*   Calculate the billing percentage for each label (date) by considering billable hours, scheduled hours, and out-of-office hours. This is just an example of a trended line calulation. You can replace it with your own logic.
*   Create a line dataset (`lineData`) for the trended line and add it to the datasets.

####Step 4: Create the Chart with Chart.js
--------------------------------------
   This is where we create the chart using Chart.js. Most of what is in the snippet is just customization of Chart.js options to get it to look the way I wanted. You can play around with the options by looking at the [Chart.js documentation](https://www.chartjs.org/docs/latest/).
```javascript
    // Create the chart using Chart.js
    var ctx = document.getElementById('chart').getContext('2d');
    Chart.register(ChartDataLabels);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    position: 'top',
                },
                y: {
                    beginAtZero: true,
                    offset: true,
                },
                percentLine: {
                    type: 'linear',
                    position: 'left',
                    beginAtZero: true,
                    grid: {
                        drawOnChartArea: false,
                    },
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        },
                        z: 1,
                    },
                    min: 0,
                    max: 120,
                }
            },
            plugins: {
                datalabels: {
                    labels: { // Label for the trended line
                        value: {
                            color: 'white',
                            font: {
                                size: 12
                            },
                            textStrokeWidth: 2,
                            textStrokeColor: 'black',
                            formatter: function(value, context) {
                                if (context.dataset.label === 'Billing %') {
                                    return value.toFixed(1) + '%';
                                } else {
                                    return value > 0 ? value : '';
                                }
                            }
                        },
                        legend: { // Label for each bar
                            display: true,
                            color: "black",
                            anchor: 'start',
                            align: 'start',
                            rotation: -90,
                            font: {
                                size: '10px',
                                weight: 'bold',
                            },
                            formatter: (value, context) => {
                                const { datasets } = context.chart.data;
                                const dataset = datasets[context.datasetIndex];
                                const stack = dataset.stack;

                                const stackLabels = categories.reduce((acc, category, index) => {
                                    acc[category] = `Bar ${index + 1}`;
                                    return acc;
                                }, {});

                                if (datasets.filter(
ds => ds.stack === stack).indexOf(dataset) === 0 && stack !== undefined) {
                                    return stackLabels[stack];
                                } else {
                                    return '';
                                }
                            }
                        }
                    },
                },
                legend: { // Label of each stack
                    position: 'bottom',
                    title: {
                        display: true,
                        padding: 40,
                    },
                    labels: {
                        font: {
                            size: 12
                        },
                        boxHeight: 4,
                        boxWidth: 8,
                        generateLabels: function(
) {
                            const legendItems = [];

                            stacks.forEach((item, datasetIndex) => {
                                const color = stackColors[item];
                                legendItems.push({
                                    text: item,
                                    fillStyle: color,
                                });
                            });
                            return legendItems;
                        }
                    },
                    maxHeight: 300,
                },
            },
        }
    });
}
```
*   Create and configure a Chart.js instance to render the chart.
*   Set up chart options including scales, plugins, and datalabels for better visualization. These are mostly customizable. I am using the `ChartDataLabels` plugin to show data labels. 

The following snippet takes care of adding a label under each bar, based on the stack it belongs to.
```javascript
formatter: (value, context) => {
   const { datasets } = context.chart.data;
   const dataset = datasets[context.datasetIndex];
   const stack = dataset.stack;

   const stackLabels = categories.reduce((acc, category, index) => {
         acc[category] = `Bar ${index + 1}`;
         return acc;
   }, {});

   if (datasets.filter(
ds => ds.stack === stack).indexOf(dataset) === 0 && stack !== undefined) {
         return stackLabels[stack];
   } else {
         return '';
   }
}
```
*This goes inside the `plugins.legend` object where we are adding labels for the bars*

### **Step 5: Define the Manifest File (manifest.json)**

The `manifest.json` file is crucial in Domo for defining your app's metadata and data mappings. Update it according to your dataset's structure.

```json

{
   "id": "26b83850-ac08-43d0-a90c-338005da39e3", // Unique ID created by pro-code editor
   "name": "Stacked Bars with Trended Line",
   "version": "0.0.1",
   "size": {
      "width": "6",
      "height": "2"
   },
   "mapping": [
      {
         "dataSetId": "182e83f3-b09a-4def-8ae1-b2b9d2685a61", // Example dataset
         "fields": [
            {
               "alias": "Stacks",
               "columnName": "Stacks",
               "type": "STRING"
            },
            {
               "alias": "Bar1",
               "columnName": "Bar1",
               "type": "LONG"
            },
            {
               "alias": "Bar2",
               "columnName": "Bar2",
               "type": "LONG"
            },
            {
               "alias": "Bar3",
               "columnName": "Bar3",
               "type": "LONG"
            },
            {
               "alias": "Date",
               "columnName": "Date",
               "type": "STRING"
            },
            {
               "alias": "Extra1",
               "columnName": "Extra1",
               "type": "LONG"
            },
            {
               "alias": "Extra2",
               "columnName": "Extra2",
               "type": "LONG"
            }
```
You can also use the GUI editor to edit the manifest file. Simply add the dataset directly using the GUI and it will create the schema by itself. Make sure that the Field Alias does not contain spaces.

### **Step 6: Save and Test Your App**

1. **Deploy the App**:
   - Save all files in the Pro-Code Editor.
   - Create a new card based on the Asset created by Pro-Code Editor.
   - Wire a dataset to the card within Domo.
   
2. **Test the App**:
   - Navigate to the card.
   - Verify that the chart displays correctly with the stacked bars and trended line.

### **Conclusion**

Congratulations! You've successfully built a stacked bar chart with a trended line in Domo's Pro-Code Editor. This tutorial provided you with the foundational steps to create a custom chart using JavaScript, Chart.js, and Domo's data platform. Feel free to customize and expand on this tutorial to fit your specific needs.

This guide should get you started on building more complex visualizations in Domo's Pro-Code Editor. Remember to explore Domo’s documentation for advanced features and customization options.
